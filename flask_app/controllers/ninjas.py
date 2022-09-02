from flask_app import app
from flask import Flask, render_template, request, redirect, session 
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def make_ninja():
    all_dojos = Dojo.get_all()
    return render_template('create_ninja.html', all_the_dojos = all_dojos)

@app.route('/create_ninja', methods = ['POST'])
def create_ninjas():
    print(request.form)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'], 
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id'] #request.form is connected to my html
    }
    Ninja.create(data)
    return redirect('/dojos')