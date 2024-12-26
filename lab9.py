from flask import Blueprint, render_template, request, redirect, url_for

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9')
def main():
    return render_template('lab9/index.html')

@lab9.route('/lab9/name', methods=['GET', 'POST'])
def form_name():
    if request.method == 'POST':
        name = request.form.get('name')  # Используйте get для безопасного получения значения
        if not name:  # Проверка на пустое значение
            return render_template('lab9/form_name.html', error="Имя не может быть пустым")
        return redirect(url_for('lab9.form_age', name=name))
    return render_template('lab9/form_name.html')

@lab9.route('/lab9/age', methods=['GET', 'POST'])
def form_age():
    name = request.args.get('name')
    if request.method == 'POST':
        age = request.form.get('age')  # Используйте get для безопасного получения значения
        if not age:  # Проверка на пустое значение
            return render_template('lab9/form_age.html', name=name, error="Возраст не может быть пустым")
        try:
            age = int(age)  # Преобразование в целое число
        except ValueError:
            return render_template('lab9/form_age.html', name=name, error="Возраст должен быть числом")
        
        return redirect(url_for('lab9.form_gender', name=name, age=age))
    return render_template('lab9/form_age.html', name=name)

@lab9.route('/lab9/gender', methods=['GET', 'POST'])
def form_gender():
    name = request.args.get('name')
    age = request.args.get('age')
    if request.method == 'POST':
        gender = request.form.get('gender')  # Используйте get для безопасного получения значения
        if not gender:  # Проверка на пустое значение
            return render_template('lab9/form_gender.html', name=name, age=age, error="Пол не может быть пустым")
        return redirect(url_for('lab9.form_preference', name=name, age=age, gender=gender))
    return render_template('lab9/form_gender.html', name=name, age=age)

@lab9.route('/lab9/preference', methods=['GET', 'POST'])
def form_preference():
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    if request.method == 'POST':
        preference = request.form.get('preference')  # Используйте get для безопасного получения значения
        if not preference:  # Проверка на пустое значение
            return render_template('lab9/form_preference.html', name=name, age=age, gender=gender, error="Предпочтение не может быть пустым")
        return redirect(url_for('lab9.form_sub_preference', name=name, age=age, gender=gender, preference=preference))
    return render_template('lab9/form_preference.html', name=name, age=age, gender=gender)

@lab9.route('/lab9/sub_preference', methods=['GET', 'POST'])
def form_sub_preference():
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    preference = request.args.get('preference')
    if request.method == 'POST':
        sub_preference = request.form.get('sub_preference')  # Используйте get для безопасного получения значения
        if not sub_preference:  # Проверка на пустое значение
            return render_template('lab9/form_sub_preference.html', name=name, preference=preference, error="Подпредпочтение не может быть пустым")
        return redirect(url_for('lab9.greeting', name=name, age=age, gender=gender, preference=preference, sub_preference=sub_preference))
    return render_template('lab9/form_sub_preference.html', name=name, preference=preference)

@lab9.route('/lab9/greeting', methods=['GET', 'POST'])
def greeting():
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    preference = request.args.get('preference')
    sub_preference = request.args.get('sub_preference')

    if gender == 'male':
        gender_text = "чтобы ты быстро вырос, был умным"
    else:
        gender_text = "чтобы ты быстро выросла, была умной"

    if preference == 'вкусное':
        if sub_preference == 'сладкое':
            gift = "мешочек конфет"
            image = "static/images/candies.jpg"  # Путь к изображению конфет
        else:
            gift = "тарелку сытного"
            image = "static/images/hearty_food.jpg"  # Путь к изображению сытной еды
    else:
        if sub_preference == 'красивое':
            gift = "красивый подарок"
            image = "static/images/beautiful_gift.jpg"  # Путь к изображению красивого подарка
        else:
            gift = "что-то полезное"
            image = "static/images/useful_gift.jpg"  # Путь к изображению полезного подарка

    return render_template('lab9/greeting.html', name=name, gender_text=gender_text, gift=gift, image=image)