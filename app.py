from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы :'(", 404

@app.route("/")
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