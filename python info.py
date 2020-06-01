============ Командная строка ============
pwd – показать текущую папку
cd .. – возвращает на уровень вверх
ls – выводит содержимое папки 
ls -Al выводит содержимое в подробном формате 
touch - создает файл


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








