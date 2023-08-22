# fast Api Server

From the root directory of the repository run the following commands:
    To create a docker image of the server run in the directory fastApiProject: 
                docker build -t fast-api-app:1.0 .
    Next, to run created image in a docker container run command: 
                docker run -d -p 8000:8000 --name server fast-api-app:1.0
    Access server from localhost:8000 and the swagger docs from http://localhost:8000/docs

To run server locally from the root directory:
    - python main.py 
    - or uvicorn.run(app, host="0.0.0.0", port=8000)

To run with different ports:
    - In HostAndPort.py you can add your port and host of preference
    - Or set HOST and PORT environment variables and run python main.py
    
