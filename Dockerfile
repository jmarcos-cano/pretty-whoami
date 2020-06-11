FROM python:3.7-alpine
WORKDIR /app

ENV DEBUG=False

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY . ./
ENTRYPOINT [ "python" ]
CMD [ "server.py"]


EXPOSE 5000