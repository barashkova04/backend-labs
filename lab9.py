from flask import Flask, Blueprint, render_template, session

# Create a new Blueprint for lab8
lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')
