from collections import namedtuple

import requests

import flask_sqlalchemy

from flask import Flask, render_template, redirect, url_for, request


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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета претендента</h1>
                            <h3 align="center">на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" aria-describedby="surnamelHelp" placeholder="Введите фамилию" name="surname">

                                    <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="eduSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="edu">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Выше среднего</option>
                                          <option>Супер!</option>
                                        </select>
                                     </div>
                                        <label for="eduSelect">Какие у Вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof" name="prof">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof1">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof2">
                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof3">
                                        <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof4">
                                        <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof5">
                                        <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof6">
                                        <label class="form-check-label" for="acceptRules">Врач</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof7">
                                        <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                    </div>

                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['edu'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        print(request.form['prof'])
        print(request.form['prof1'])
        print(request.form['prof2'])
        print(request.form['prof3'])
        print(request.form['prof4'])
        print(request.form['prof5'])
        print(request.form['prof6'])
        print(request.form['prof7'])
        return "Форма отправлена"


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    messages.append(Message(text, tag))

    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run()

