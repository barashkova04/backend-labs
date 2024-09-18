from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    path=url_for("static", filename='err.jpeg')
    return '''
    <!doctype html>
<html>
    <body style="background-color: red">
        <h1 style="text-align: center;">ТАКОЙ СТРАНИЦЫ НЕТ!!!<h1>
        <p style="text-align: center;"><img src="''' + path + '''" width="700" style="padding: 40px;"></p>
    </body>
</html>
''', 404

@app.route("/")

@app.route("/index")
def index():
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
@app.route("/lab1")
def lab1():
    path = url_for("static", filename='lab1.css')
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Лабораторная 1</title>
    <link rel="stylesheet" href="''' + path + '''">
</head>
<body>
    <header>
        НГТУ, ФБ, WEB-программирование, часть 2.
    </header>

    <main>
        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>

        <a href="/">ссылка на меню</a>
    </main>

    <footer>
        <hr>
        &copy; Барашкова Светлана, ФБИ-22, 2 курс, 2024
    </footer>
</body>
</html>
'''

@app.route("/lab1/web")
def web():
    return """<!doctype html> \
        <html> \
           <body> \
               <h1>web-сервер на falsk</h1> \
           <body>\
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
        }

@app.route("/lab1/author")
def author():
    name = "Барашкова Светлана Константиновна"
    group = "ФБИ-22"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """+name+"""<p>
                <p>Группа: """+group+"""<p>
                <p>Факультет: """+faculty+"""<p>
                <a href="/web">web</a>
            <body>
        <html>"""

@app.route('/lab1/dub')
def dub():
    path = url_for("static", filename='dub.jpeg')
    path2 = url_for("static", filename='lab1.css')
    return '''
<!doctype html>
<html>
    <head>
    <link rel="stylesheet" href="''' + path2 + '''">
    </head>
    <body>
        <h1>Дуб<h1>
        <img src="''' + path + '''">
    </body>
</html>
'''

count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: '''+ str(count) +'''
        <a href="/lab1/counter0">очистка</a>
    </body>
</html>
'''

count2 = 0
@app.route('/lab1/counter0')
def counter0():
    global count2
    count2 += 1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: '''+ str(count2) +'''
    </body>
</html>
'''

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно<h1>
        <div><i>что-то создано!<i><div>
    </body>
</html>
''', 201