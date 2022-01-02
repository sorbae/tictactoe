# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /client
EXPOSE 5000
COPY . .
CMD ["npm", "install", "npm", "run", "build"]