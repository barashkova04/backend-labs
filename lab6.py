from flask import Blueprint, render_template, request, redirect, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
import sqlite3
from os import path

lab6 = Blueprint('lab6', __name__)

# Функция для подключения к базе данных
def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='svetlana_barashkova_knowledge_base',
            user='svetlana_barashkova_knowledge_base',
            password='123'
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

    return conn, cur

# Функция для закрытия соединения с базой данных
def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@lab6.route('/lab6/')
def lab():
    return render_template('lab6/lab6.html', login=session.get('login'))

@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data.get('id')  # Используем get для безопасного извлечения id
    
    if data['method'] == 'info':
        conn, cur = db_connect()
        cur.execute("SELECT number, tenant, price FROM offices")
        offices = cur.fetchall()
        db_close(conn, cur)
        
        return {
            'jsonrpc': '2.0',
            'result': offices,
            'id': id
        }
    
    login = session.get('login')
    if not login:
        return {
            'jsonrpc': '2.0',
            'error': {
                'code': 1,
                'message': 'Unauthorized'
            },
            'id': id
        }
    
    if data['method'] == 'booking':
        office_number = data['params']
        conn, cur = db_connect()
        cur.execute("SELECT tenant FROM offices WHERE number = %s", (office_number,))
        office = cur.fetchone()
        
        if office:
            if office['tenant'] is not None:  # Проверяем, что поле tenant не None
                db_close(conn, cur)
                return {
                    'jsonrpc': '2.0',
                    'error': {
                        'code': 2,
                        'message': 'Already booked'
                    },
                    'id': id
                }
            
            cur.execute("UPDATE offices SET tenant = %s WHERE number = %s", (login, office_number))
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'result': 'success',
                'id': id
            }

    if data['method'] == 'cancellation':
        office_number = data['params']
        conn, cur = db_connect()
        cur.execute("SELECT tenant FROM offices WHERE number = %s", (office_number,))
        office = cur.fetchone()
        
        if office:
            if office['tenant'] is None:  # Проверяем, что поле tenant равно None
                db_close(conn, cur)
                return {
                    'jsonrpc': '2.0',
                    'error': {
                        'code': 3,
                        'message': 'Office is not booked'
                    },
                    'id': id
                }
            if office['tenant'] != login:
                db_close(conn, cur)
                return {
                    'jsonrpc': '2.0',
                    'error': {
                        'code': 4,
                        'message': 'You cannot cancel someone else\'s booking'
                    },
                    'id': id
                }
            
            cur.execute("UPDATE offices SET tenant = NULL WHERE number = %s", (office_number,))
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'result': 'success',
                'id': id
            }

    return {
        'jsonrpc': '2.0',
        'error': {
            'code': -32601,
            'message': 'Method not found'
        },
        'id': id
    }

@lab6.route('/lab6/logout')
def logout():
    session.pop('login', None)
    return redirect('/lab6/')