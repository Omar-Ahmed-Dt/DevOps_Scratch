FROM node
WORKDIR /app
COPY package.json . 
#RUN npm install
RUN npm install
COPY . .
EXPOSE 4000
#CMD [ "npm","start" ]
CMD [ "npm", "run", "start-dev" ]
