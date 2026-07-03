# ===============================
# base
# ===============================
FROM python:3.12-slim-bookworm AS base
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONOPTIMIZE=2

# ===============================
# builder
# ===============================
FROM base AS builder
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ===============================
# dev
# ===============================
FROM base AS dev
COPY --from=builder /install /usr/local
COPY . .
EXPOSE 8000
CMD ["granian", "--interface", "asgi", "--host", "0.0.0.0", "--port", "8000", "--reload", "main:app"]

# ===============================
# prod
# ===============================
FROM base AS prod
COPY --from=builder /install /usr/local
COPY . .
EXPOSE 8000
CMD ["granian", "--interface", "asgi", "--host", "0.0.0.0", "--port", "8000", "--threads", "2", "--loop", "uvloop", "main:app"]