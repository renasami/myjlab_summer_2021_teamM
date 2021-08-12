FROM python:3.8-alpine

WORKDIR /myjlab_summer_2021_teamM

COPY requirements.txt .
# コンテナ内で必要なパッケージをインストール


COPY ./docker/api/requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
# FastAPIを8000ポートで待機
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]