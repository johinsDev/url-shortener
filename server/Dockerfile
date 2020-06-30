FROM python:3

WORKDIR /app/server

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "server.py"]
