FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN pip install flask pymongo
COPY . .
CMD ["flask","run","--host","0.0.0.0"]



# docker build -t flask-app .
# docker run -p 5005:5000 flask-app  ---> run docker container
#docker run -dp 5005:5000 flask-app   ---> run docker container in backround
#docker-compose up -d ----> run flask and mongo in backround
#docker-compose up   -----> run flask and mongo


