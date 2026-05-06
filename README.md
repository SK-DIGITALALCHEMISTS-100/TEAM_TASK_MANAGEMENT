# Team Task Manager

A Full-Stack Team Task Manager built with Django, Django Rest Framework, PostgreSQL, and Vanilla JavaScript with TailwindCSS.

## Features
- **Authentication**: JWT-based login and registration.
- **Role-Based Access**: 
  - `Admin`: Can create projects, create tasks, and assign them to members.
  - `Member`: Can view assigned tasks and update their status.
- **Dashboard**: Track tasks, statuses, and overdue items.
- **API**: Full REST API built with Django Rest Framework.

## Local Setup

1. **Clone the repository** (if pushed to GitHub) or navigate to the directory.
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Run the server**:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and go to `http://localhost:8000`.

## Deployment to Railway (Mandatory Instructions)

Since this app needs to be deployed to Railway for selection, follow these exact steps to make it live:

1. **Push to GitHub**:
   - Initialize a git repository in this folder: `git init`
   - Add all files: `git add .`
   - Commit: `git commit -m "Initial commit"`
   - Create a new repository on your GitHub account.
   - Push the code: `git remote add origin <your-repo-url>` and `git push -u origin main`.

2. **Deploy on Railway**:
   - Go to [Railway.app](https://railway.app/) and login with GitHub.
   - Click **New Project** -> **Deploy from GitHub repo**.
   - Select the repository you just created.
   - Railway will automatically detect the `Procfile` and `requirements.txt` and start building.

3. **Add PostgreSQL Database in Railway**:
   - In your Railway project, click **New** -> **Database** -> **Add PostgreSQL**.
   - Railway will automatically provision a database.

4. **Link the Database**:
   - Go to your Django App service in Railway.
   - Go to the **Variables** tab.
   - Add a new variable named `DATABASE_URL` and set its value to `${{Postgres.DATABASE_URL}}` (Railway will suggest this auto-completion).
   - Add a new variable `SECRET_KEY` and give it a random long string (e.g., `my-super-secret-key-12345`).
   - Add `DEBUG` and set it to `False`.
   - Add `ALLOWED_HOSTS` and set it to `*`.

5. **Run Migrations in Production**:
   - In Railway, go to your Django app service -> **Variables**.
   - Alternatively, Railway might run them automatically, but to be sure:
   - Go to the **Deployments** tab, click the latest deployment, and open the **Terminal**.
   - Run: `python manage.py migrate`.

6. **Done!**
   - Click on the generated **Public Domain** in the Railway Settings tab to view your live app!
