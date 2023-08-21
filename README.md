# fastApiProject

First: create a network to attached to the container once it starts running
    docker network create fast-api-app-network

To create an image of the server run in the directory fastApiProject: 
            docker build -t fast-api-app:1.0 .

To run image in a docker container run command: 
            docker run -d --net fast-api-app-network -p 8000:8000 fast-api-app:1.0
