FROM paddlecloud/paddlenlp:develop-cpu-b33ead

WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt -i https://mirror.baidu.com/pypi/simple

EXPOSE 5000
COPY . .
CMD ["python", "app.py"]
