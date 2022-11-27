# Проект Git-Rick
Данный сайт, с помощью вашего url профиля GitHub, получает информацю о вашем профиле и выводит её вместе с персонажем из вселенной Рика и Морти ```^-^```
### Пример работы
![](https://i.postimg.cc/mkbM2HbZ/Screenshot-2022-11-27-at-19-28-28-Git-Rick2.png)
![](https://i.postimg.cc/T17ydN7Q/Screenshot-2022-11-27-at-19-28-02-Git-Rick.png)
### Запуск проекта в dev-режиме:
- Клонируйте репозиторий и перейдите в него
    ```
    $ git clone git@github.com:clownvkkaschenko/Git-Rick.git
    ```
- Установите и активируйте виртуальное окружение
    ```
    $ python -m venv venv
    ```
- Установите зависимости из файла requirements.txt
    ```
    $ pip install -r requirements.txt
    ``` 
- В папке с файлом manage.py выполните миграции, и запустите сервер:
    ```
    $ python manage.py migrate
    ``` 
    ```
    $ python manage.py runserver
    ```
### Используемые технологии:
- [Python 3.7.9](https://www.python.org/)
- [Django 2.2.19](https://www.djangoproject.com/start/overview/)
- [GitHub API](https://docs.github.com/en/rest)
- [The Rick and Morty API](https://rickandmortyapi.com/)
### Автор:
Иван Конышкин
