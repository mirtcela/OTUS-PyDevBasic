#Установка ядра системы в контейнер
FROM python:3.9.6-buster
#Выбор рабочей директории
WORKDIR /app
#Установка pip
RUN pip install -U pip setuptools
#Копирование записимостей из проекта
COPY requirements.txt .
#Запуск зависимостей через pip для их настройки в контейнере
RUN pip install -r requirements.txt
#Копирование репозитория с приложением на Flask
COPY ./homework_04 .
#Копирование баш-скрипта для запуска и настройки PATH в контейнере
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
#Настройка окружения при запуске Flask
#Текущие параметры:debug development
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
#Запуск баш-скрипта
ENTRYPOINT ["./entrypoint.sh"]
#Запуск Flask-приложения с определенным хостом
CMD ["flask", "run", "--host=0.0.0.0"]