from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Teacher

@app.route('/')
def index():
    teachers = Teacher.query.all()
    return render_template('index.html', teachers=teachers)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        subject = request.form['subject']
        time = request.form['time']
        if name and id and subject and time:
            new_teacher = Teacher(name=name, id=id, subject=subject, time=time)
            db.session.add(new_teacher)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user = Teacher.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('delete_user.html')