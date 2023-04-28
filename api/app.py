import uvicorn
from fastapi import FastAPI, Request, Body
from fastapi.templating import Jinja2Templates
from sqlalchemy import select, update
from starlette.staticfiles import StaticFiles

from sqlmodel import SQLModel, create_engine, Session

from services import get_subjects, read_questions

from models import QuizProgress, Base
from db import engine
from depends import Session

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# quiz_progress = QuizProgress(user_id=1, question_id=1, answer_index=2)
# with Session(engine) as session:
#     session.add(quiz_progress)
#     session.commit()


@app.get('/')
def home(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@app.get('/pdr')
def pdr(request: Request):
    subjects = get_subjects()
    subjects = dict(sorted(subjects.items()))
    return templates.TemplateResponse('pdr-list.html', {"request": request, 'subjects': subjects})


@app.get('/{pk}')
def subject(request: Request, pk: int | float):
    subject_name = get_subjects().get(pk)
    questions = read_questions(subject_name)
    return templates.TemplateResponse("subject.html", {"request": request, 'questions': questions, 'title': subject_name})


@app.post("/save_progress")
async def save_progress(body: dict = Body(...)):
    print('starting')

    user_id = body['user_id']
    question_id = body['question_id']
    answer_index = body['answer_index']
    subject = body['subject']

    print(body)

    existing_answer = await Session.select(select(QuizProgress).where(QuizProgress.user_id == user_id).where(
        QuizProgress.question_id == question_id))

    obj = existing_answer.fetchone()

    if existing_answer:
        existing_answer.answer_index = answer_index
        Session.add(obj)
        Session.commit()
        Session.refresh(obj)

    else:
        new_answer = QuizProgress(user_id=user_id, question_id=question_id, answer_index=answer_index,
                                  subject=subject)
        Session.add(new_answer)

    Session.commit()

    return {"status": "success"}


if __name__ == "__main__":
    uvicorn.run('app:app', host="0.0.0.0", port=8001, reload=True, workers=2)
