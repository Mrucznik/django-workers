from random import random

from workers import task


@task()
def say_hello(name):
    print('Howdy', name)


@task(schedule=10)
def do_something():
    print('I run every 10 seconds')


@task(schedule=60 * 5)
def do_something_later():
    print('I run every 5 minutes')


@task(schedule=60 * 60 * 8)
def do_something_even_later():
    print('I run every 8 hours')


@task(schedule=10)
def task_with_result():
    sample_result = {
        'name': 'sample result',
        'value': random()
    }
    print(f'I run every 10 seconds and with result: {sample_result}')
    return sample_result
