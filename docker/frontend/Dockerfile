FROM node:alpine

WORKDIR /apps/frontend

COPY ./apps/frontend/ .

RUN npm install

RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "deploy"]