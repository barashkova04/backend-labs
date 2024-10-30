from flask import Blueprint, url_for, redirect, jsonify, abort, render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a')
def a():
    return 'без слэша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'


flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка', 'георгин']
@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "такого цветка нет!", 404
    else:
        return "цветок:" + flower_list[flower_id]


@lab2.route('/lab2/add_flower/<name>')
def add_flower(name=None):
    if name is None:
        abort(400, description="Вы не задали имя цветка")
    
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название прекрасного цветка: {name}</p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    <a href="{url_for('lab2.list_flowers')}">Посмотреть все цветы</a>
    </body>
</html>
'''


@lab2.route('/lab2/flowers/')
def list_flowers():
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Список всех цветов</h1>
    <p>Всего цветов: {len(flower_list)}</p>
    <ul>
        {''.join(f'<li>{flower}</li>' for flower in flower_list)}
    </ul>
    <a href="{url_for('lab2.clear_flowers')}">Очистить список цветов</a>
    </body>
</html>
'''


@lab2.route('/lab2/flowers/<int:flower_id>')
def flower_detail(flower_id):
    if flower_id < 0 or flower_id >= len(flower_list):
        abort(404)
    
    flower_name = flower_list[flower_id]
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Цветок #{flower_id + 1}</h1>
    <p>Название цветка: {flower_name}</p>
    <a href="{url_for('lab2.list_flowers')}">Вернуться к списку всех цветов</a>
    </body>
</html>
'''


@lab2.route('/lab2/clear_flowers/')
def clear_flowers():
    flower_list.clear()
    return redirect(url_for('lab2.list_flowers'))


@lab2.route('/lab2/example')
def example():
    name = 'Светлана Барашкова'
    num_lab = '2'
    clas='3'
    gr='ФБИ-22'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321},
    ]
    return render_template('lab2/example.html', name=name, num_lab=num_lab, clas=clas, group=gr, fruits=fruits)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2/lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase = phrase)


#2 задание
@lab2.route('/lab2/calc/<int:a>/<int:b>', methods=['GET'])
def calculate(a, b):
    results = {
        'sum': a + b,
        'difference': a - b,
        'product': a * b,
        'quotient': a / b if b != 0 else 'undefined',
        'power': a ** b }
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Результаты вычислений</title>
    </head>
    <body>
        <h1>Результаты для {a} и {b}</h1>
        <pre>
            {a} + {b} = {results['sum']}
            {a} - {b} = {results['difference']}
            {a} * {b} = {results['product']}
            {a} / {b} = {results['quotient']}
            {a} ** {b} = {results['power']}
        </pre>
    </body>
    </html>
    """


@lab2.route('/lab2/calc/')
def default_calc():
    return redirect(url_for('calculate', a=1, b=1))


@lab2.route('/lab2/calc/<int:a>')
def redirect_a(a):
    return redirect(url_for('calculate', a=a, b=1))


@lab2.route('/lab2/book')
def book():
    return render_template('lab2/book.html')


# Данные о ягодах
berries = [
    {
        "name": "Клубника",
        "description": "Сочная и сладкая ягода, популярная в летний сезон.",
        "image": "lab2/strawberry.jpeg"
    },
    {
        "name": "Черника",
        "description": "Полезная ягода с множеством антиоксидантов.",
        "image": "lab2/blueberry.jpeg"
    },
    {
        "name": "Малина",
        "description": "Ароматная ягода, часто используется в десертах.",
        "image": "lab2/raspberry.jpeg"
    },
    {
        "name": "Ежевика",
        "description": "Темная, сочная и насыщенная по вкусу ягода.",
        "image": "lab2/blackberry.jpeg"
    },
    {
        "name": "Клюква",
        "description": "Кислая ягода, известная своими лечебными свойствами.",
        "image": "lab2/cherry.jpeg"
    }
]

@lab2.route('/lab2/berry')
def show_berries():
    return render_template('lab2/index.html', items=berries)

if __name__ == '__main__':
    lab2.run(debug=True)