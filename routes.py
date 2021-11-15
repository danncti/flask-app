from app import app, db
from flask import render_template, redirect, url_for
from models import Task
from datetime import datetime

import forms

@app.route('/')
@app.route("/index")
def index():
    tasks = Task.query.all()
    # return render_template('index.html', current_title = 'Custom Title')
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        try:
            db.session.add(t)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        # finally:
        #     session.close()
        return redirect(url_for('index'))
        # return render_template('add.html', form=form,
        #                        title=form.title.data)

    return render_template('add.html', form=form)