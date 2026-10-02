# SWD_Proj1 Overview
Author Names: Steph Rivera, Tyler Black, Cameron Greeson, Pete Dives
Repo URL: https://github.com/FrostyBagels/SWD_Proj1

In this project, our group developed a simple web application that allows students to track their GPAs. Students are able to register for the application and, after successfully logging in, enter completed courses along with their corresponding letter grades. The application then displays all previously entered courses and calculate their overall GPA. Students are also able to update their letter grades if they were entered incorrectly.

# Process Requirement
The team was required to use the Waterfall process model to follow its traditional phases: 
- Communication
- Planning
- Modeling
- Construction
- Deployment

# Communication Phase
## Team Roles

|Name|Role(s)|
|--|--|
| Cameron | Developer |
| Tyler | Tester & Documentation |
| Stephanie | Manager & Documentation | 
| Pete | Developer 2 & Documenter |

# Planning Phase
## Schedule

|Phase|Task|Start|End|Duration|Deliverable|
|---|---|---|---|---|---|
|Modeling|Requirements Analysis|09/21/26|09/24/26|3 days|Use Case Diagram|
|Modeling|Data Model|09/21/26|09/24/26|3 days|Class Diagram|
|Construction|Coding|09/25/26|09/30/26|5 days|Code|
|Construction|Testing|09/25/26|10/02/26|7 days|Test Report|
|Deployment|Delivery|10/02/26|10/03/26|1 days|Final Commit/Push|


# Construction Phase
The construction of this application was primarily handled by the two developers—Pete and Cameron—,
and some addition work was done by Tyler and Stephanie. All work was done individually
on separate branches and merged into a development branch (`dev`). All team members approved
and monitored the status of the `dev` branch.

# Testing Phase
The GPA calculation logic (`calculate_gpa` in the `gpacalculator3250` package) is covered by unit tests in `src/tests/test_gpa_calculator.py` using _pytest_. To run them from the root directory of the project:
```bash
cd src
python -m pytest
```

| Functionality Tested | Date     | Result |
|---|----------|--------|
| Log In | 09/25/26 | passed |
| Sign Up | 09/25/26 | failed |
| Course Data Load (Database) | 09/25/26 | failed |
| Sign Up | 09/26/26 | passed |
| GPA Calculation | 09/27/26 | passed |
| Course Data Load (Database) | 09/29/26 | passed |
| Weighted GPA across multiple courses (`test_weighted_multi_course_average`) | 09/30/26 | passed |
| GPA for a single course (`test_single_course`) | 09/30/26 | passed |
| Empty enrollment list returns 0 (`test_empty_list_returns_zero`) | 09/30/26 | passed |
| Ungraded and unrecognized grades are ignored (`test_ignores_upgraded_and_unrecognized_grades`) | 09/30/26 | passed |
| Edge cases: zero credits and null grades/credits (`test_edge_cases_and_null`) | 10/01/26 | passed |


# Deployment Phase
The app can be run either with Docker (recommended) or directly with Python in a virtual environment.

## Running with Docker (Recommended)

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed, with the Docker daemon running (e.g., Docker Desktop is open)
- Git

Python does not need to be installed on the host machine; the Docker image includes everything the app needs.

### 1. Clone the repository
```bash
git clone https://github.com/FrostyBagels/SWD_Proj1.git
cd SWD_Proj1
```

### 2. Build the Docker image
Run this from the root directory of the project (the directory containing the `Dockerfile`). The trailing `.` tells Docker to use the current directory as the build context.
```bash
docker build -t swd-proj1 .
```

### 3. Run the container
```bash
docker run --rm -p 5001:5001 swd-proj1
```
The application is attached to port `5001` to ensure cabatibility 
with MacOS deviced running AirPlay.

### 4. Open the app
Open http://localhost:5001 in a web browser.

> **Note:** Flask's startup log lists addresses such as `http://172.17.0.2:5001`. Those are addresses *inside* the container and are not reachable from the host. Use http://localhost:5001 instead.

To stop the app, press `Ctrl+C` in the terminal running the container.

If port 5001 is already in use on the host, map a different host port and open that port in the browser instead, e.g.:
```bash
docker run --rm -p 8080:5001 swd-proj1
```

## Running Locally with Python

### Prerequisites
- Python 3.10 or newer
- pip
- Git

### 1. Clone the repository and create a virtual environment
```bash
git clone https://github.com/FrostyBagels/SWD_Proj1.git
cd SWD_Proj1
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Start the Flask development server
Run this from the root directory of the project. `PYTHONPATH=src` lets Python find the `app` package inside `src/`.
```bash
PYTHONPATH=src python -m flask --app app run --port 5001
```

### 4. Open the app
Open http://127.0.0.1:5001 in a web browser. Press `Ctrl+C` to stop the server.


## User Interface
Students will have two options when they land on the home page: 
![Initial Screen](pics/initial_screen.jpg)

To log in, they will select Login.

To register, they will select Sign Up.
![Enrollment Window](pics/enrollment_window.jpg)

First time users will see the Enrollments screen empty.
![No Enrollments](pics/no_enrollments.jpg)

To add courses and grades, click on Grade Entry. Select course and grade from the drop-down menus. 
![Course and Grade Selection](pics/course_and_grade_selection.jpg)

Once necessary courses have been added, the Enrollments screen will automatically calculate the GPA.
![Filled Course and Grade](pics/filled_course_and_grade.jpg)

Students can update grades at any time by selecting a new letter grade and clicking Update. Students can delete courses at any time by clicking on Delete. The GPA automatically updates whenever a course is added, a grade is updated, or a course is deleted.