from flask import render_template, redirect, url_for, request

from app import app


@app.route('/')
def home():
    return redirect(url_for('chat'))


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    print("test", request.method)
    if request.method == 'POST':
        print(request.form)
    return render_template('base.html', tab='chat')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    return render_template('base.html', tab='quiz')
