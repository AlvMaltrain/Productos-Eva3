# Etapa 1: Builder
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

#Etapa 2: Runtime
FROM python:3.12-slim
RUN useradd --create-home appuser
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app.py wsgi.py ./
ENV PYTHONUNBUFFERED=1 \
    PORT=8082
EXPOSE 8082
USER appuser

#Preload: corre wsgi.py (espera DB + init_db) una sola vez antes de forkear
CMD ["gunicorn", "--preload", "-w", "2", "-b", "0.0.0.0:8082", "wsgi:app"]