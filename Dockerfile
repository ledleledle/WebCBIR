FROM python:3.7.9-slim
WORKDIR /app
COPY requirements.txt /app
ENV DEBIAN_FRONTEND noninteractive
RUN apt update -y
RUN apt install libgl1-mesa-glx libglib2.0-0 -y
RUN pip install -r requirements.txt
CMD ["python3", "runner.py"]
