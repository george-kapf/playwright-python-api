# Prerequisites:

1. Docker Desktop installed & running on your machine

# Steps to run tests:

To execute the tests and publish an HTML report that you can view on your machine, you can follow these steps:

1. Make sure you have Docker installed on your machine.

2. Create a new directory and place the `Dockerfile` and `playwright_script.py` files inside it.

3. Open a terminal or command prompt and navigate to the directory where the files are located.

4. Build the Docker image using the following command:
   `docker build -t test-framework .`
   This command will build the Docker image using the `Dockerfile` and tag it as `test-framework`.

5. Run the Docker container and execute the tests using the following command:
   `docker run -it --rm -v $(pwd):/usr/src/app test-framework`
   This command will run the Docker container, mount the current directory as a volume inside the container, and execute the tests.

6. After the tests are executed, an HTML report named `report.html` will be generated in the current directory.

7. You can open the HTML report in your preferred web browser to view the test results.
