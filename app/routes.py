from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'JC'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'example'},
            'body': 'dscription'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('hola {}, datos guardados = {}'.format( form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)
    
@app.route("/<name>")
def user(name):
    return f"hello {name}"

@app.route("/admin")
def admin():
   
    return render_template('admin.html')
    


if __name__ == "__main__":
    app.debug = True
    app.run(debug = True)