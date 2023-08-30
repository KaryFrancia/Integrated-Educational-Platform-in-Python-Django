# Integrated Educational Platform in Python Django
Python project, comision43870-CODERHOUSE

This project is a web application on an Integrated Educational platform in Python Django for Management of Students, Teachers, Courses, Deliverables and Payments. It allows the administrator and staff users to add students, teachers, deliverables, register courses and payments, as well as perform database searches. Also, they can edit and delete them if necessary. Each user has their own profile and avatar, which can also be edited or deleted.
## Contenido

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contribution](#contribution)

## Requirements

- Python 3.11.4 (python --version)
- Django 4.2.3 (python -m django --version)

## Installation

1. Clone this repository to your local machine: git clone https://github.com/KaryFrancia/Tercera_pre_entrega_Francia_coderhouse.git
2. Navigate to the project directory: cd coder43870
3. Create and activate a virtual environment:
- Windows:
  ```
  python -m venv myenv
  myenv\Scripts\activate
  ```
- macOS/Linux:
  ```
  python3 -m venv myenv
  source myenv/bin/activate
  ```

4. Install the dependencies: pip install -r requirements.txt

## Usage

1. Run the Django development server:  ```python manage.py runserver```
2. Access the application in your browser by visiting: `http://127.0.0.1:8000/`

## Features

1. **Página de Inicio**: The main page of the application. On the home page you will find two buttons: login and register.
2. **Login**: Enter the platform with the username and password belonging to a staff member.
3. **Register**: Register a new staff user who does not have their own account.
4. **Buscar**: Search for courses, students, teachers, payments, and deliverables in the database.
5. **Profesores**: Add new teachers, edit and delete them, and view the current teachers.
6. **Estudiantes**: Register new students, edit and delete them, and view the current students.
7. **Cursos**: Save new courses, edit and delete them, and view the current courses.
8. **Entregable**: Register new deliverables, edit and delete them, and view the current deliverables.
9. **Pagos**: Add new payments, edit and delete, and view the current payments.
10. **Logout**: Exit platform.
11. **Editar Perfil**: Modify or update the personal information of a registered user on the platform.
12. **Agregar Avatar**: Attach an image or graphic representation that serves as a visual identification of the user on the platform.
   
## Contribution

If you wish to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a branch for your changes: `git checkout -b feature/new-feature`
3. Make your changes and commit them: `git commit -m "Add new feature"`
4. Push your changes to your fork: `git push origin feature/new-feature`
5. Open a pull request on GitHub.
