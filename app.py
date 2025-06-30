from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# 18 Reasons
reasons = [
    "You light up my world like nobody else",
    "Your smile makes everything better",
    "You believe in me even when I doubt myself",
    "You're beautiful inside and out",
    "You're my safe space",
    "You make every moment special",
    "Your laugh is my favorite sound",
    "You're incredibly talented",
    "You understand me like no one else",
    "You’re my biggest supporter",
    "You inspire me every day",
    "You’re my peace and my chaos",
    "You're thoughtful and kind",
    "You make life exciting",
    "You always know how to make me smile",
    "You're my heart's favorite person",
    "You're my best friend",
    "You are my forever and always"
]

@app.route('/')
def home():
    now = datetime.now()
    birthday = datetime(now.year, 7, 18)
    if now > birthday:
        birthday = datetime(now.year + 1, 7, 18)
    delta = birthday - now
    return render_template('index.html', countdown=delta.days, reasons=reasons)

if __name__ == '__main__':
    app.run(debug=True)
