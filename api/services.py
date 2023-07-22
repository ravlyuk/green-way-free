import json
import os

import requests
from fastapi import HTTPException

from config import headers, json_folder, url
from request_data import request_data


def download_questions():
    subjects = {}
    for subject, data in request_data.items():
        print(f'Download questions: "{subject}"')
        resp = requests.post(url=url, data=data, headers=headers).text

        resp = resp.replace('&ndash;', '-') \
            .replace('&laquo;', "«") \
            .replace('&raquo;', "»") \
            .replace('ПДР online', '') \
            .replace('&rsquo;', 'ʼ') \
            .replace('&mdash;', '-') \
            .replace('&lsquo;', 'ʼ') \
            .replace('&quot;', "'") \
            .replace('&ldquo;', "'") \
            .replace('&rdquo;', "'")

        resp_dict = json.loads(resp)

        if not isinstance(resp_dict, list):
            continue

        subject_slug = float(subject.split(' ')[0].strip('.'))
        subjects.update({float(subject_slug): subject.replace('Обовязки', 'Обовʼязки')})

        with open(f'{json_folder}/{subject_slug}.json', 'w') as file:
            json.dump(resp_dict, file, indent=4, sort_keys=True, ensure_ascii=False)

    with open(f'subjects.json', 'w') as file:
        json.dump(subjects, file, indent=4, sort_keys=True, ensure_ascii=False)


def read_questions(subject_slug: float | str):
    try:
        with open(f'{json_folder}/{subject_slug}.json', 'r') as file:
            return json.loads(file.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Subject not found")


def get_subjects() -> dict | None:
    try:
        with open(f'subjects.json', 'r') as file:
            return json.loads(file.read())

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Subject not found")


def combine_json_files(input_folder, output_file):
    combined_data = []

    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(input_folder, filename)

            # Read and parse JSON data from the file
            with open(file_path, "r") as file:
                json_data = json.load(file)

                combined_data.append(json_data)

    with open(output_file, "w") as output:
        json.dump(combined_data, output, ensure_ascii=False, indent=4, sort_keys=True, )


if __name__ == '__main__':
    download_questions()
    combine_json_files(json_folder, json_folder + "/all_questions.json")
