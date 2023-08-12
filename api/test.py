questions = ",".join([str(num) for num in list(range(0, 3500))])

payload = f'method=getJsonQuestions&data=%7B%22questionIds%22:%22{questions}%22,%22locale%22:%22uk%22%7D'
print(payload)
