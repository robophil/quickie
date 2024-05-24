package routes

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type User struct {
	Id   string `json:"id"`
	Name string `json:"name"`
}

var users []User

func init() {
	users = []User{
		{"1", "John Doe"},
		{"2", "Paul Doe"},
		{"3", "Jane Doe"},
	}
}

func AddUsersRoutes(r *gin.RouterGroup) {
	r.GET("/users", handleGetUsers)
	r.GET("/users/:id", handleGetUsers)
	r.POST("/users", handleGetUsers)
	r.PUT("/users/:id", handleGetUsers)
	r.DELETE("/users/:id", handleGetUsers)
}

func handleGetUsers(c *gin.Context) {
	c.JSON(http.StatusOK, users)
}
