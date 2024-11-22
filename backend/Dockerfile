FROM python:3.12-slim as PYTHON_IMAGE

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /jaknajtaniej/backend

COPY requirements.txt /jaknajtaniej/backend
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /jaknajtaniej/backend

RUN chmod +x /jaknajtaniej/backend/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]