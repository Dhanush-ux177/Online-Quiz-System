# Online Quiz System - Student Project



## 📋 Project Overview
This is a web-based Online Quiz System developed using Python Flask framework. It allows students to take programming quizzes in Python, Java, and C languages. Administrators can add questions and view student results.

## ✨ Features
✨ Additional Features

This Online Quiz System can be further enhanced with several advanced features to improve functionality, user experience, and scalability. The quiz module can include timer-based quizzes, multiple difficulty levels such as easy, medium, and hard, and category-wise questions to better organize content. Features like randomized answer options, negative marking, question skipping, and a progress bar can make the quiz experience more interactive and realistic.

From a user perspective, the system can be upgraded with a complete authentication system including registration and login, along with a personalized dashboard where users can track their quiz history, view past scores, and analyze their performance over time. Adding a leaderboard, badges, and achievement systems can increase engagement and motivation among users.

For analytics, the platform can provide detailed result insights such as correct and incorrect answers, score percentages, and visual performance graphs. Users could also download their results in formats like PDF or CSV, while administrators can access a comprehensive analytics dashboard to monitor overall performance.

Security can be improved by implementing password hashing, proper session management, role-based access control for admins, and input validation to prevent vulnerabilities like SQL injection. In terms of user interface, enhancements such as responsive design for mobile devices, dark mode, modern styling frameworks like Bootstrap or Tailwind CSS, and smooth animations can significantly improve usability and appearance.

Advanced features may include REST API integration, multi-language support, email notifications for quiz results, third-party login options like Google OAuth, chatbot assistance, and auto-saving quiz progress. On the admin side, functionalities like bulk question uploads via CSV or Excel, editing and deleting questions, managing users, exporting data, and scheduling quizzes can make the system more powerful and efficient.

Finally, for deployment and development, features like Docker support, CI/CD pipelines, environment variable configuration, logging systems, and custom error handling pages can make the application more robust, scalable, and production-ready.

### For Students:
- ✅ Automatic registration on first login
- ✅ Choose from 3 programming languages (Python, Java, C)
- ✅ 10 multiple choice questions per quiz
- ✅ Questions appear in random order
- ✅ Instant score calculation
- ✅ Option to retake quiz

### For Admin:
- ✅ Separate admin login
- ✅ Dashboard to manage system
- ✅ Add new questions with 4 options
- ✅ View all student results with scores

## 🛠️ Technology Used
- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3
- **Database:** SQLite
- **Template Engine:** Jinja2

⚙️ Installation & Setup
🔧 Step 1: Clone the Repository
git clone https://github.com/Dhanush-ux177/Online-Quiz-System.git
cd Online-Quiz-System

🐍 Step 2: Install Dependencies
pip install flask

▶️ Step 3: Run the Application
python app.py

🌐 Step 4: Open in Browser
Student Login: http://127.0.0.1:5000
Admin Login: http://127.0.0.1:5000/admin
🔑 Admin Credentials
Username: admin
Password: admin123
🚀 Live Demo (Render Deployment)
🌍 Steps to Deploy on Render
Go to https://render.com

Create a new Web Service

Connect your GitHub repository
Set the following:
Build Command:
pip install -r requirements.txt
Start Command:
python app.py
Add a requirements.txt file:
flask
gunicorn
(Optional but Recommended) Update run command:
gunicorn app:app
Click Deploy

🎉 Your app will be live at:
https://your-app-name.onrender.com

🧑‍💻 Usage
👨‍🎓 For Students:
Visit homepage
Enter name (auto-registers)
Choose quiz (Python / Java / C)
Answer 10 MCQs
View score instantly
Retake quiz anytime

👨‍💼 For Admin:
Login via /admin
Add new quiz questions
Manage question bank
View all student results
⚠️ Limitations
❌ Uses SQLite (not ideal for large-scale apps)
❌ No user authentication security (basic login only)
❌ No timer for quiz
❌ No negative marking
❌ UI is basic (can be improved)
❌ Not mobile optimized fully
🔮 Future Improvements
✅ Add user authentication (JWT / sessions)
✅ Add quiz timer
✅ Improve UI with Bootstrap or React
✅ Add leaderboard system
✅ Support more programming languages
✅ Export results (PDF/CSV)
✅ Deploy with Docker
✅ Add REST API support

👨‍💻 Author
🔗 GitHub: https://github.com/Dhanush-ux177

💬 Support

If you like this project ⭐, feel free to support:

Create real UI screenshots mockups
Fix your GitHub formatting issue
Help you deploy it live step-by-step






Password: admin123
Step 4: Open in Browser
Student Login: http://127.0.0.1:5000

Admin Login: http://127.0.0.1:5000/admin
