FROM python:3.7.9-slim
COPY . /app
WORKDIR /app
ENV DEBIAN_FRONTEND noninteractive
RUN apt update -y
RUN apt install libgl1-mesa-glx libglib2.0-0 -y
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "runner.py"]
