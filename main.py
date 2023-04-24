from flask import Flask, render_template
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/member')
def member():
    print('+')
    list_members = []
    with open('templates/crew_members.json', "r", encoding='utf8') as f:
        lst = json.loads(f.read())
    return render_template('galery.html', lst=lst['members'])


if __name__ == '__main__':
    app.run(port=8080,  host='127.0.0.1')
