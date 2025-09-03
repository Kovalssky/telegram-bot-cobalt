FROM python:3.12-slim

WORKDIR /app


RUN apt update -y && apt install -y git && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "bot"]
