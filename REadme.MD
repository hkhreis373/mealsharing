# MealShare - A Meal Sharing Platform

## Project Overview

**MealShare** is a web application designed to facilitate the sharing and discovery of homemade recipes. It allows users to create, share. The platform aims to build a vibrant community of cooking enthusiasts, fostering connections and culinary creativity.

---

## Features

### Core Features

1. **User Authentication and Profile Management**

   - **Registration & Login:** Users can create accounts, log in, and log out securely.
   - **Profile Customization:** Users can set up and edit their profiles, including uploading profile pictures and specifying cooking preferences.

2. **Recipe Creation and Sharing**
   - **Create Recipes:** Users can create detailed recipes with ingredients, instructions, and images.
   - **Public Sharing:** Recipes are shared publicly, allowing all users to view, like, and comment on them.

---

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap 5
- **Forms Handling:** Django Crispy Forms with Bootstrap 5
- **Database:** SQLite (default), can be switched to PostgreSQL for production
- **Image Handling:** Pillow
- **Version Control:** Git & GitHub
- **IDE:** PyCharm, Vscode

---

## Installation

Follow these steps to set up and run the MealShare project on your local machine.

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.8+**
- **pip**
- **Git**
- **Virtualenv** (optional but recommended)
- **PyCharm** or any other preferred IDE

### Configure Git Editor

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/hkhreis373/mealsharing.git
   cd mealshare
   ```
2. **Create and Activate a Virtual Environment:**

   ```bash
   On Unix or MacOS:
      python3 -m venv env
      source env/bin/activate
   ```

   ```bash
   On Windows:
      python -m venv env
      env\Scripts\activate
   ```

3. **Upgrade pip:**

   ```bash
   pip install --upgrade pip

   ```

4. **Install Required Packages:**

   ```bash
      pip install django-crispy-forms django-crispy-bootstrap5 Pillow

   ```

5. **Apply Migrations and running the server:**

   ```bash
      python manage.py makemigrations
      python manage.py migrate
   ```

   ```bash
      python manage.py runserver
   ```
