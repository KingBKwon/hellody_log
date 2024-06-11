FROM --platform=linux/amd64 python:3.10-slim as build

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
	        && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src
COPY requirements.txt ./
RUN pip install -r requirements.txt 
COPY . .

EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
