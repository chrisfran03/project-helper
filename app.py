from flask import Flask, request, render_template
from openai import OpenAI
import os
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__)

# Replace 'your-api-key' with your actual OpenAI API key
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        chat_response = response.choices[0].message.content
        return render_template('index.html', user_input=user_input, chat_response=chat_response)
    return render_template('index.html', user_input='', chat_response='')


if __name__ == '__main__':
    app.run(debug=True)
