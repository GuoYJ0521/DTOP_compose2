FROM python:3.9-slim

WORKDIR /flask
COPY . /flask/
# RUN pip install flask
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["python3", "run.py"]