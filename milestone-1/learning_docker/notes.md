# Docker Notes

## What is Docker?

Docker is a platform for developing, shipping, and running applications inside lightweight, portable containers. Containers package an application and its dependencies into a standardized unit that can run consistently across different environments.

## Why Use Docker?

- **Consistency**: Applications run the same way in development, testing, and production
- **Isolation**: Containers isolate applications from each other and the host system
- **Portability**: Containers can run on any system that supports Docker
- **Efficiency**: Containers share the host OS kernel, making them lightweight compared to virtual machines
- **Scalability**: Easy to scale applications horizontally
- **Version Control**: Docker images can be versioned and stored in registries

## Core Concepts

### Images

- Read-only templates used to create containers
- Built from Dockerfiles
- Stored in registries like Docker Hub

### Containers

- Running instances of images
- Isolated environments with their own filesystem, network, and process space
- Can be started, stopped, paused, and deleted

### Dockerfile

- Text file containing instructions to build a Docker image
- Defines the base image, dependencies, and commands to run

### Docker Compose

- Tool for defining and running multi-container Docker applications
- Uses YAML files to configure services, networks, and volumes

## Basic Docker Commands

### Image Commands

```bash
# List images
docker images

# Pull an image from registry
docker pull <image_name>:<tag>

# Build an image from Dockerfile
docker build -t <image_name>:<tag> <path>

# Remove an image
docker rmi <image_id>

# Search for images
docker search <term>
```

### Container Commands

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Run a container
docker run <image_name>

# Run a container in background
docker run -d <image_name>

# Run with port mapping
docker run -p <host_port>:<container_port> <image_name>

# Run with volume mounting
docker run -v <host_path>:<container_path> <image_name>

# Stop a container
docker stop <container_id>

# Start a stopped container
docker start <container_id>

# Remove a container
docker rm <container_id>

# Execute commands in running container
docker exec -it <container_id> <command>

# View container logs
docker logs <container_id>

# View container details
docker inspect <container_id>
```

### System Commands

```bash
# Show Docker system information
docker info

# Show disk usage
docker system df

# Clean up unused resources
docker system prune

# Clean up everything
docker system prune -a --volumes
```

## Dockerfile Instructions

### FROM

Sets the base image for the Docker image.

```dockerfile
FROM python:3.10-slim
```

### WORKDIR

Sets the working directory inside the container.

```dockerfile
WORKDIR /app
```

### COPY

Copies files from host to container.

```dockerfile
COPY . /app
```

### ADD

Similar to COPY but can handle URLs and tar files.

```dockerfile
ADD source destination
```

### RUN

Executes commands during image build.

```dockerfile
RUN pip install -r requirements.txt
```

### CMD

Specifies the default command to run when container starts.

```dockerfile
CMD ["python", "app.py"]
```

### ENTRYPOINT

Similar to CMD but allows arguments to be passed.

```dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]
```

### ENV

Sets environment variables.

```dockerfile
ENV PORT=8000
```

### EXPOSE

Documents which ports the container listens on.

```dockerfile
EXPOSE 8000
```

### VOLUME

Creates a mount point for external volumes.

```dockerfile
VOLUME ["/data"]
```

### USER

Sets the user to run subsequent commands.

```dockerfile
USER appuser
```

## Docker Compose

### Basic Structure

```yaml
version: "3.8"
services:
  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: password
```

### Common Commands

```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# Stop services
docker-compose down

# Build images
docker-compose build

# View logs
docker-compose logs

# Execute commands in service
docker-compose exec <service> <command>

# Scale services
docker-compose up -d --scale <service>=<count>
```

## Mini-Project Example

This project demonstrates a FastAPI application with PostgreSQL database using Docker Compose.

### Project Structure

```
mini-project/
├── docker-compose.yml    # Orchestrates services
├── Dockerfile           # Builds the FastAPI app image
├── app/                 # Application code
│   ├── main.py         # FastAPI application
│   ├── db.py           # Database configuration
│   ├── requirements.txt # Python dependencies
│   └── models/         # SQLAlchemy models
└── db/                  # Database initialization
    └── script.sql      # Database schema and data
```

### Dockerfile Analysis

```dockerfile
FROM python:3.10-slim    # Base image
WORKDIR /app             # Working directory
COPY /app /app          # Copy application code
RUN pip install -r requirements.txt  # Install dependencies
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]  # Run command
```

### Docker Compose Analysis

- **postgres-db service**: Runs PostgreSQL 13 with custom database, user, and password
- **app service**: Builds from local Dockerfile, depends on database
- **Networks**: Both services connected to test-network for communication
- **Volumes**: Persistent data storage for database and initialization script

### Running the Project

```bash
# Build and start services
docker-compose up --build

# Access the API at http://localhost:8000
# Database available at localhost:5432
```
