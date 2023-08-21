# fast Api Server

From the root directory of the repository run the following commands:
    To create a docker image of the server run in the directory fastApiProject: 
                docker build -t fast-api-app:1.0 .
    Next, to run created image in a docker container run command: 
                docker run -d -p 8000:8000 --name server fast-api-app:1.0
    Access server from localhost:8000 and the swagger docs from http://localhost:8000/docs
