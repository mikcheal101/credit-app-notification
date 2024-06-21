FROM python:3.8-alpine

WORKDIR /dist

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run", "--debug"]