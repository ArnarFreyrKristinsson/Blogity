# Overview

A RESTful API built with the Django REST framework for managing user-generated content through posts and comments. This API supports typical blog or forum-style interactions, where anyone can read content, and only authenticated users can contribute where users can only modify their own content.

Designed to support public content viewing, user registration, and secure content modification using JWT-based authentication.

**Note:** The API is stored on an instance that needs some time to spin up to save costs. 

Feel free to access the [API](https://arnarfreyr.is/api/)

# Table of contents

1. [Features](#features)
2. [Local installation](#local-installation)
3. [Access the API](#access-the-api)
4. [API-documentation](#api-documentation)
5. [Contribution](#contribution)
6. [Feature requests](#feature-requests)
7. [Bug Reports](#bug-reports)
8. [Contact](#contact)


## Features

- **Public Content Viewing:** Posts and comments are readable without authentication.
- **User Registration** New users can be created by anyone and passwords are hashed.
- **JWT User Login** Users log in with credentials and receive a signed JWT for authenticated access.
- **Token-based Authentication:** All write operations require a valid access token obtained at login; tokens are used to secure user-specific actions.
- **CRUD Operations:** Standard REST support for creating, reading, updating and deleting posts and comments with access restricted to content owners.
- **Swagger UI Documentation:**  Swagger UI provided for live endpoint testing

## Local installation

### Prerequisites

- Python 3.11.4 or higher
- PostgreSQL (latest version should work) 
- A REST client like Postman or curl (optional, if not using Swagger UI directly)

### Installation
  
1. **Clone the Repository to your local machine**
   
   Run the following command to clone the project:
   ```
   git clone https://github.com/afk0901/Blogity
   ```
2. **Set Up a Virtual Environment**

   Run the following command to create a virtual environment:
   ```
   python -m venv venv
   ```
3. **Install Dependencies**
   
   Run the following command to install dependencies:
   ```
   pip install -r requirements.txt
   ```
   
   Run the following command to install development dependencies such as Linters, pre-commit and Mypy:
   ```
   pip install -r requirements-dev.txt
   ```
     
4. **Database Initialization**
    
    Run the following command to setup the database:
   
    ```python manage.py migrate```

5. **Install Pre-commit Hooks** (Optional but highly recommended)
   Set up pre-commit hooks to ensure code style and standards are verified before each commit, if the intention is to commit to the repository:

   Run the following command to set up pre-commit hooks:
   
   ```pre-commit install```

6. **Start the Development Server**
    Run the following command to run the development server locally with the hardcoded local settings:
    ```python manage.py runserver ```

## Running the tests ##
   
   1. Set the ENV environment variable to DEV either in .env file or in the terminal
   2. Run ```python manage.py test```. 
      You can also use an optional file path if only testing certain directory or 
      file as the second parameter to this command.

## Access the API ##
   
   The API can be accessed at ```/api/``` (place it after the base URL), which will direct you to the Swagger (drf-spectacular) UI page.
   Do not hesitate to fiddle around with it to get a feeling of how the API works.

## API documentation
Swagger UI provides detailed documentation for all API endpoints, including descriptions, parameter requirements, and example responses. 
This feature simplifies the process of integrating and testing the API.

## Contribution
Contributors are always welcome! If you wish to contribute:

1. Fork or clone the repository.
2. Make your changes in a separate branch.
3. Ensure your code adheres to the existing style and passes quality checks. We are using Black, Isort, Mypy and flake8.
   You should have installed pre-commit already if you followed the local installation steps which will take care of these
   if it's hooks are installed correctly.
5. Submit a pull request with your changes and a detailed description of the changes to this repository.
6. In your pull request, explain the value your contribution brings to the project and how it enhances/improves the game.


## Feature requests ##
If you have any feature requests in mind that could enhance the API please make an issue here in the repository and use the feature request template.

## Bug Reports ##
If you encounter any bugs please make an bug report in the issues here in this repository and use the bug report template.

## Contact ##
For further support regarding to this project or collaboration, don't hesitate to send me an <a href="mailto:arnarfkr@gmail.com">email</a> and I will try to help you.


  
