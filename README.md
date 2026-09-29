# Healthcare-Appointment-System

A simple Python-based Healthcare Appointment Management System for Cygnus Hospital. The program allows users to enter their personal details, select a department, choose a specific medical department, and select a doctor based on their preference.

Features

Collects patient information:

Name

Age

Mobile number

Displays a welcome message from Cygnus Hospital.

Allows users to select a department:

Clinical

Diagnostic

Administrative

Provides clinical department options:

Cardiology

Neurology

Orthopedics

Paediatrics

Allows users to select a doctor from the chosen department.

Displays:

Doctor's name

Qualifications

Years of experience

Available consultation hours

Confirms successful appointment booking.

Displays an error message for invalid department selections.

Technologies Used

Python 3

input() for taking user input

if, elif, and else statements for decision-making

print() for displaying information

Project Structure
Doctor-Appointment-Management-System/
│
├── doctor_appointment.py
└── README.md

How to Run
1. Install Python

Make sure Python 3 is installed on your computer.

You can check your Python version using:

python --version


or:

python3 --version

2. Save the Code

Save the Python program in a file named:

doctor_appointment.py

3. Run the Program

Open a terminal in the project directory and run:

python doctor_appointment.py

How the Program Works

The program follows a simple menu-based flow:

Enter your name
      ↓
Enter your age
      ↓
Enter your mobile number
      ↓
Select Department
      ↓
Clinical Department
      ↓
Select Medical Department
      ↓
Select Doctor
      ↓
Display Doctor Information
      ↓
Appointment Confirmation

Available Clinical Departments
1. Cardiology
Doctor	Qualification	Experience	Availability
Dr. Satish	MBBS, MD (Cardiology)	15 years	10:00 AM - 2:00 PM
Dr. Ravi	MBBS, MD (Cardiology)	10 years	2:00 PM - 6:00 PM
Dr. Rakesh	MBBS, MD (Cardiology)	8 years	6:00 PM - 10:00 PM
2. Neurology
Doctor	Qualification	Experience	Availability
Dr. Sara	MBBS, MD (Neurology)	12 years	10:00 AM - 2:00 PM
Dr. Sakshi	MBBS, MD (Neurology)	9 years	2:00 PM - 6:00 PM
Dr. Samay	MBBS, MD (Neurology)	6 years	6:00 PM - 10:00 PM
3. Orthopedics
Doctor	Qualification	Experience	Availability
Dr. Ramesh	MBBS, MS (Orthopedics)	14 years	10:00 AM - 2:00 PM
Dr. Kavita	MBBS, MS (Orthopedics)	11 years	2:00 PM - 6:00 PM
Dr. Manoj	MBBS, MS (Orthopedics)	9 years	6:00 PM - 10:00 PM
4. Paediatrics
Doctor	Qualification	Experience	Availability
Dr. Ananya	MBBS, MD (Paediatrics)	13 years	10:00 AM - 2:00 PM
Dr. Ritu	MBBS, MD (Paediatrics)	10 years	2:00 PM - 6:00 PM
Dr. Karan	MBBS, MD (Paediatrics)	7 years	6:00 PM - 10:00 PM
Example
Enter your name: Rahul
Enter your age: 25
Enter your mobile number: 9876543210

Hi Rahul, Welcome to Cygnus Hospital.

Enter the department you want to visit:
(Clinical=1, diagnostic=2, administrative=3): 1

You have selected Clinical Department.

Enter the specific clinical department:
Cardiology=1, Neurology=2, Orthopedics=3, Paediatrics=4,
Oncology (cancer)=5, Obstetrics & Gynaecology=6: 1

You have selected Cardiology Department.

Enter the doctor you want to visit:
(Dr. Satish=1, Dr. Ravi=2, Dr. Rakesh=3): 1

You have selected Dr. Satish.
Qualifications: MBBS, MD (Cardiology)
Experience: 15 years in Cardiology
Dr. Satish is available from 10:00 AM to 2:00 PM.

Your appointment with Dr. Satish has been successfully booked.
Please arrive 15 minutes before your scheduled time.

Current Limitations

This project is currently a basic console-based demo. It does not yet include:

Actual appointment date selection

Specific appointment time selection

Database storage

Patient record management

Doctor availability checking

Appointment cancellation

Appointment rescheduling

Diagnostic department functionality

Administrative department functionality

Oncology department functionality

Obstetrics & Gynaecology functionality

Input validation for incorrect age or mobile number

Graphical user interface (GUI)

Future Improvements

The project can be expanded by adding:

A database such as SQLite or MySQL.

Patient registration and login.

Appointment date and time selection.

Automatic appointment IDs.

Appointment cancellation and rescheduling.

Doctor availability management.

Search functionality for doctors.

A graphical interface using Tkinter.

A web interface using Flask or Django.

Proper input validation and error handling.

Learning Objectives

This project is useful for beginners learning Python because it demonstrates:

Variables

User input

Data types

Conditional statements

Nested if-elif-else statements

String formatting

Basic program flow

Building a menu-driven application

Disclaimer

This project is intended for educational and demonstration purposes only. The doctor names, qualifications, experience, and availability shown in the program are sample data and should not be treated as real hospital or medical information.

Author

Himanshi
