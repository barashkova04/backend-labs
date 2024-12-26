from flask import Flask, Blueprint, render_template, request, redirect
from db import db
from db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8')
def lab():
    # Удаляем login из session и используем current_user
    return render_template('lab8/lab8.html', login=current_user.login if current_user.is_authenticated else 'Anonymous')

@lab8.route('/lab8/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab8/login.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')

    user = users.query.filter_by(login=login_form).first()

    if user:
        if check_password_hash(user.password, password_form):
            login_user(user, remember=False)
            return redirect('/lab8')
    
    return render_template('/lab8/login.html',
                           error='Ошибка входа: логин или пароль неверны')

@lab8.route('/lab8/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')

    login_exists = users.query.filter_by(login=login_form).first()
    if login_exists:
        return render_template('lab8/register.html',
                               error='Такой пользователь уже есть')
    
    password_hash = generate_password_hash(password_form)
    new_user = users(login=login_form, password=password_hash)
    db.session.add(new_user)
    db.session.commit()

    # Автоматический логин после регистрации
    login_user(new_user, remember=False)

    return redirect('/lab8')

@lab8.route('/lab8/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab8')

@lab8.route('/lab8/create', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'POST':
        title = request.form.get('title')
        article_text = request.form.get('content')  # Измените на 'content', если это поле в форме

        # Создание новой статьи
        new_article = articles(
            login_id=current_user.id,  # Используйте login_id для связи с текущим пользователем
            title=title,
            article_text=article_text,
            is_favorite=False,  # Установите значение по умолчанию
            is_public=True,     # Установите значение по умолчанию
            likes=0             # Начальное количество лайков
        )
        db.session.add(new_article)
        db.session.commit()

        return redirect('/lab8/articles')  # Перенаправление на список статей

    return render_template('lab8/create.html')

@lab8.route('/lab8/articles')
@login_required
def article_list():
    all_articles = articles.query.all()  # Получение всех статей из базы данных
    return render_template('lab8/articles.html', articles=all_articles)

@lab8.route('/lab8/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    article = articles.query.get_or_404(article_id)  # Получаем статью по ID

    if request.method == 'POST':
        article.title = request.form.get('title')
        article.article_text = request.form.get('content')

        db.session.commit()  # Сохраняем изменения в базе данных
        return redirect('/lab8/articles')  # Перенаправление на список статей

    return render_template('lab8/edit.html', article=article)  # Отображаем форму редактирования

@lab8.route('/lab8/delete/<int:article_id>', methods=['POST'])
@login_required
def delete_article(article_id):
    article = articles.query.get_or_404(article_id)  # Получаем статью по ID
    db.session.delete(article)  # Удаляем статью
    db.session.commit()  # Сохраняем изменения в базе данных
    return redirect('/lab8/articles')  # Перенаправление на список статей