import random

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from services import get_subjects, read_questions

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

subjects = get_subjects()


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
    return templates.TemplateResponse('home.html', {"request": request})


@app.get('/pdr')
def pdr(request: Request):
    print(subjects)
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
    subject_name = subjects[str(pk)]["title"]
    return templates.TemplateResponse("subject.html",
                                      {"request": request, 'questions': questions, 'title': subject_name})


@app.get('/pi-number')
def pi_number(request: Request):
    return templates.TemplateResponse('pi-number.html', {"request": request})


@app.get('/calc')
def calc(request: Request):
    return templates.TemplateResponse('calc.html', {"request": request})


@app.get('/trader-calc')
def trader_calc(request: Request):
    return templates.TemplateResponse('trader-calc.html', {"request": request})


@app.get('/rr-calc')
def rr_calc(request: Request):
    return templates.TemplateResponse('rr-calc.html', {"request": request, "title": "Win calc"})


@app.get('/words')
def words(request: Request):
    return templates.TemplateResponse('words.html', {"request": request})


if __name__ == "__main__":
    uvicorn.run('app:app', host="0.0.0.0", port=8001, reload=True, workers=2)
