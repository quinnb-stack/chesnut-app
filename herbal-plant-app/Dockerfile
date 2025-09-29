FROM node:22-alpine

WORKDIR /app

ENV CYPRESS_INSTALL_BINARY=0

COPY ./app/package*.json ./

RUN npm install

COPY ./app ./

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]