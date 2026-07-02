# ===============================
# Base
# ===============================
FROM golang:1.25-alpine AS base

WORKDIR /app
RUN apk add --no-cache git

# ===============================
# Dev (hot reload with air)
# ===============================
FROM base AS dev

RUN go install github.com/air-verse/air@latest

CMD ["air"]

# ===============================
# Build
# ===============================
FROM base AS builder

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o gin-gonic-example

# ===============================
# Prod
# ===============================
FROM alpine:3.20 AS prod

WORKDIR /app
RUN apk add --no-cache ca-certificates

COPY --from=builder /app/gin-gonic-example /app/gin-gonic-example

EXPOSE 8080
CMD ["./gin-gonic-example"]