import numpy as np
from mongo_setup import setup_mongo

def calculate_average_salary():
    collection = setup_mongo()
    salaries = [float(job['salary'].replace('$', '').replace(',', '')) for job in collection.find()]
    average_salary = np.mean(salaries)
    return average_salary
