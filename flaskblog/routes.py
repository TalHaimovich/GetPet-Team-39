from flask import render_template, url_for, flash, redirect, send_from_directory, abort, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, AsosRegistrationForm, BusRegistrationForm, PostForm,UpdateAccountForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required, login_manager
from werkzeug.utils import secure_filename
import os
import uuid
from flask import Flask, render_template, session
from flask_login import current_user

<<<<<<< HEAD



=======
>>>>>>> eb2ff8d7f64d17d6c978c00431268d0407104dca
@app.route('/images/<path:path>')
def serve_images(path):
    return send_from_directory('images', path)


@app.route('/uploads/<path:path>')
def serve_uploads(path):
    return send_from_directory('uploads', path)


@app.route("/")
@app.route("/home")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('homelogged'))
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    return render_template('register.html', title='Register')


def get_and_save_image(f):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    unique_filename = f'{uuid.uuid4()}_{f.filename}'
    filename = secure_filename(unique_filename)
    f.save(os.path.join(base_dir, 'flaskblog', 'uploads', filename))
    return filename


@app.route("/registeruser", methods=['GET', 'POST'])
def registeruser():
    if current_user.is_authenticated:
        return redirect(url_for('homelogged'))

    form = RegistrationForm()
    if form.validate_on_submit():
        f = form.image.data
        filename = None
        if f:
            filename = get_and_save_image(f)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password, image=filename)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account have been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('registeruser.html', title='RegisterUser', form=form)


@app.route("/registerbus", methods=['GET', 'POST'])
def registerbus():
    if current_user.is_authenticated:
        return redirect(url_for('homelogged'))
    form = BusRegistrationForm()

    if form.validate_on_submit():
        f = form.image.data
        filename = None
        if f:
            filename = get_and_save_image(f)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password, bus_id=form.bus_id.data,
                    is_bus=True, image=filename)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account have been created! You are now able to log in', 'success')
        return redirect(url_for('login'))

    return render_template('registerbus.html', title='RegisterBussines', form=form)


@app.route("/registerasos", methods=['GET', 'POST'])
def registerasos():
    if current_user.is_authenticated:
        return redirect(url_for('homelogged'))
    form = AsosRegistrationForm()

    if form.validate_on_submit():
        f = form.image.data
        filename = None
        if f:
            filename = get_and_save_image(f)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password, address=form.address.data,
                    is_asos=True, image=filename)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account have been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('registerasos.html', title='RegisterAssosition', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homelogged'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('homelogged'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/homelogged", methods=['GET', 'POST'])
@login_required
def homelogged():
    form = PostForm()
    if current_user.is_bus:
        form.type.choices = ['product','discount']
    
    if form.validate_on_submit():
        user_id = current_user.id
        f = form.image.data
        filename = None
        if f:
            filename = get_and_save_image(f)
        selected_type = form.type.data

        is_adopt = selected_type == 'adopt'
        is_foster = selected_type == 'foster'
        is_product = selected_type == 'product'
        is_discount = selected_type == 'discount'
        

        post_created = Post(title=form.title.data, content=form.content.data, user_id=user_id, image=filename,
                            is_adopt=is_adopt, is_foster=is_foster, is_product=is_product,is_discount=is_discount,
                             price=form.price.data)

        db.session.add(post_created)
        db.session.commit()
        return redirect(url_for('homelogged'))

    return render_template(
        'homelogged.html',
        title='homelogged',
        all_posts=Post.query.filter_by(is_events=False,is_tips=False),
        adopt_posts=Post.query.filter_by(is_adopt=True),
        foster_posts=Post.query.filter_by(is_foster=True),
        product_posts=Post.query.filter_by(is_product=True),
        discount_posts=Post.query.filter_by(is_discount=True),
        form=form
    )


@app.route("/update_post/<post_id>", methods=['POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        flash('You cant update this post!', 'danger')
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
    #elif request.method == 'GET':
        #form.title.data = post.title
        #form.content.data = post.content
    return redirect(url_for('homelogged'))


@app.route("/delete_post/<post_id>", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post:
        if post.user_id == current_user.id or current_user.is_admin:
            db.session.delete(post)
            db.session.commit()
            flash(f'Your post has been deleted!', 'success')
        else:
            flash(f'You cannot delete this post', 'danger')
    else:
        flash(f'Post with id - {post_id} does not exist', 'danger')
    return redirect(url_for('homelogged'))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account", methods=['GET', 'POST'])
def account():
    form=UpdateAccountForm()
    if form.validate_on_submit():
        current_user.name=form.name.data
        current_user.email=form.email.data
        db.session.commit()
        flash('Your Account is updated!','success')
        return redirect (url_for('account'))
    elif request.method =='GET':
        form.name.data=current_user.name
        form.email.data=current_user.email

    return render_template(
        'account.html', title='account',form=form,
        all_posts=Post.query.filter_by(user_id=current_user.id))


     
@app.route("/asosnews", methods=['GET', 'POST'])
@login_required
def asosnews():
    form = PostForm()
    if current_user.is_asos:
        form.type.choices = ['events','tips']
    
    if form.validate_on_submit():
        user_id = current_user.id
        f = form.image.data
        filename = None
        if f:
            filename = get_and_save_image(f)
        selected_type = form.type.data

        is_events = selected_type == 'events'
        is_tips = selected_type == 'tips'
       
    
        post_created = Post(title=form.title.data, content=form.content.data, user_id=user_id, image=filename,
                            is_events=is_events, is_tips=is_tips)

        db.session.add(post_created)
        db.session.commit()
     
    return render_template(
        'asosnews.html',
        title='asosnews',
        all_posts=Post.query.filter_by(is_discount=False,is_product=False,is_foster=False,is_adopt=False),
        asos_events_posts=Post.query.filter_by(is_events=True),
        asos_tips_posts=Post.query.filter_by(is_tips=True),
        form=form
    )