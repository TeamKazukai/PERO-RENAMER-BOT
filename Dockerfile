FROM python:3.10
WORKDIR /app
COPY . /app/
RUN apt update && apt upgrade -y
RUN apt install git python3-pip ffmpeg -y
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]
