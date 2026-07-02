# FastAPI with React:

A Basic Setup of **FastAPI** as a backend with **React** on the Frontend and **Mongodb** for Backend with **Docker** Setup.

## 📦 Tech Stack:

- [FastAPI](https://fastapi.tiangolo.com/) - FastAPI framework, high performance, easy to learn, fast to code, ready for production.
- [Mongo DB](https://www.mongodb.com) - Build the next big thing.
- [React Js](https://reactjs.org) - A JavaScript library for building user interfaces.
- [Carbon Design System](https://carbondesignsystem.com/) - Carbon is IBM’s open source design system for products and digital experiences.
- [Docker](https://www.docker.com/) - Docker is a platform designed to help developers build, share, and run modern applications. We handle the tedious setup, so you can focus on the code.

## Getting Started:

- Clone Repo

```bash
cd /path/to/folder
mkdir fastapi-react
cd fastapi-react
git clone https://github.com/Arvind-4/FastAPI-with-React .
```

- Create a Virtual Environment

```bash
cd fastapi-react
python3.10 -m venv .
source bin/activate
```

**For Windows use:** `.\Scripts\activate`

- Install Dependencies

```bash
pip install -r apps/backend/requirements.txt
```

Add Your Environment variable to `.env`.
Refer `.sample.env` file.

- Build Frontend

```bash
cd /path/to/folder/fastapi-react
npm i --prefix apps/frontend
```

- Using Docker-Compose:

```bash
docker compose up --build
```
