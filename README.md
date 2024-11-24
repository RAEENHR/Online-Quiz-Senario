# User Management System with Course Enrollment and Quizzes

This Python application allows users to sign up, log in, enroll in courses, and take quizzes. It also provides a password recovery system via security questions. The data is stored and managed in JSON files, making it easy to read, modify, or extend.

## Features

- User Sign-Up: New users can sign up with a username, email, password, birth year, and security questions.
- Login: Users can log in using either their username or email, with password verification.
- Password Recovery: Users can reset their passwords using security questions.
- Course Enrollment: Users can enroll in available courses, such as "Python Basics" or "Advanced Python."
- Quizzes: After enrolling in a course, users can take quizzes related to that course. Their scores are saved.
- Data Storage: All user data, courses, quizzes, and security questions are stored in JSON files.

## Prerequisites

To run this application, you need the following:

- Python 3.x
- JSON files for users, courses, and quizzes.

### JSON Files:
- user_db.json: Stores user information (username, email, password, birth year, courses).
- python_basic.json: Stores information about the "Python Basics" course (students enrolled, quiz scores).
- Advanced_python.json: Stores information about the "Advanced Python" course (students enrolled, quiz scores).
- quiz.json: Contains the quiz questions and answers for both Python Basic and Advanced Python courses.
- security_question.json: Contains predefined security questions for password recovery.

## File Structure

/project_directory
    ├── user_db.json           # User data storage
    ├── python_basic.json      # Course data for Python Basics
    ├── Advanced_python.json   # Course data for Advanced Python
    ├── quiz.json              # Quiz questions and answers
    ├── security_question.json # Security questions for password recovery
    ├── main.py                # Main Python script (this file)
## How to Run the Application

1. Install Python 3.x (if not installed).
2. Ensure that all required JSON files (user_db.json, python_basic.json, Advanced_python.json, quiz.json, security_question.json) are present in the project directory.
3. Run the application by executing the main.py script.

python main.py
4. Follow the on-screen instructions to:
   - Sign up as a new user.
   - Log in using your credentials.
   - Take courses and quizzes.

## Usage

### Sign Up:
1. Enter a unique username and email.
2. Set a password with at least one letter and one number.
3. Provide a birth year that makes you eligible for the app (18–50 years old).
4. Answer two security questions to help recover your password in case you forget it.

### Log In:
1. Enter your username or email.
2. Provide your password to gain access to the system.
3. If you forget your password, you can reset it using the security questions you set during sign-up.

### Take Courses:
1. Once logged in, choose to enroll in available courses ("Python Basics" or "Advanced Python").
2. You can only take the quiz for a course if you're enrolled in that course.

### Take Quizzes:
1. After enrolling in a course, you can take the related quiz.
2. Your score will be recorded in the course file and updated in your user profile.

### Password Recovery:
1. If you forget your password, you can use the security questions to recover it.

## Code Structure

### Main Classes:

1. Json Class: 
   - Responsible for loading and saving JSON data.

2. SignUp Class: 
   - Handles user sign-up, including username, email, password, birth year, and security questions.

3. Login Class: 
   - Manages the login process and password recovery through security questions.

4. Taking_course Class: 
   - Allows users to enroll in courses and take quizzes. Saves their progress and quiz scores.
5. Main Class: 
   - Displays the main menu and routes the user to different functionalities (sign-up, login, course enrollment, etc.).

## Example Workflow

1. Sign-Up: A user creates an account by entering a username, email, password, birth year, and answering security questions.
2. Login: The user logs in with their credentials.
3. Course Enrollment: After logging in, the user can enroll in courses.
4. Taking Quizzes: The user takes quizzes and receives scores.
5. Password Recovery: If the user forgets their password, they can recover it using their security questions.

## Potential Improvements

- Security: The current password handling is basic. Password hashing and encryption should be implemented for better security.
- Database Management: Instead of storing data in JSON files, consider using a database like SQLite or MongoDB for better scalability and data management.
- User Interface: This is a command-line interface (CLI) application. You could create a graphical user interface (GUI) for a better user experience.

## License

This project is open source and available under the [MIT License](LICENSE).
