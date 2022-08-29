# Cver

Cver is a CV/Resume builder. The purpose of this project is to sharpen my backend development skill, turning my project idea into models and creating working API endpoints that can be used for any CV/Resume building project.
CV/Resumes are needed for any job or internship application but quite a number of people do not know how to go about creating a Cv on their own, hence the inspiration to create something
for the community, friends family and my network. Although, this project is still in development but the application requirements are:

1. The user should be able to sign up.
2. The user should be able to login in.
3. The user should be able to create a resume.
4. The user should be able to edit and delete an existing resume.
5. The user should be able to select from an existing list of templates.
6. The application should collect the necessary information to create a standard CV.
7. A user should not be able to view/download a CV that belongs to another user. 
8. The admin should be the only entity able to create, edit, and delete resume templates.

## Table of Content

- [Cver](#Cver)
  - [Technologies](#technologies)
  - [How to setup locally](#how-to-setup-locally)
  - [The ER Diagram](#the-er-diagram)
  - [Limitations](#limitations)
  - [Deployment](#deploy-how-to-install-build-product)
  - [Contributing / Reporting issues](#contributing--reporting-issues)
  - [License](#license)

## Technologies

1. Python
2. Django Rest Framework
3. JSON WebToken
4. OpenAPI (SwaggerAPI)
5. HTML
6. CSS
7. Sass

## How to setup locally

1. Create a new virtual environment for this project. *Virtualenv* and *anaconda* are popular choices. ***Please make sure to create a new environment for this project.***
2. Install dependencies by running the following command in your terminal:

  ```bash
  pip install -r requirements.txt
  ```

3. Setup database migrations:

   ```bash
   python manage.py migrate

  ```

4. To visit the API endpoints in your browser at port <http://localhost:8000>, start the server:

   ```bash
   python manage.py runserver
   ```

7. OPTIONAL: Create a super admin account

   ```bash
   python manage.py createsuperuser
   ```

   Visit `/admin/` and login with credentials to have access to the admin dashboard.

That's all! For the API Documentation, visit:

- SwaggerAPI: <http://localhost:8000/>

## The ER Diagram

The Entity-Relation Diagram of this project.
You can view the ER diagram at: https://dbdiagram.io/d/5fbaa7ce3a78976d7b7cef0c

## Limitations

* This application lacks a proper user interface due to my shallow knowledge in frontend development.

## Deploy (how to install build product)

* This Application has not been deployed. 

## Contributing / Reporting issues

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
