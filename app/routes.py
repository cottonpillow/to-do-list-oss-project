from app import app
from flask import render_template, redirect, url_for, request
from app.models import Task

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form['task']
        new_task = Task(name=task_name)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))
