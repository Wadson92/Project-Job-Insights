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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
