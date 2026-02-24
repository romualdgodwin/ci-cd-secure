FROM python:3.11.14-alpine3.23

WORKDIR /app

# Mettre à jour Alpine et openssl
RUN apk update && apk upgrade --no-cache \
    && apk add --no-cache openssl bash

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3000
CMD ["python", "app.py"]