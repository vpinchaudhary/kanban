## Frontend

- JavaScript
- React with functional components and hooks
- Components & styling with Material-UI
- Drag & Drop using react-beautiful-dnd

## Backend

- Django REST framework for a powerful API
- Django ORM for interacting with the database
- PostgreSQL

## Features

- Multiple kanban boards
- Drag & drop tasks
- CRUD for tasks, labels & columns
- Edit task descriptions with Markdown
- Manage board members
- Update your profile & pick an avatar

## Development setup

Steps to locally setup development after cloning the project.

### Django

Have [Python 3.8](https://www.python.org/downloads/release/python-3810/) installed and in PATH.

```sh
python3 --version
```

```sh
pip install pipenv

pipenv shell

pip install -r requirements.txt
```

### Create Database

These steps are to be followed on Linux. For windows or mac the database creation might differ.

```sh
sudo su - postgres
psql

CREATE USER user_name WITH PASSWORD 'password';
CREATE DATABASE database_name;
GRANT ALL PRIVILEGES ON DATABASE database_name TO user_name;
```

### Load avatars and run Migrations
```sh
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata avatars
python manage.py runserver
```

- API root available at `http://localhost:8000/api/`
- Admin available at `http://localhost:8000/admin/`

### React

- [Node.js](https://nodejs.org) v12 or greater
- [Yarn](https://yarnpkg.com/) v1 or greater

```sh
node --version
yarn --version
```

```sh
npm install
npm start
```

React app is now accessible at `http://localhost:3000`