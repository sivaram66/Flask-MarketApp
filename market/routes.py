from market import app
from flask import render_template ,redirect, url_for, flash
from market.models import Item,User
from market.forms import RegisterForm, LoginForm
from market import db #directly imported becoz it is in __init__ file
from flask_login import login_user


@app.route('/')
@app.route('/Home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register',methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():#it checks whether the user click on the submit button 
        user_to_create =User(username=form.username.data,
                             email_address=form.email_address.data,
                             password = form.password1.data) #This password goes to the @password.setter(before create pasword.setter use password_hash only)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors !={}: #if there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}',category='danger')

    return render_template('register.html', form=form)

@app.route('/login',methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():#here 2 functions are going first it check the information is valid and also hit this conditional when we click on submit button
        attempted_user =User.query.get(form.username.data).first() #this statement going to filter out ther User by provided username
        if attempted_user and attempted_user.check_password_correction(attempted_password = form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}',category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match!',category='danger')
    return render_template('login.html',form =form)