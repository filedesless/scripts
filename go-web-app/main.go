package main

import (
	"io"
	"net/http"
)

func indexHandler(res http.ResponseWriter, req *http.Request) {
	io.WriteString(res, "Hello world!")
}

func main() {
	http.HandleFunc("/index", indexHandler)
	http.ListenAndServe(":8080", nil)
}
