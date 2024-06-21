# HitCounter

HitCounter is a Dockerized Python Flask application integrated with Redis, designed to track and display the number of times a webpage has been visited. It demonstrates containerization for easy deployment and uses Redis as an efficient in-memory database for storing visit counts.

## Features

- Tracks and displays the number of times a webpage has been visited.
- Uses Redis as an efficient in-memory database for storing visit counts.
- Containerized application for consistent deployment across different environments.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)

## Getting Started

Follow these instructions to get the HitCounter application up and running on your local machine.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AdityaJain2162/hitcounter/
   cd hitcounter
   ```

2. **Build and start the Docker containers:**

   ```bash
   docker-compose up --build
   ```

   This command builds the Docker images and starts the containers for the Flask web application and Redis database.

3. **Access the HitCounter application:**

   Open your web browser and go to `http://localhost:8000`. You should see a simple webpage served by Flask displaying the number of visits.

4. **Stop the containers:**

   To stop the containers and remove the network, use:

   ```bash
   docker-compose down
   ```

## Project Structure

The project structure is as follows:

- **app.py**: Flask application file that defines routes and interacts with Redis.
- **requirements.txt**: Lists the Python packages required for the application.
- **Dockerfile**: Specifies instructions for building the Docker image for the Flask application.
- **docker-compose.yml**: Defines the services (Flask and Redis) and their configuration using Docker Compose.
- **README.md**: This file, providing instructions on setting up and running the application.

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## Contact

For questions or feedback, contact [Aditya Jain](jaditya700@gmail.com).