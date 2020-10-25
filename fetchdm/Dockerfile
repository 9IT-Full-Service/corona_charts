FROM alpine

RUN apk update && apk add curl jq
RUN mkdir /app
# WORKDIR /app
COPY fetch.sh /app/fetch.sh

CMD ["/app/fetch.sh"]
