# Online Study Portal

User Authentication: Secure login and registration system for students and instructors.
Course Management:   Instructors can create and manage courses, upload study materials, and track student progress.
Study Resources:     Upload notes, videos, and other resources for courses.
Discussion Forum:    A space for students and instructors to discuss course-related topics.
Notifications:       Receive notifications about new course materials, upcoming exams, or announcements.

## Technologies Used

Python 3.x
Django: Web framework used for building the backend.
HTML/CSS/JavaScript: For frontend design and interaction.
PostgreSQL: Database for storing user and course data.
Bootstrap: For responsive design.
Django Rest Framework: For creating APIs (if required).



### 1. Clone the repository


git clone https://github.com/yourusername/online-study-portal.git
cd online-study-portal
2. Set up a virtual environment
It's a good practice to create a virtual environment to manage dependencies.


python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install dependencies
pip install -r requirements.txt

4. Set up the database
Make sure you have PostgreSQL or any other database set up and configured in your settings.py.

Run the following commands to set up the database tables:
python manage.py migrate

5. Create a superuser
Create an admin account to access the Django admin panel:
python manage.py createsuperuser

6. Run the server
python manage.py runserver
