# 💳 Credit Card Advisor (AI-Powered)

This is an intelligent credit card recommendation system built with **Flask** and powered by **OpenAI's GPT-3.5** API. It provides smart, personalized credit card suggestions based on a user's income, spending habits, and preferred benefits.

---

## 🚀 Features

- ✨ AI-powered credit card recommendations using GPT
- 📊 Custom inputs: monthly income, spend, and benefit preferences
- 🎨 Clean dark-themed UI (GitHub style)
- ⚡ Fast, simple Flask backend
- 🔒 Secure `.env` for storing your API key

---

## 🛠️ Tech Stack

- Python 3.x
- Flask
- OpenAI API (GPT-3.5)
- HTML, CSS, JavaScript
- Bootstrap (optional for styling)

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/TejJeeney/credit-card-advisor.git
cd credit-card-advisor
```

2. Create and activate virtual environment

python -m venv ccenv
ccenv\Scripts\activate  # For Windows

3. Install required packages

pip install -r requirements.txt

4. Add your OpenAI API key

Create a .env file in the root folder and add:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    🔒 Keep this file secret and don’t upload it to GitHub.



▶️ Run the Application

cd app
python main.py

Open your browser and go to:

http://127.0.0.1:5000


🧠 How It Works

    User submits monthly income, spend, and benefit preferences

    Backend creates a GPT prompt with this data

    GPT-3.5 generates JSON recommendations

    Frontend displays the AI’s recommendations


---

### ✅ How to Use

1. Copy the entire block above ⬆️
2. Open your project folder
3. Create a file named `README.md`
4. Paste this content into it
5. Save and run:


## 👤 Author

Made with ❤️ by **Tejasva Gairi**
