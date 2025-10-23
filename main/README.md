# Flask CI/CD Lab

# Backend
Subhan Kashif(FA22-BCS-187)
# Frontend
Hassan Tariq (FA22-BCS-172)
# Devops
Muzammil Abubakar(FA22-BCS-116)

Minimal Flask sample app used to demonstrate CI/CD, testing, Docker packaging, and a tiny frontend.

## Project structure (important files)
- main/app.py — Flask application
- main/templates/layout.html, main/templates/index.html — frontend templates
- main/static/js/main.js — client helper (sendData)
- main/static/css/style.css — styles
- main/tests/test_app.py — pytest tests
- main/requirements.txt — Python dependencies
- main/Dockerfile — container image definition
- main/.dockerignore — Docker ignore rules
- .github/workflows/ci-cd.yml — GitHub Actions workflow for CI/CD
- main/README.md — this file

## What the app provides
- GET / — welcome text
- GET /health — health check (returns "OK")
- POST /data — accepts JSON and echoes it back

## Prerequisites
- Python 3.10
- pip
- (Optional) Docker
- (Optional) GitHub account for Actions / image registry if using CI to push images

## Install & run (Windows)
Open a terminal in the project root (d:\DevOps\flask-lab-project).

Using Command Prompt:
1. Change to the app directory:
   ```
   cd main
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   python app.py
   ```
The app listens on 0.0.0.0:5000 by default.

Using PowerShell:
1. Set PYTHONPATH and run tests / app if needed:
   ```
   cd main
   $env:PYTHONPATH = "$PWD"
   python .\app.py
   ```

## Run tests
From repository root in PowerShell:
```
cd main
$env:PYTHONPATH = "$PWD"
pytest
```
Or from Command Prompt:
```
cd main
set PYTHONPATH=%CD%
pytest
```

## Docker
Build the image (run from the `main` folder):
```
cd main
docker build -t flask-lab-app .
```
Run:
```
docker run -p 5000:5000 flask-lab-app
```

The Dockerfile uses Gunicorn for production in the container image; for local development the app runs with Flask's dev server.

## CI/CD
A GitHub Actions workflow is provided in `.github/workflows/ci-cd.yml`. It:
- checks out the repository
- sets up Python
- installs dependencies and runs pytest
- builds a Docker image and can push it to a registry (configure secrets / registry settings in the workflow)

## Notes and tips
- The app includes a small compatibility patch for werkzeug in CI; this is intentional for demo purposes.
- For production, run the containerized app with the Gunicorn command defined in the Dockerfile instead of Flask's dev server.
- Expose only necessary ports and avoid enabling debug mode in production.

## Contact / Next steps
- Run tests locally, then build the Docker image.
- Inspect `.github/workflows/ci-cd.yml` to adapt the workflow to your registry (set secrets like DOCKERHUB_USERNAME, DOCKERHUB_TOKEN or use GitHub Packages).
- Add more unit tests and input validation for POST /data as needed.