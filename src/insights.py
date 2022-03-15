from src.jobs import read


def get_unique_job_types(path):
    all_jobs_type = read(path)
    lista = []
    for types in all_jobs_type:
        if types["job_type"] not in lista:
            lista.append(types["job_type"])
    return lista


def filter_by_job_type(jobs, job_type):
    return_all_jobs = []
    for name_job in jobs:
        if name_job["job_type"] == job_type:
            return_all_jobs.append(name_job)
    return return_all_jobs


def get_unique_industries(path):
    all_industries = read(path)
    lista = []
    for industry in all_industries:
        if industry["industry"] not in lista and len(industry["industry"]) > 0:
            lista.append(industry["industry"])
    return lista


def filter_by_industry(jobs, industry):
    return_all_indutries = []
    for name_industry in jobs:
        if name_industry["industry"] == industry:
            return_all_indutries.append(name_industry)
    return return_all_indutries


def get_max_salary(path):
    get_all_max_salary = read(path)
    lista = []
    for max_length in get_all_max_salary:
        if max_length["max_salary"].isnumeric():
            lista.append(int(max_length["max_salary"]))
    return max(lista)


print(get_max_salary("src/jobs.csv"))


def get_min_salary(path):
    get_all_min_salary = read(path)
    lista = []
    for min_length in get_all_min_salary:
        if min_length["min_salary"].isnumeric():
            lista.append(int(min_length["min_salary"]))
    return min(lista)


print(get_min_salary("src/jobs.csv"))


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary or max_salary is missing")
    if (
        not isinstance(job["min_salary"], int) or
        not isinstance(job["max_salary"], int)
    ):
        raise ValueError("min_salary and max_salary must be valid integers")
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("min salary is greater than max_salary")
    if not isinstance(salary, int):
        raise ValueError("salary must be valid integer")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filter_salary = []
    for job in jobs:
        try:
            matches_salary_range(job, salary)
        except ValueError:
            pass
        else:
            if matches_salary_range(job, salary):
                filter_salary.append(job)
    return filter_salary
