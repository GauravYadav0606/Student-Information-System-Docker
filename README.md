# Student Information System Using Docker

A basic student information web application built with **Python Flask** and containerized using **Docker**. This practical demonstrates building an image, running a container with port mapping, inspecting logs, managing the container lifecycle, and publishing the image to Docker Hub.

## Project details

- **Author:** Gaurav Yadav
- **Technology:** Python 3.13, Flask 3.1.2, Docker
- **Application port:** `5000`
- **Local image:** `student-info-app:v1`
- **Docker Hub image:** [`gauravyadav0606/student-info-app:v1`](https://hub.docker.com/r/gauravyadav0606/student-info-app)

## Features

- Displays sample student records.
- Shows the total number of students.
- Allows a user to add a student name, course, and email.
- Runs in Docker and is accessible through a browser.

> **Note:** This is a basic demonstration. Records are stored in memory and reset when the app restarts. Do not enter real or sensitive student information.

## Project structure

```text
Student-Information-System-Docker/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
├── screenshots/
│   └── README.txt
└── report/
    └── Student_Information_Docker_Assessment_Report.docx
```

## Build and run with Docker

Run these commands from the project directory:

```powershell
docker build -t student-info-app:v1 .
docker run -d -p 5000:5000 --name student-container student-info-app:v1
docker ps
```

Open **http://localhost:5000** in your browser.

## Useful Docker commands

```powershell
docker logs student-container
docker inspect student-container
docker stats student-container
docker stop student-container
docker rm student-container
```

Recreate the container from the existing image:

```powershell
docker run -d -p 5000:5000 --name student-container student-info-app:v1
```

## Docker Hub

Pull and run the published image on another computer with Docker installed:

```powershell
docker pull gauravyadav0606/student-info-app:v1
docker run -d -p 5000:5000 --name student-container gauravyadav0606/student-info-app:v1
docker ps
```

Open **http://localhost:5000**. The Docker Hub repository must be public for anonymous users to pull it.

## Screenshots

Add your own actual screenshots to the `screenshots/` folder. Suggested evidence:

1. Docker installation verification
2. Project directory
3. Flask application source
4. Requirements file
5. Dockerfile
6. Docker image build
7. Running container
8. Application in browser
9. Container inspection
10. Container logs
11. Container stopped
12. Container removed
13. Container recreated
14. Image tagging
15. Docker Hub push
16. Docker Hub repository and `v1` tag
17. Docker pull and run demonstration

## Practical report

The editable assessment report is included in the `report/` folder. Insert your actual screenshots into its marked placeholders before submission.

## Author

**Gaurav Yadav**
