FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt
RUN mkdir ~/.bootcamp && cp config.toml ~/.bootcamp/config.toml && cp credentials.toml ~/.bootcamp/credentials.toml

EXPOSE 80
WORKDIR /app
ENTRYPOINT ["bootcamp","run"]
CMD [ "app.py" ]