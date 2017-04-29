package main

import (
    "os"
    "fmt"
    "net/http"
    "math/rand"
    "time"
)

func hiHandler(writer http.ResponseWriter, request *http.Request) {
    time.Sleep(time.Duration(rand.Int31n(10000)) * time.Millisecond)
    fmt.Fprint(writer, "Hi!\n")
}

func main() {
    http.HandleFunc("/", hiHandler)
    http.ListenAndServe(":" + os.Args[1], nil)
}
