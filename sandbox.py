import random 
from datetime import datetime, timedelta

b = {'DS100': '250',
     'DS400': '400',
     'DH60': '200',
     'DH250': '350'}

def get_pair():
    pair = random.choice(list(b.items()))
    question = pair[0]
    tru_answer = pair[1]
    answer = input(f'Напиши цену {question} ')
    result = {} # в этот словарь предполагается записывать пары вопрос:правильно или вопрос:неправильно
    start_time = datetime.now()
    if answer == tru_answer:
        print('правильно')
        result[answer] = 'правильно'
        get_pair()

    elif answer == 'стоп':
        finish_time = datetime.now()
        delta_time = finish_time - start_time
        print(f"Баста! Ты тренировался c {start_time} по {finish_time}")

    else:
        print('неправильно')
        result[answer] = 'неправильно'
        get_pair()
        
        
result = get_pair()





'''
def get_pair():
    pair = random.choice(list(b.items()))
    question = pair[0]
    tru_answer = pair[1]
    answer = input(f'Напиши цену {question} ')
    if answer == tru_answer:
        print('правильно')
        get_pair()
    else:
        print('неправильно')
        get_pair()
        

result = get_pair()
'''