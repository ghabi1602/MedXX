# Medx App

![logo](https://github.com/ify-zi/MedX/blob/main/app/static/images/md.png)

## Description

The Medx App is a web-based application designed to facilitate communication between doctors and patients. It features user authentication, real-time chat functionality, and separate interfaces for doctors and patients. The backend is built with the Flask framework, and the frontend is designed with HTML, CSS, and JavaScript. The application also utilizes WebSocket via Flask-SocketIO for real-time messaging.

## Features

- User authentication and authorization
- Doctor and patient profile management
- Real-time chat between doctors and patients
- Online status indication for users
- Secure password hashing
- Database migrations using Flask-Migrate
- MySQL database support

## Screenshots
- landing page
![screenshot1](https://github.com/ify-zi/MedX/blob/main/screenshots/landing_page.jpg)

- patients Dashboard
![screenshot2](https://github.com/ify-zi/MedX/blob/main/screenshots/patient_dashboard.jpg)

- doctor_dashboard
![screenshot2](https://github.com/ify-zi/MedX/blob/main/screenshots/doctor_dashboard.jpg)

- chat interface
![screenshot4](https://github.com/ify-zi/MedX/blob/main/screenshots/chat_interface.jpg)

- doctors_patients_records
![screenshot5](https://github.com/ify-zi/MedX/blob/main/screenshots/doctors_records.jpg)


## Demo Video (tap to watch)

[![Watch the video](https://github.com/ify-zi/MedX/blob/main/screenshots/landing_page.jpg)](https://1drv.ms/v/s!Atxmn4zs8omJmA-JTSiI15Ed_LCH?e=8p30GC)


## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-SocketIO
- MySQL
- HTML
- CSS
- JavaScript

## Installation

### Prerequisites

- Python 3.x
- MySQL
- Virtual environment (optional but recommended)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ify-zi/Medx.git
   cd MedX

2. **Install Requiremnets
    ```bash
    pip install -r requirements.txt

3. **Initialise database:**
    ```bash
    flask db init
    flask db migrate -m "Initial commit"
    flask db upgrade

3. **Start the Server:**

    ```bash
   python -m run

4. **Use a broswer to naviagte the app


## Authors
- Ifeanyi Zion Chidibere - [Github](https://github.com/ify-zi) / [Twitter](https://twitter.com/ify_zi) / [LinkedIn](https://www.linkedin.com/in/ifeanyi-zion-chidiebere-b078371a4)
- Asma Guesmi - [Github](https://github.com/Asma22334585) / [Twitter](https://twitter.com/HaDil08527786) / [LinkedIn](https://www.linkedin.com/in/asma-guesmi)
- Abdessattar Ghabi - [Github](https://github.com/ghabi1602) / [Twitter](https://twitter.com/GhabiAm1602) / [LinkedIn](https://www.linkedin.com/in/abdessattar-ghabi-412a30285)