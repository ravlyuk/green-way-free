import json
import os

import requests
from fastapi import HTTPException

from config import headers, json_folder, url
from request_data import request_data


def download_questions():
    for subject, data in request_data.items():
        print(f'Download questions: "{subject}"')
        resp = requests.post(url=url, data=data, headers=headers).text
        resp = resp.replace('&ndash;', '-') \
            .replace('&laquo;', "«") \
            .replace('&raquo;', "»") \
            .replace('ПДР online', '') \
            .replace('&rsquo;', 'ʼ') \
            .replace('&mdash;', '-') \
            .replace('&lsquo;', 'ʼ')
        resp_dict = json.loads(resp)

        with open(f'{json_folder}/{subject}.json', 'w') as file:
            json.dump(resp_dict, file, indent=4, sort_keys=True, ensure_ascii=False)


def read_questions(subject: str):
    try:
        with open(f'{json_folder}/{subject}.json', 'r') as file:
            return json.loads(file.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Subject not found")


def get_subjects():
    subjects = {}
    for file_name in os.listdir(json_folder):
        if file_name == '.gitkeep':
            continue
        subjects.update({float(file_name.split(' ')[0].strip('.')): file_name.replace('.json', '')})

    return subjects


if __name__ == '__main__':
    download_questions()
