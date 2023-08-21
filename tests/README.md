# Robot tests for fastApiProject
On PowerShell (ensure to run 'deactive' in case you are in the python virtual environment )

To create an image of the tests run in the test directory (/tests): 

    docker build -t fast-api-robot-tests:1.0 .

To run test on server container (fast-api-app:1.0) from the test directory (/tests) run the below:
    docker run -d --net=host -v ${PWD}/../results/:/usr/results fast-api-robot-tests:1.0  robot -d /usr/results .


# --add-host=host.docker.internal:host-gateway

# -v $(pwd)/tests:/usr/fastApiProjectRobotTests

# nc -lp 8000  the server should be listening //this is not eh test machine 

# nc fast-api-server 8000

#  robot -d ${PWD}/../results .