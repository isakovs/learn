import random 
from datetime import date, time, datetime, timedelta

b = {'DS100': '250',
     'DS400': '400',
     'DH60': '200',
     'DH250': '350'}

start_time = datetime.now()
result = {} # в этот словарь записываются пары вопрос:правильно или вопрос:неправильно

def get_pair():
    pair = random.choice(list(b.items()))
    question = pair[0]
    tru_answer = pair[1]
    answer = input(f'Напиши цену {question} ')
    if answer == tru_answer:
        print('правильно')
        result[f'{question}'] = 'правильно'
        get_pair()

    elif answer == 'стоп':
        finish_time = datetime.now()
        delta_time = finish_time - start_time
        #str_delta_time = str(delta_time) не знаю, как перевести delta_time в читаемый вид
        #user_test_time = time.strptime(str_delta_time, '%H:%M:%S.%f')
        print(f"Баста! Ты тренировался {delta_time}.\nРезультаты вот:\n{result}")

    else:
        print('неправильно')
        result[f'{question}'] = 'неправильно'
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