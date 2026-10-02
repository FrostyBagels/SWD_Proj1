FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app/src

EXPOSE 5001

CMD ["python", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0", "--port=5001"]