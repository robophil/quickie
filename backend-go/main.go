package main

import (
	"github.com/gin-gonic/gin"
	"github.com/robophil/quickie/routes"
)

func main() {
	r := gin.Default()
	routeGroup := r.Group("/api")

	// add user routes
	routes.AddUsersRoutes(routeGroup)

	r.Run(":8080") // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
