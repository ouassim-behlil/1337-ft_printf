FROM debian:stable

RUN apt-get update && apt-get install -y build-essential
RUN apt-get install -y git valgrind
RUN rm -rf /var/lib/apt/lists/*

ENV TERM=xterm-256color

WORKDIR /app

COPY .	.

CMD ["sh", "-c", "cd printfTester && make"]