import csv
from functools import lru_cache


@lru_cache
def read(path="src/jobs.csv"):

    with open(path, "r") as file:
        find_jobs = csv.DictReader(file, delimiter=",")
        lista = []
        for job_file in find_jobs:
            lista.append(job_file)
        return lista


read("src/jobs.csv")
