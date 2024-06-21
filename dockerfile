FROM python:3.11-slim

# Copy the requirements.txt file into the container
COPY requirements.txt /src/requirements.txt

# Set the working directory to /src
WORKDIR /src

# Install the required Python packages
RUN pip3 install -r requirements.txt

# Create a non-root user and application directory
RUN groupadd -r demouser && useradd -r -g demouser demouser && \
    chown -R demouser:demouser /src

# Switch to the non-root user
USER demouser

# Copy the application code to the /src directory
COPY app.py /src/app.py

# Set environment variables
ENV FLASK_APP=app.py \
    REDIS_HOST=redis \
    FLASK_RUN_PORT=8000

# Expose port 8000 to match the port mapping in docker-compose.yml
EXPOSE 8000

# Run Flask application
CMD ["flask", "run", "-h", "0.0.0.0"]
