import os
from flask import Flask, url_for
from os import path
from flask_sqlalchemy import SQLAlchemy
from db import db
from db.models import users
from flask_login import LoginManager

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9

app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE']=os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'sveta_barashkova_orm'
    db_user = 'sveta_barashkova_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "sveta_barashkova_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)

@app.errorhandler(404)
def not_found(err):
    path=url_for("static", filename='lab1/err.jpeg')
    return '''
    <!doctype html>
<html>
    <body style="background-color: red">
        <h1 style="text-align: center;">ТАКОЙ СТРАНИЦЫ НЕТ!!!<h1>
        <p style="text-align: center;"><img src="''' + path + '''" width="700" style="padding: 40px;"></p>
    </body>
</html>
''', 404

@app.errorhandler(400)
def not_found400(err):
    return '''
    <!doctype html>
<html>
    <body style="background-color: red">
        <h1 style="text-align: center;">Некорректный запрос. Будьте внимательнее)<h1>
    </body>
</html>
''', 400

@app.errorhandler(401)
def not_found401(err):
    return '''
    <!doctype html>
<html>
    <body style="background-color: red">
        <h1 style="text-align: center;">Вы не авторизованы!<h1>
    </body>
</html>
''', 401

@app.errorhandler(403)
def not_found403(err):
    return '''
<!doctype html>
<html>
    <body style="background-color: red">
        <h1 style="text-align: center;">Доступ к ресурсу запрещен! >:(<h1>
    </body>
</html>
''', 403

@app.errorhandler(405)
def not_found405(err):
    return '''
    <!doctype html>
<html>
    <body style="background-color: red">
        <h1 style="text-align: center;">Метод HTTP не разрешен веб-сервером для запрошенного URL-адреса<h1>
    </body>
</html>
''', 405

@app.errorhandler(418)
def not_found418(err):
    return '''
    <!doctype html>
<html>
    <body style="background-color: red">
        <h1 style="text-align: center;">Время ожидания сервером передачи от клиента истекло<h1>
    </body>
</html>
''', 418

@app.errorhandler(500)
def not_found500(err):
    return '''
    <!doctype html>
<html>
    <body style="background-color: pink">
        <h1 style="text-align: center;">Внутренняя ошибка сервера(((<h1>
    </body>
</html>
''', 500

@app.route("/")
def start():
    path = url_for("static", filename='lab1.css')
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <link rel="stylesheet" href="''' + path + '''">
</head>
<body>
    <header>
        НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
    </header>

    <main>
        <h1>Лабораторные работы по WEB-программированию</h1>
        
        <div>
            <ol>
                <li>
                    <a href="/lab1">Лабораторная работа 1</a>
                </li>

                <li>
                    <a href="/lab2">Лабораторная работа 2</a>
                </li>

                <li>
                    <a href="/lab3">Лабораторная работа 3</a>
                </li>
                <li>
                    <a href="/lab4">Лабораторная работа 4</a>
                </li>
                <li>
                    <a href="/lab5">Лабораторная работа 5</a>
                </li>
                <li>
                    <a href="/lab6">Лабораторная работа 6</a>
                </li>
                <li>
                    <a href="/lab7">Лабораторная работа 7</a>
                </li>
                <li>
                    <a href="/lab8">Лабораторная работа 8</a>
                </li>
                <li>
                    <a href="/lab9">Лабораторная работа 9</a>
                </li>

            </ol>
        </div>
    </main>

    <footer>
        <hr>
        &copy; Барашкова Светлана, ФБИ-22, 2 курс, 2024
    </footer>
</body>
</html>
'''
