FROM python:3.7

WORKDIR /usr/src/app

# Install Chrome and ChromeDriver
RUN apt-get update && apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable

COPY requirements.txt ./
RUN apt-get update && apt-get install -y python3-pip
RUN pip install -r requirements.txt

#COPY volvo-assestment/* ./
COPY ./* ./