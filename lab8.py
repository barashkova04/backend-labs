from flask import Flask, Blueprint, render_template, session

# Create a new Blueprint for lab8
lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8')
def lab():
    return render_template('lab8/lab8.html', login=session.get('login'))

@lab8.route('/lab8/login')
def login():
    return render_template('lab8/login.html')

@lab8.route('/lab8/register')
def register():
    return render_template('lab8/register.html')

@lab8.route('/lab8/articles')
def articles():
    return render_template('lab8/articles.html')

@lab8.route('/lab8/create')
def create_article():
    return render_template('lab8/create.html')

# Create the main Flask application
app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(lab8)

if __name__ == '__main__':
    app.run(debug=True)