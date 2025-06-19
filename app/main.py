
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI, RateLimitError
from dotenv import load_dotenv
import os
import re
import json

# THE FILE HERE IS FOR LOCAL RECOMMENDATION OF CARDS.
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# TEMPLATES_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'templates'))
# STATIC_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'static'))

# app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
# CORS(app)

# # BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# # TEMPLATES_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'templates'))
# # STATIC_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'static'))

# # app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
# # app = Flask(__name__, template_folder='../templates', static_folder='../static')
# # CORS(app)

# def load_cards():
#     with open("cards.json") as f:
#         return json.load(f)

# def parse_income_requirement(text):
#     match = re.search(r'Rs\.?\s?(\d+)([kKL]?)', text)
#     if match:
#         number, suffix = match.groups()
#         number = int(number)
#         if suffix.lower() == 'l':
#             return number * 100000
#         elif suffix.lower() == 'k':
#             return number * 1000
#         else:
#             return number
#     return 0

# def recommend_cards(user_input, cards):
#     filtered = []
#     for card in cards:
#         income_required = parse_income_requirement(card.get('eligibility', ''))
#         print(f"Checking card: {card['name']}, Required: {income_required}, User: {user_input['income']}")
#         if user_input['income'] >= income_required:
#             score = 0
#             if any(benefit.lower() in [perk.lower() for perk in card['perks']] for benefit in user_input['benefits']):
#                 score += 1
#             score += card['reward_rate'] * user_input['spend'] / 1000
#             filtered.append((card, score))
#     return sorted(filtered, key=lambda x: x[1], reverse=True)[:5]

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/recommend', methods=['POST'])
# def recommend():
#     user_data = request.json
#     cards = load_cards()
#     recommendations = recommend_cards(user_data, cards)
#     result = []
#     for card, score in recommendations:
#         reward = user_data['spend'] * card['reward_rate'] * 12
#         result.append({
#             'name': card['name'],
#             'image': card['image'],
#             'reasons': card['perks'],
#             'estimated_rewards': f"Rs. {reward:.2f}/year"
#         })
#     return jsonify(result)


# Uses the API key and uses the integrted OPENAI model to use. 
# AI-Credits will be required to use the Integrated AI in the predictor. 
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ No OPENAI_API_KEY found in .env file")

client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__, template_folder='../templates', static_folder='../static')
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    income = data.get("income")
    spend = data.get("spend")
    benefits = ", ".join(data.get("benefits", []))

    prompt = (
        f"You are an expert credit card advisor. A user has a monthly income of Rs. {income}, "
        f"spends around Rs. {spend} per month, and prefers benefits like: {benefits}. "
        f"Suggest 5 credit cards available in India, each with name, estimated_rewards (in Rs/year), "
        f"and one-line reason. Format as JSON list with fields: name, reason, estimated_rewards."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use gpt-4 only if your key supports it
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        reply = response.choices[0].message.content
        return jsonify({"ai_response": reply})

    except RateLimitError:
        return jsonify({"error": "❌ OpenAI quota exceeded. Check your usage or billing. Kindly yaad rakhe-\"It is just from a free account\" :)"}), 429

    except Exception as e:
        return jsonify({"error": f"❌ Unexpected error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

