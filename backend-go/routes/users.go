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
	r.GET("/users/:id", handleGetUser)
	r.GET("/users", handleGetUsers)
	r.POST("/users", handlePostUser)
	r.PUT("/users/:id", handlePutUser)
	r.DELETE("/users/:id", handleDeleteUser)
}

func handleGetUser(c *gin.Context) {
	c.JSON(http.StatusOK, users)
}

func handleGetUsers(c *gin.Context) {
	c.JSON(http.StatusOK, users)
}

func handlePostUser(c *gin.Context) {
	c.JSON(http.StatusOK, users)
}

func handlePutUser(c *gin.Context) {
	c.JSON(http.StatusOK, users)
}

func handleDeleteUser(c *gin.Context) {
	c.JSON(http.StatusOK, users)
}
