package helpers

import (
	"database/sql"
	"errors"
	"fmt"
	"log"
	"os"

	_ "github.com/lib/pq"
)

func Connect() (*sql.DB, error) {
	dbDriver := os.Getenv("DB_DRIVER")
	if dbDriver == "" {
		return nil, errors.New("DB_DRIVER not set")
	}

	DB, err := sql.Open(dbDriver, GetConnectionString())
	if err != nil {
		return nil, fmt.Errorf("open db: %w", err)
	}

	if err := DB.Ping(); err != nil {
		DB.Close()
		return nil, fmt.Errorf("ping db: %w", err)
	}

	log.Println("[log] Connected to the db successfully")
	return DB, nil
}

func Close(DB *sql.DB) {
	err := DB.Close()
	if err != nil {
		log.Println("[error] db closing: %w", err)
		return
	}
	log.Println("[log] Closed db connection successfully")
}

func GetConnectionString() string {
	host := os.Getenv("DB_HOST")
	port := os.Getenv("DB_PORT")
	dbName := os.Getenv("DB_NAME")
	username := os.Getenv("DB_LOGIN")
	password := os.Getenv("DB_PASSWORD")
	SSLMode := os.Getenv("DB_SSLMODE")

	return fmt.Sprintf(
		"host=%s port=%s user=%s password=%s dbname=%s sslmode=%s",
		host,
		port,
		username,
		password,
		dbName,
		SSLMode)
}
