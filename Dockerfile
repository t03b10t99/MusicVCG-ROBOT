FROM debian:latest

RUN apt update && apt upgrade -y
# Install Python 3.9 in Debian
RUN apt install wget build-essential libreadline-gplv2-dev libncursesw5-dev \
      libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev -y

RUN wget https://www.python.org/ftp/python/3.9.4/Python-3.9.4.tgz
RUN tar xzf Python-3.9.4.tgz
RUN cd Python-3.9.4 \
    && ./configure --enable-optimizations

RUN python -m pip install pytgcalls ffmpeg-python psutil
RUN curl -sL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip3 install -U -r requirements.txt
RUN apt update && apt upgrade -y
CMD python3 main.py
