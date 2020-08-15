\n - перенос строки
\t - добавить табуляцию

============ Командная строка ============
pwd – показать текущую папку
cd .. – возвращает на уровень вверх
ls – выводит содержимое папки 
ls -Al выводит содержимое в подробном формате 
touch - создает файл
-m venv env - создает виртуальное окружение, где env - это название виртуального окружения

============ git ============
1. Создаем отдельную директорию под гит и в ней пишем команду: 
$ git init
2. Для установки git пишем команды 
$ git config —global user.name «your name»
$ git config —global user.email mail@mail.ru

git add -A - добавляет в git все файлы (запоминает)
git commit -m «комментарий» сохраняет файлы (сопровождается комментарием)
git status - проверяет, были ли изменения с последнего изменения
git checkout HEAD - перейти к последней версии кода
.gitignore - файл, в котором перечисляются файлы, не нужные для записи в git 
git log - показывает историю работы с гитом

Добавить репозиторий в github впервые:
git remote add origin https://github.com/isakovs/isakovs.git

Добавить обновления репозитория:
git push -u origin master

ВРОДЕ скинуть все файлы в репозитория в текущую папку: 
git clone git://g...


============ Программы ============
Visual Studio Code
Саблайн


============ Типы данных: ============
- целые числа (integer)
- вещественные числа (float)
- логический тип (bool): true and false строки (string)
- None

============ Подставить переменную в текст ============
1. Способ через плюсы
a = "Привет"
b = 'Мир'
c = a + ' ' + b
print (c)

2. Формиатирование строки
a = "Привет"
b = 'Мир'
с = '{} {}!'.format(a, b)

3. f строки
user = "Python"
c = f'Привет, {user}!'
print(c)

============ Приведение типов данных ============
- int() - приводит к целому числу
- float() - приводит к вещественному числу
- bool() - приводит к логической херне 
- str() - приводит к строке 
- abs() - взвращает значение по модулю
- .upper - приводит всё к заглавным буквам
- .replace('что меняем', 'на что меняем') - замена 

== - равно 
!= или <> - не равно
< - меньше 
> - больше 
<= - меньше или равно
>= - больше или равно


============ Функции ============
len () – выводит длину строки в виде числа символов
.format – прибавляется к строкам, в которых есть переменные {}, чтобы объяснить что откуда брать
.upper - ставится к строке, что сделать ЗАГЛАВНЫЕ буквы
.lower – ставится к строке, чтобы сделать маленькие буквы
.capitalize – делает предложение с большой буквы
.strip() - убирает пробелы в начале и конце
.replace - замена символов
.split (‘.’) - разбивает строку на элементы листа
.append(‘’) - добавляет элемент в лист
.count(‘’) - посчитает, сколько раз в листе встречается значение
.index(‘’) - покажет, какой номер индекса имеет элемент в листе 
.remove (‘’) - удалит первое такое встречающее значение в лист

Функция
- позиционные аргументы
- именованные аргументы (необязательные, со значением по умолчанию)


============ Условный оператор ============
простой оператор
if age < 18:
	print(‘Никаких тебе сигарет!’)
else:
	print(‘Вам синий или красный’)

вызов функции в зависимости от условия
if not is_user_banned
ban_user(user)

последовательно перебирает, где истина и исполняет след. строку
if team == ‘mystic’:
print(‘Hi, blue team’)
elif team == ‘instinct’
print(‘Hi, yellow team’)
elif team == ‘valor’
print(‘Hi, red team’)



============ Циклы ============
Цикл for
выполняет тело цикла с каждым элементом списка, который дали на вход. 

students_scores = [1, 21, 19, 6, 5]
for score in students_scores:
	print (score)

здесь print (score) – тело 


Цикл while 
выполняет тело цикла пока выполняется условие

while True:
	user_say = input('Скажи что-нибудь')
	if user_say == 'Пока':
		print('Ну пока')
		break
	else:
		print('Сам ты {}'.format(user_say))


Цикл try/except
def cut_cake(parts):
	try:
		return 1 / int(parts)
	except (ZeroDivisionError, TypeError, ValueError):
		return 'Вы что, с ума посходили?'

cake = cut_cake(0)
print(cake)



============ Solve problems ============
>>> Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: 

<<< You are trying to install the package to a system folder which you don't have permissions to write to.
You have three options(use only one of them):
1-setup a virtual env to install the package (recommended):

python3 -m venv env
source ./env/bin/activate 
python -m pip install google-assistant-sdk[samples]
2-Install the package to the user folder:
python -m pip install --user google-assistant-sdk[samples]

3-use sudo to install to the system folder (not recommended)
sudo python -m pip install google-assistant-sdk[samples]


============ Работа с файлами ============
with open('myfole.txt'. 'w', encoding='utf-8') as myfile:
	myfile.write('Всем привет!')
'''
with - вроде чтобы не нужно было закрывать файл
'w' или 'r' - записывать или читать
'a' - не перезаписывать, а заносить в конец
'''

with open('myfole.txt'. 'r', encoding='utf-8') as myfile:
	text = myfile.read()
	print(text)
'''
текст распечатается, но это плохой вариант, потому что занимает много памяти. Лучше печатать построчно 
'''

with open('myfole.txt'. 'r', encoding='utf-8') as f:
	for line in f:
		line = line.apper()
		print(linr)



============ Useful modules ============
########################################
########################################
# datetime - работа с датой и временем
########################################
Компоненты: 
date - 
time - 
datetime - дата/время
timedelta - разница между моментами времени
tzinfo - часовые пояса и летнее время

# пример
from datetime import datetime
dt_now = datetime.now()
dt_now 

datetime.datetime(2020, 6, 7, 19, 6, 40484)

#задаем дату или время
dt = date(2020, 6, 14)
dtt = datetime(2020, 6, 14, 23, 43, 17, 40486)

# задаем переменную в виде разницы во времени
delta = timedelta(days=1) # timedelta это готовый модуль. Теперь переменную delta можно использовать

# мы можем создавать дату
dt2 = datetime(2020, 5, 16, 8, 4, 44)
dt2
datetime.datetime(2020, 5, 16, 8, 3, 44)

# разница между датами
delta = dt_now - dt2
delta

datetime.timedelta(504, 11663, 4738474)
	#здесь дни, секунды, милисекунды

#вывод даты на экран
from datetime import datetime
dt_now = datetime.now()
dt_now.strftime('%d.%m.%Y %H:%M')

'01.10.2020 11:10'

# для локализации написания даты и времени под русский язык используется модуль locale
import locale 
locale.setlocale(locale.LC_ALL, "russian")
dt_now.strftime('%A %d %B %Y')

'суббота 01 октября 2020'

#получение даты из строки
date_string = '12/23/2020'
date_dt = datetime.strptime(date_string, '%m/%d/%Y')
date_dt

datetime.datetime(2020, 12, 23, 0, 0)

########################################
########################################
# csv - запись и чтение csv файлов
########################################
import csv 
with open('users.csv', 'r', encoding='utf-8') as f:
	fields = ['first_name', 'last_name', 'email', 'gender', 'balance'] #объявляем поля, чтобы вывести их на печать в словари
	reader = csv.DictReader(f, fields, delimiter=';') #из модуля вызываем функцию и ей обозначаем (переменную с таблицей, поля для обозначения столбцов, разделитель)
	for row in reader:
		print(row)

#для записи данных в csv нужно иметь их в списке словарей в коде
with open('export.csv', 'w', encoding='utf-8') as f: #здесь уже стоит 'w'
	fields = ['first_name', 'last_name', 'email', 'gender', 'balance'] #объявляем, как будут называться столбцы
	writer = csv.DictWriter(f, fields, delimiter=';') #из модуля вызываем функцию и ей обозначаем (переменную с таблицей, поля для обозначения столбцов, разделитель)
	for row in reader:
		print(row)


============ Объекты ============

class Point: #class описывает объект
	x = 0
	y = 0

	def coordinates(self) # функция внутри клаccа называется методом. У методов всегдам первым идет параметр self 
		print(f'Координаты: x {self.x}, y {self.y}')

my_point = Point() # создаем экземпляр класса

my_point.coordinates # выполнится функция, то есть распечатаются координаты в тексте

my_point.x = 10
my_point.y = -5

my_point.coordinates # распечает точку с новыми координатами

# =================

class Point: 
	def __init__(self, x, y): # __init__ для случаев, когда заранее значения параметров не задаются, а здаются только переменные. Дальше при использовании объекта нужно задать переменные
		self.x = x
		self.y = y

	def coordinates(self): # функция внутри клаccа называется методом. У методов всегдам первым идет параметр self 
		print(f'Координаты: x {self.x}, y {self.y}')

my_point = Point(1, 3) # теперь в Point нужно задавать конкретные координаты переменных, потому без этого нихуя не получится

my_point.coordinates 

my_point.x = 10
my_point.y = -5

my_point.coordinates 

# =================  если просто распечатать класс
print(my_point) # получим кракозябры:

<__main__.Point object at 0x00F381F0>

# а если в Point добавим метод:
def __repr__ (self):
	return f'Point x: {self.x}, y: {self.y}'

# тогда возвращается текст: 
Point x: 10, y: -5