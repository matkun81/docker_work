Docker task
Данный проект запускает три теста, которые подымают ОС ubuntu в docker and virtual box и пытается получить ip адреса

Для того чтобы запустить данный проет необходимо его скачать
и выполнить следующие команды: 

pip install -r requirements.txt
pytest -v -s --alluredir=report

Окружение: необходим установленный python. 

В данном проекте используется python 3.8