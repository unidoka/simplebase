package helpers

import (
	"log"
	"os"
	"time"

	"github.com/golang-jwt/jwt/v5"
	"github.com/joho/godotenv"
)

var (
	jwtSecret []byte
)

func init() {
	if err := godotenv.Load(); err != nil {
		log.Println("No .env file found, reading from system env")
	}

	jwtSecret = []byte(os.Getenv("JWT_SECRET_KEY"))
}

func GetJWTSecret() []byte {
	return jwtSecret
}

func GenerateToken(userID int64, phone string) (string, error) {
	t := jwt.NewWithClaims(
		jwt.SigningMethodHS256,
		jwt.MapClaims{
			"user_id": userID,
			"phone":   phone,
			"exp":     time.Now().Add(72 * time.Hour).Unix(),
		})
	return t.SignedString(jwtSecret)
}
