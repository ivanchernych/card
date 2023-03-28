import flask

app = flask.Flask(__name__)


@app.route('/')
@app.route('/auto_answer')
def auto_answer():
    param = {
        'title': 'Анкета',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': 'True'
    }
    return flask.render_template('auto_answer.html', **param)


if __name__ == '__main__':
    app.run(port=8080,  host='127.0.0.1')
