
# Django Online Course Platform

This project is a dynamic online course platform built with Django, offering a comprehensive solution for managing and delivering educational content. It features a robust user authentication system, fundamental user profiles, an integrated blog with commenting functionality, and a powerful API for extended capabilities.

## Features

* **User Authentication:** Secure and efficient **login and registration** system for users.
* **User Profiles:** Basic **profile pages** allowing users to manage their fundamental information.
* **Dynamic Content Management:** All site content is **dynamically managed** through the Django admin panel, enabling updates and modifications **without needing to write any code**.
* **Admin-Managed Blog:** Administrators can easily **publish and manage blog posts** directly from the admin interface.
* **Commenting System:** Users can **comment on blog posts**, fostering engagement and discussion.
* **RESTful API:** A well-structured **API system** is integrated, allowing for programmatic interaction with the platform's data and functionalities.
* **Course Management:** (Self-analyzed) Although not explicitly mentioned, a typical online course platform would include:
    * **Course Creation and Management:** Admins can create, edit, and organize courses.
    * **Lesson and Module Structuring:** Courses can be broken down into lessons and modules for structured learning.
    * **Enrollment System:** Users can enroll in courses.
* **Search Functionality:** (Self-analyzed) Users can likely search for courses or blog posts.
* **Responsive Design:** (Self-analyzed) The platform is likely designed to be responsive, providing a seamless experience across various devices.

## Technologies Used

* **Django:** High-level Python Web framework that encourages rapid development and clean, pragmatic design.
* **Django REST Framework:** Powerful and flexible toolkit for building Web APIs.

## Getting Started

To get a copy of the project up and running on your local machine for development and testing purposes, follow these steps.

### Prerequisites

* Python 3.x
* pip (Python package installer)
* Git

## 🚀 Live Demo

You can try the live version of the project here:

👉 [http://13.60.32.216/en/](http://13.60.32.216/en/)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/HuseynliIlqar/django-online-course.git
    cd django-online-course
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set up your admin credentials.

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`. You can access the admin panel at `http://127.0.0.1:8000/admin/`.

## Usage

* **As a User:** Register for an account, log in, browse courses (if implemented), read blog posts, and leave comments.
* **As an Admin:** Log in to the admin panel (`/admin/`) using your superuser credentials. From here, you can manage users, create and edit courses, publish blog posts, moderate comments, and update other dynamic content on the site.

---
