import random 

b = {'DS100': '250',
	 'DS400': '400',
	 'DH60': '200',
	 'DH250': '350'}

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