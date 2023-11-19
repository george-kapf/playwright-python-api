# Use an official Playwright image as the base image
FROM mcr.microsoft.com/playwright/python:v1.21.0-focal


# Set the working directory
WORKDIR /usr/src/app

# Install Python and required dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# # Install Playwright for Python
# RUN python3 -m pip install playwright

# # # Install pytest-playwright
# # RUN python3 -m pip3 install pytest-playwright
RUN python3 -m pip install pytest pytest-html

# Copy the test script and sample data into the container
COPY . .
# Install any additional dependencies or setup steps if needed
# For example, you may need to install additional Python dependencies, etc.

# Run the Playwright script
CMD ["pytest", "-v", "--html=report.html", "playwright_script.py"]
