# Use a base image with Python
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy all the project files to the container
COPY . .

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port where Flask will run
EXPOSE 5001

# Command to run the application correctly
CMD ["python", "-m", "src.app"]