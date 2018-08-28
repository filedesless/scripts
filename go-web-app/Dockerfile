FROM golang:1.5.3

COPY . /go/src/github.com/filedesless/scripts/go-web-app

RUN go install github.com/filedesless/scripts/go-web-app

ENTRYPOINT /go/bin/go-web-app

EXPOSE 8080
