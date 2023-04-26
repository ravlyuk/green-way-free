import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from services import get_subjects, read_questions

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


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
    title = questions[0]['h1']
    return templates.TemplateResponse("subject.html", {"request": request, 'questions': questions, 'title': title})


if __name__ == "__main__":
    uvicorn.run('app:app', host="0.0.0.0", port=8001, reload=True, workers=2)
