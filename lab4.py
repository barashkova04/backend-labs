from flask import Blueprint, render_template, request, redirect, session
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)

    if x2 == 0:
        return render_template('lab4/div.html', error='Деление на ноль невозможно! Пожалуйста, введите другое значение.')
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)
    

# Страница суммирования
@lab4.route('/lab4/add-form')
def add_form():
    return render_template('lab4/add-form.html')

@lab4.route('/lab4/add', methods=['POST'])
def add():
    x1 = request.form.get('x1') or 0
    x2 = request.form.get('x2') or 0
    result = int(x1) + int(x2)
    return render_template('lab4/add.html', x1=x1, x2=x2, result=result)


# Страница умножения
@lab4.route('/lab4/mul-form')
def mul_form():
    return render_template('lab4/mul-form.html')

@lab4.route('/lab4/mul', methods=['POST'])
def mul():
    x1 = request.form.get('x1') or 1
    x2 = request.form.get('x2') or 1
    result = int(x1) * int(x2)
    return render_template('lab4/mul.html', x1=x1, x2=x2, result=result)

# Страница вычитания
@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')

@lab4.route('/lab4/sub', methods=['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', error='Оба поля должны быть заполнены!')
    result = int(x1) - int(x2)
    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)


# Страница возведения в степень
@lab4.route('/lab4/pow-form')
def pow_form():
    return render_template('lab4/pow-form.html')

@lab4.route('/lab4/pow', methods=['POST'])
def power():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/pow.html', error='Оба поля должны быть заполнены!')
    if int(x1) == 0 and int(x2) == 0:
        return render_template('lab4/pow.html', error='0 в степени 0 неопределено!')
    result = int(x1) ** int(x2)
    return render_template('lab4/pow.html', x1=x1, x2=x2, result=result)


tree_count = 0

@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    # Обработка операций с проверкой на границы
    if operation == 'cut' and tree_count > 0:
        tree_count -= 1
    elif operation == 'plant' and tree_count < 10:
        tree_count += 1

    return redirect('/lab4/tree')

users = [
    {'login': 'alex', 'password': '123', 'name': 'Alexander Petrov', 'gender': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Bob Johnson', 'gender': 'male'},
    {'login': 'ivan', 'password': '000', 'name': 'Ivan Ivanov', 'gender': 'male'},
    {'login': 'Tramp', 'password': '2024', 'name': 'Donald Trump', 'gender': 'male'}
]


@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            user = next((user for user in users if user['login'] == login), None)
            name = user['name'] if user else login
        else:
            authorized = False
            login = ''
            name = ''
        return render_template("lab4/login.html", authorized=authorized, name=name, login=login)
    
    login = request.form.get('login')
    password = request.form.get('password')
    
    # Проверка на пустые значения логина и пароля
    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    if not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)

    # Проверка правильности логина и пароля
    user = next((user for user in users if user['login'] == login and user['password'] == password), None)
    if user:
        session['login'] = login
        return redirect('/lab4/login')
    
    # Обработка неверных данных авторизации
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)


@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    message = ""
    
    if request.method == 'POST':
        temp = request.form.get('temperature')
        
        # Проверка на пустое значение
        if temp is None or temp.strip() == '':
            message = "Ошибка: не задана температура"
            return render_template("lab4/fridge.html", message=message)
        
        try:
            # Преобразуем температуру в число
            temp = float(temp)
        except ValueError:
            message = "Ошибка: температура должна быть числом"
            return render_template("lab4/fridge.html", message=message)
        
        # Проверка диапазонов температуры
        if temp < -12:
            message = "Не удалось установить температуру — слишком низкое значение"
        elif temp > -1:
            message = "Не удалось установить температуру — слишком высокое значение"
        elif -12 <= temp <= -9:
            message = f"Установлена температура: {temp}°С ❄️❄️❄️"
        elif -8 <= temp <= -5:
            message = f"Установлена температура: {temp}°С ❄️❄️"
        elif -4 <= temp <= -1:
            message = f"Установлена температура: {temp}°С ❄️"
        else:
            message = f"Установлена температура: {temp}°С"
        
        return render_template("lab4/fridge.html", message=message)

    return render_template("lab4/fridge.html")