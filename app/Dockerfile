FROM python:latest

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD . /code

WORKDIR /code

CMD ["python","-m", "unittest", "discover"]