package main

import (
	v0 "niyazgim/backend-template/gin-gonic-example/controllers/v0"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	r.GET("/hello", v0.SayHello)

	r.Run(":8080")
}
