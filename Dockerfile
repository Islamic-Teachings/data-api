FROM python:3.7
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python IslamicApp/manage.py makemigrations
RUN python IslamicApp/manage.py migrate
RUN python IslamicApp/Quran/init_db.py
ENTRYPOINT IslamicApp/manage.py runserver 9000
EXPOSE 9000
