
# DeployForge

**A Production-Oriented CI/CD and Cloud Deployment Platform**

DeployForge is a hands-on DevOps engineering project demonstrating how to build, test, containerize, automate, and deploy a Python application using modern DevOps practices.

The project focuses on automation, containerization, infrastructure as code, cloud deployment, security, and operational monitoring.

## Project Objectives

- Build and maintain a Python Flask application.
- Automate application testing using GitHub Actions.
- Build production-ready Docker images.
- Manage local application environments using Docker Compose.
- Provision AWS infrastructure using Terraform.
- Deploy containerized applications using Amazon ECS.
- Store container images in Amazon ECR.
- Monitor application health and infrastructure using Amazon CloudWatch.
- Apply security and reliability best practices.

## Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python 3.12 |
| Backend Framework | Flask 3.1 |
| WSGI Server | Gunicorn |
| Version Control | Git |
| Source Code Management | GitHub |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Local Container Management | Docker Compose |
| Infrastructure as Code | Terraform |
| Container Registry | Amazon ECR |
| Cloud Platform | AWS |
| Container Deployment | Amazon ECS |
| Monitoring and Logging | Amazon CloudWatch |
| Testing | Pytest |

**Note:** AWS and Terraform components are planned and have not yet been implemented.

## Architecture

The planned DeployForge delivery architecture:

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions CI/CD
    |
    +---- Run Python Tests
    |
    +---- Build Docker Image
    |
    v
Amazon ECR
    |
    v
Amazon ECS
    |
    v
Running Application
    |
    v
Amazon CloudWatch
(Monitoring and Logs)
```

## Current Implementation Status

- [x] Flask application and application factory
- [x] Application configuration
- [x] Automated tests using Pytest
- [x] Gunicorn production server
- [x] Docker image
- [x] Non-root container execution
- [x] Docker health checks
- [x] Docker Compose configuration
- [x] Docker build context exclusions
- [x] Initial GitHub Actions CI workflow
- [ ] GitHub repository integration and CI execution
- [ ] Docker image build and validation in CI
- [ ] Amazon ECR integration
- [ ] Terraform infrastructure
- [ ] Amazon ECS deployment
- [ ] CloudWatch monitoring and logging

## Local Development Setup

### Prerequisites

Install the following tools:

- Python 3.12
- Git
- Docker Engine
- Docker Compose

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd DeployForge
```

### 2. Create a Python Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Development Dependencies

```bash
python -m pip install -r requirements-dev.txt
```

### 4. Run Automated Tests

```bash
python -m pytest -v
```

### 5. Run the Application Locally

```bash
gunicorn --bind 0.0.0.0:8000 --workers 2 'app:create_app()'
```

Application URL: http://localhost:8000

Health endpoint: http://localhost:8000/health

### 6. Run Using Docker Compose

Build and start the application:

```bash
docker compose up -d --build
```

Check container status:

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs -f
```

Stop the application:

```bash
docker compose down
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Application information |
| GET | `/health` | Application health status |

## Testing

DeployForge uses Pytest for automated testing.

Current test coverage includes:

- Home endpoint response
- Health endpoint response
- Unknown endpoint handling
- Testing configuration
- JSON response content types

Run the test suite:

```bash
python -m pytest -v
```

## Security Practices

DeployForge follows security-conscious development practices:

- Run the application inside Docker using a non-root user.
- Keep secrets and environment variables out of source control.
- Exclude unnecessary and sensitive files using `.gitignore` and `.dockerignore`.
- Use read-only repository permissions in GitHub Actions.
- Bind local development ports to localhost.
- Keep production dependencies separate from development dependencies.
- Use Docker health checks to monitor application health.

Additional security controls will be implemented as the project evolves.

## Project Roadmap

### Phase 1 — Application Foundation
- [x] Flask application
- [x] Application configuration
- [x] Pytest automated tests
- [x] Gunicorn production server

### Phase 2 — Containerization
- [x] Dockerfile
- [x] Non-root container user
- [x] Docker health checks
- [x] Docker Compose
- [x] Docker build context optimization

### Phase 3 — Continuous Integration
- [x] Initial GitHub Actions workflow
- [ ] Execute CI workflow on GitHub
- [ ] Docker image build in CI
- [ ] Container image validation

### Phase 4 — AWS Infrastructure
- [ ] Terraform infrastructure
- [ ] Amazon ECR
- [ ] Amazon ECS
- [ ] Application deployment

### Phase 5 — Monitoring and Operations
- [ ] CloudWatch logs
- [ ] CloudWatch metrics
- [ ] Monitoring and alerting
- [ ] Operational runbooks
