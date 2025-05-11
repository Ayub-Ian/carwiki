# Carwiki Auction Service

A Spring Boot application for managing auctions. This project supports both local development and containerized deployment.

## Prerequisites
For Local Development

- Java 21: Install OpenJDK 21.
- Maven: Install Maven (e.g., brew install maven on macOS or download from Maven).
- Git: To clone the repository.

## For Docker Deployment

Docker: Install Docker Desktop (available for Windows/Mac or Linux).
Docker Compose: Included with Docker Desktop or install separately (e.g., sudo apt-get install docker-compose on Linux).


## Setup and Running Locally

Clone the Repository
```
git clone https://github.com/Ayub-Ian/carwiki.git
cd carwiki
```

Run the Application
```
mvn spring-boot:run
```

Access the Application

- Auction Application docs: http://localhost:8671/swagger-ui.html
- Search Application docs: http://localhost:8080/swagger-ui.html



## Setup and Running with Docker

Clone the Repository (if not already done)
```
git clone https://github.com/Ayub-Ian/carwiki.git
cd carwiki
```

Create .env FileCreate a .env file in the project root with the following content:
```
# MySQL
AS_MYSQLDB_ROOT_PASS
AS_MYSQLDB_USER
AS_MYSQLDB_USER_PASS
AS_MYSQLDB_DATABASE

# MongoDB
SS_MONGO_NAME
SS_MONGO_PASS
SS_MONGO_DB

```

Start the Services
```
docker-compose up --build -d
```

Access the Application
- Auction Application docs: http://localhost:8671/swagger-ui.html
- Search Application docs: http://localhost:8672/swagger-ui.html
