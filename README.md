# Wikimedia

This repository contains the Django project for the Wikimedia Intern Application task.


## Project Description

The Wikimedia project is aimed at creating a web application that allows users to view and manage bug reports for various software projects. The application provides a platform for users to submit bug reports, track the status of the reported bugs, and collaborate with other users and developers to resolve the issues.

The main features of the Wikimedia project include:

- Bug Submission: Users can submit bug reports by providing detailed information about the issue, such as the steps to reproduce, expected behavior, and actual behavior.

- Bug Tracking: The application allows users to track the status of their submitted bug reports. They can view the current status, assignees, and any comments or updates related to the bug.

- Collaboration: Users can collaborate with other users and developers by commenting on bug reports, discussing possible solutions, and providing additional information or suggestions.

- Bug Management: The application provides a comprehensive interface for managing bug reports. This includes assigning bugs to specific developers, setting priorities, and categorizing bugs based on their severity or impact.

- Bug Detail View: Users can view detailed information about each bug report, including its description, attachments, and any related discussions or updates.

The Wikimedia project aims to streamline the bug reporting process, enhance collaboration between users and developers, and provide a user-friendly interface for managing and tracking bug reports.

## Installation

To get started with the Wikimedia project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/wikimedia.git

2. ```bash
    cd wikimedia

3. ```bash
    python3 -m venv env
    source env/bin/activate

4. ```bash
    pip install -r requirements.txt

5. ```bash
    python manage.py migrate

6. ```bash
    python manage.py createsuperuser

7. ```bash
    python manage.py runserver


## ## Usage

To use the Wikimedia project, follow these steps:

1. Open your web browser and access the application at `http://localhost:8000`.

2. Sign in with your superuser account created during the installation process to access the admin panel.

3. Explore the bug reports:

   - View Bug List: On the homepage, you can see a list of bug reports submitted by users. Click on a bug report to view its details.

   - Submit a Bug: To submit a new bug report, click on the "Submit Bug" button and fill in the required information, such as the bug description, steps to reproduce, and expected behavior.

   - Track Bug Status: After submitting a bug report, you can track its status by visiting the bug detail page. 


4. Manage Bug Reports (Admin Panel):

   - Assign Bugs: As a superuser, you can assign bugs to specific developers by accessing the admin panel and editing the bug details.

   - Set Priorities: You can set the priority of each bug report based on its severity or impact.

   - Categorize Bugs: You can categorize bugs based on their types or specific software projects.


