# Robot tests for fastApiProject

To create an image of the tests run in the test directory: 

    docker build -t fast-api-robot-tests:1.0 .

To run test on fast-api-app:1.0 container:
    docker run --net fast-api-app-network -v $(pwd)/tests:/usr/fastApiProjectRobotTests/tests -v $(pwd)/../results:/usr/fastApiProjectRobotTests/results fast-api-robot-tests:1.0 robot /usr/fastApiProjectRobotTests/tests

    # robot /usr/fastApiProjectRobotTests/tests