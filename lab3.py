from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', 'аноним')
    age = request.cookies.get('age', 'неизвестный возраст')
    name_color = request.cookies.get('name_color', 'black')
    return render_template('lab3/lab3.html', name=name, age=age, name_color=name_color)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect ('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 90
    else:
        price = 65

    if request.args.get('milk') == 'on':
        price += 40
    if request.args.get('sugar') == 'on':
        price += 20

    return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    # Получаем итоговую стоимость из параметров запроса
    price = request.args.get('price', '0')  # Значение по умолчанию — '0'
    return render_template('lab3/success.html', price=price)
    
@lab3.route('/lab3/settings')
def settings():
    # Получаем параметры из запроса
    color = request.args.get('color')
    bg_color = request.args.get('bg_color')
    font_size = request.args.get('font_size')
    font_style = request.args.get('font_style')
    
    # Создаем ответ для сохранения cookies
    resp = make_response(redirect('/lab3/settings'))

    # Устанавливаем cookies, если параметры были переданы
    if color:
        resp.set_cookie('color', color)
    if bg_color:
        resp.set_cookie('bg_color', bg_color)
    if font_size:
        resp.set_cookie('font_size', font_size)
    if font_style:
        resp.set_cookie('font_style', font_style)
    
    # Если параметры не переданы, получаем их значения из cookies
    color = color or request.cookies.get('color')
    bg_color = bg_color or request.cookies.get('bg_color')
    font_size = font_size or request.cookies.get('font_size')
    font_style = font_style or request.cookies.get('font_style')
    
    # Отображаем шаблон с применением сохраненных значений стилей
    resp = make_response(render_template('lab3/settings.html', color=color, bg_color=bg_color, font_size=font_size, font_style=font_style))
    return resp