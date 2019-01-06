from flask import render_template, flash, redirect
from app import app, db
from app.forms import RSVPForm
from app.models import Guest


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index/<id>', methods=['GET', 'POST'])
def index(id=None):
    form = RSVPForm()
    return render_template('index.html', form=form, id=id)


@app.route('/rsvp', methods=['POST'])
def rsvp():
    form = RSVPForm()
    if form.validate_on_submit():
        guest = Guest(name=form.name.data, email=form.email.data,
                      attending=form.attending.data)
        db.session.add(guest)
        db.session.commit()
        return redirect('/success')
    flash('Please input a valid name, email, and attendance.')
    return redirect('/index#rsvp')


@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')
