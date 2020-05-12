from collections import namedtuple
import requests
import flask_sqlalchemy

from flask import Flask, render_template, redirect, url_for, request


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    profil = {}
    profil['title'] = 'Анкета'
    profil['surname'] = 'Watny'
    profil['name'] = 'Mark'
    profil['education'] = 'выше среднего'
    profil['profession'] = 'штурман марсохода'
    profil['sex'] = 'male'
    profil['motivation'] = 'Всегда мечтал застрять на Марсе!'
    profil['ready'] = 'True'
    return render_template('auto_answer.html', **profil)


class MapParams(object):
    def __init__(self):
        self.lat = 61.665279
        self.lon = 50.813492
        self.zoom = 16  # Масштаб карты на старте. Изменяется от 1 до 19
        self.type = "map"  # Другие значения "sat", "sat,skl"

    # Преобразование координат в параметр ll, требуется без пробелов, через запятую и без скобок
    def ll(self):
        return str(self.lon) + "," + str(self.lat)


# Создание карты с соответствующими параметрами.
def load_map(mp):
    map_request = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}".format(ll=mp.ll(), z=mp.zoom, type=mp.type)
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запись полученного изображения в файл.
    map_file = "1.jpg"

class LoginForm(FlaskForm):
    userid = StringField('Id астронавта', validators=[DataRequired()])
    password_1 = PasswordField('Пароль астронавта', validators=[DataRequired()])
    cap_id = StringField('Id капитана', validators=[DataRequired()])
    password_2 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login1', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)
    def main():
    global_init(input())

    session = create_session()

    for job in session.query(Jobs).filter((Jobs.work_size < 20),
                                          Jobs.is_finished == 0):
        print(job)
    
    
app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def main():
    return render_template('main.html', messages=messages)


@app.route('/otzivi', methods=['GET'])
def main1():
    return '''<img src="/static/img/1.jpg" alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    messages.append(Message(text, tag))

    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run()
