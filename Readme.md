# 💳 Credit Card Advisor (AI-Powered)
This is a web-based, conversational AI project that recommends the best Indian credit cards for users based on their income, spending habits, and preferred benefits. 

---

## 🚀 Features

- 🔍 Conversational Agent (LLM-based)
- 💰 Credit Card Matching Engine
- 📊 Reward Simulation (e.g., Rs. 8,000/year cashback)
- 💡 User Preferences: Income, Spend, Perks
- 📱 Mobile Responsive UI (HTML/CSS/JS)
- 🧠 Built with Flask, LangChain, and OpenAI

---

## 🛠️ Tech Stack

| Layer        | Tools Used                       |
|--------------|-----------------------------------|
| Backend      | Python, Flask, LangChain, OpenAI |
| Frontend     | HTML, CSS, JavaScript            |
| Data         | `cards.json` (20+ Indian cards)  |

---

## 🧩 Folder Structure

```
credit_card_advisor/
├── app/                  # Backend logic
│   ├── main.py
│   ├── cards.json
├── static/               # CSS and JS files
│   ├── styles.css
│   └── script.js
├── templates/            # Frontend HTML
│   └── index.html
├── requirements.txt
├── .env
├── .gitignore
├── README.md             # Project description
```

---

## 📦 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/TejJeeney/Credit_Card-Advisor.git ///(.git- dd additionally)///
cd credit-card-advisor
```

### 2. Create virtual environment and install dependencies
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt  (few dependencies to installed on the go like dotenv)
```

### 3. Run the backend
```bash
cd app
python main.py
```

### 4. Open in browser
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)
***any other link if encountered do chck the files once again*** | Most commom error encountered by me.
---

## 🧪 Test Inputs
Example:
- Income: `65000`
- Spend: `15000`
- Benefits: `cashback, lounge access`

---

## 📸 Screenshots / Demo (Add Here)
![Screenshot](demo.png)

---

## 📝 Future Improvements
- ✅ Add user login system
- ✅ WhatsApp Integration via Twilio
- ✅ Admin Panel for card management
- ✅ Filter cards by banks or categories...
- and more as i work on it.

---

## 👨‍💻 Author
**Tejasva Gairi** | [GitHub](https://github.com/TejJeeney)
**It started as a project submission but now i will try to make it as awesome as i can***
---

## 📜 License
MIT License
