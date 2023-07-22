import random

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from services import get_subjects, read_questions

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/pdr/exam')
def exam(request: Request):
    all_questions = []
    questions = read_questions('all_questions')
    for question in questions:
        all_questions.extend(question)
    random_questions = random.choices(all_questions, k=20)
    return templates.TemplateResponse(
        "exam.html",
        {
            "request": request, 'questions': random_questions,
            'title': '20 випадкових питань'
        }
    )


@app.get('/')
def home(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@app.get('/pdr')
def pdr(request: Request):
    subjects = get_subjects()
    return templates.TemplateResponse('pdr-list.html', {"request": request, 'subjects': subjects})


@app.get('/pdr/about')
def about(request: Request):
    return templates.TemplateResponse('about.html', {"request": request})


@app.get('/pdr/contact')
def contact(request: Request):
    return templates.TemplateResponse('contact.html', {"request": request})


@app.get('/pdr/{pk}')
def subject(request: Request, pk: int | float):
    questions = read_questions(pk)
    subject_name = get_subjects()[str(pk)]
    return templates.TemplateResponse("subject.html",
                                      {"request": request, 'questions': questions, 'title': subject_name})


if __name__ == "__main__":
    uvicorn.run('app:app', host="0.0.0.0", port=8001, reload=True, workers=2)
