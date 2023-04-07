from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from services import get_subjects, read_questions

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get('/pdr')
def index(request: Request):
    subjects = get_subjects()
    subjects = dict(sorted(subjects.items()))
    return templates.TemplateResponse('home.html', {"request": request, 'subjects': subjects})


@app.get('/{pk}')
def subject(request: Request, pk: int | float):
    subject_name = get_subjects().get(pk)
    questions = read_questions(subject_name)
    title = questions[0]['h1']
    return templates.TemplateResponse("subject.html", {"request": request, 'questions': questions, 'title': title})

#
# if __name__ == "__main__":
#     uvicorn.run('app:app', host="0.0.0.0", port=8001, reload=True, workers=2)
