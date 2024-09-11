FROM python:3.12.6-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
 
RUN python3 -m pip install -r requirements.txt

COPY app.py app.py

CMD ["python","app.py"]