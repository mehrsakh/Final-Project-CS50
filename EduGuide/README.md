# EduGuide

#### Video Demo 1: [( https://youtu.be/CNtLbp1L49k )]
#### Description:
EduGuide is a simple yet interactive web application designed to help high school students discover and compare university majors based on their interests, academic strengths, and career goals.
I created this project as my **CS50 Final Project** using **Python (Flask), HTML, and CSS**.

The main goal of EduGuide is to make the process of choosing a university major easier and more data-driven. Many students struggle to decide what they want to study after school. EduGuide provides quizzes, comparisons, and helpful information in a clean and friendly way — so users can understand which major fits them best.

---

##  Project Overview

EduGuide has four main parts:

1. **Home Page:**
   Users enter their name to personalize the experience. This step makes the app feel more engaging.

2. **Track Selection:**
   Students choose their high school track (Science, Math, or Humanities). This selection filters the quiz questions to make them relevant.

3. **Quiz Section:**
   A set of ten questions appears for each track. Each question is rated from 0 to 5 based on the user’s preferences.
   After submission, the system calculates a **Match Score** for each major and recommends the best option.

4. **Compare Section:**
   Users can pick any two majors and see a **side-by-side visual comparison**.
   Each major is compared using progress bars and short descriptions in categories like:
   - Duration of study
   - Difficulty
   - Job market demand
   - Average income
   - Match Score

Additionally, the project includes a **Scholarship Checker** that evaluates a student’s chance for financial aid based on GPA and English level, and a **Roadmap Page** that provides a simple overview of how to prepare for university admission.

---

## 🧱 File Structure

EduGuide/
├── app.py
├── static/
│ └── style.css
├── templates/
│ ├── home.html
│ ├── track.html
│ ├── quiz.html
│ ├── results.html
│ ├── compare.html
│ ├── roadmap.html
│ └── scholarship.html
└── README.md


---

## How to Run the Project

1. Install Flask (if not already installed):
   ```bash
   pip install flask

2. Run the application:
python app.py

3. Open your browser and go to:
http://127.0.0.1:5000/

4. The app will start from the home page.

 File Descriptions
app.py — The core of the project. It handles all routes, user input, form submissions, and logic for calculating quiz results and comparisons.

templates/home.html — The first page where the user enters their name.

templates/track.html — Lets the user select their academic track.

templates/quiz.html — Contains the quiz questions and handles scoring logic through Flask forms.

templates/results.html — Displays the recommended major and match score.

templates/compare.html — Compares two majors visually using progress bars.

templates/roadmap.html — Shows steps for preparing for university.

templates/scholarship.html — Checks if the user is eligible for scholarships.

static/style.css — Manages the app’s appearance, layout, and responsive design.

 Logic and Design Choices
Flask Framework:
I used Flask because it’s lightweight and perfect for small web applications. It allowed me to use HTML templates with Python logic.

Match Score Algorithm:
Each question has a weight (0–5). After the quiz, the app averages the results and assigns a “Match Score” to possible majors.
For example, a student strong in math and logic will get a higher score for Computer Science or Engineering.

Compare Visualization:
The compare page uses simple HTML div bars to visualize values like difficulty and income.
This approach is easy to understand and feels more interactive than plain text.

CSS Design:
The design is minimal and student-friendly. I used soft colors and rounded containers for a modern look.
Everything is responsive, so it looks good on both desktop and mobile.

 Challenges Faced
Balancing simplicity with functionality:
I didn’t want the app to look too advanced or automated. It needed to seem like something a student (me) could build for CS50 — not an AI project.

Managing the scoring system:
At first, I had trouble calculating the average match score for multiple majors, but using dictionaries and loops made it cleaner.

Making the compare page visual:
I used inline CSS and simple div bars to represent levels, keeping it functional yet easy to understand.

 Future Improvements
Connect the app to a real database for saving user results.

Add a user login system.

Include more majors and real job data through an API.

Improve quiz logic to include personality traits and not just academic interests.

Add charts using Chart.js for more interactive visuals.

 Conclusion
EduGuide is a personal and educational web app that helps students explore majors and plan their academic paths.
It’s easy to use, visually clean, and built entirely by me using the concepts learned in CS50.

This project taught me how to combine backend logic (Flask) with frontend design (HTML & CSS), manage routes, and create a small but complete web application.

I’m proud of how EduGuide turned out — it represents my growth from CS50’s very first problem set to building something practical and real.

Created by [Mehrsa Khalaj]
CS50 Final Project – 2025
