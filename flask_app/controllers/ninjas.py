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
    show_ninja = Ninja.create(data)
    return redirect(f'/read/{request.form["dojo_id"]}') #this is also showing tuple index out of range

@app.route('/delete/<int:id>', methods = ["POST"]) #this is to delete user
def delete(id):
    data = {
        'id' : id
    }
    Ninja.delete(data)
    return redirect(f'/read/{request.form["dojo_id"]}')
    #need to use hidden inputs 

    #this deletes but I keep getting tuple index out of range

    # a_dojo = Dojo.get_dojo_ninjas
    # return redirect(f'/read/{a_dojo}') 
    # Above I get URL not found
    # 
    

@app.route('/edit/<int:id>') #this is the edit page/form
def edit(id):
    data = {
        'id' : id
    }
    a_ninja = Ninja.get_one(data)
    return render_template('edit.html', one_ninja = a_ninja)

@app.route('/update/<int:id>', methods = ['POST']) #this is to actually edit the user
def update(id):
    data = {
        'id' : id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.update(data)
    return redirect('/')
    #use hidden input for redirect? 