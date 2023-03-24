FROM python:3.7
WORKDIR /Project/tfidf_cooperate

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

ENV LANG C.UTF-8

CMD ["gunicorn", "tf_idf:app", "-c", "./gunicorn.conf.py"]
