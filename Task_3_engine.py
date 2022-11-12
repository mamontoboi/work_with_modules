from random import randint


def inquire():
    qnt = int(input('How many numbers do you want to get? \n'))
    return qnt


def prime_gen():
    yield randint(2, 99)


x = 'hello stupid world'
