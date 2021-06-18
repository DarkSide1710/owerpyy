FROM python:3.9.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/owerpy/Docker/survey_owerpy/owerpyy/

COPY ./requirements.txt /home/owerpy/Docker/survey_owerpy/owerpyy/requirements.txt
RUN pip install -r /home/owerpy/Docker/survey_owerpy/owerpyy/requirements.txt

COPY . /home/owerpy/Docker/survey_owerpy/owerpyy/

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["python","manage.py", "migrate"]
