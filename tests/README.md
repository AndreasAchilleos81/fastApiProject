# Robot tests for fastApiProject
From, PowerShell (ensure to run 'deactive' in case you are in the python virtual environment) and in the folder /tests run the following commands:
    To create an image of the tests run in the : 
            docker build -t fast-api-robot-tests:1.0 .
    To run the test on a docker container run:
            docker run -d --net=host -v ${PWD}/../results/:/usr/results fast-api-robot-tests:1.0  robot -d /usr/results .

The results of the tests will be created on directory above the tests folder under the results folder.

        
