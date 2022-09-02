from flask_app import app
from flask import Flask, render_template, request, redirect, session 
from flask_app.models.dojo import Dojo


@app.route('/dojos')
def dojo():
    all_dojos = Dojo.get_all()
    return render_template('create.html', all_the_dojos = all_dojos)

@app.route('/dojos/new', methods = ['POST'])
def create_dojo():
    print(request.form)
    data = {
        'name': request.form['name'] #request.form is connected to my html
    }
    Dojo.create(data)
    return redirect('/dojos')