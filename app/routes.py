from flask import render_template, redirect, url_for, request, session

from app import app
from app.ai import get_output


@app.route('/')
def home():
    return redirect(url_for('chat'))


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    print(session.get('history', None))
    if 'history' not in session.keys():
        session['history'] = []
    if request.method == 'POST':
        t = [request.form['question']]
        out = get_output(request.form["question"], session['topic'] if 'topic' in session.keys() else 'electrodynamics')
        print(out)
        t.append(out)
        session['history'] = [t, *session['history']]
    return render_template('base.html', tab='chat', history=session['history'])


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'history' not in session.keys():
        session['history'] = []
    return render_template('base.html', tab='quiz', history=session['history'])


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'history' not in session.keys():
        session['history'] = []
    if request.method == 'POST':
        session['topic'] = request.form['topic']
    return render_template('base.html', tab='admin', history=session['history'])
