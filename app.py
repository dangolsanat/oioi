from flask import Flask, render_template, redirect, session, flash, url_for, request, jsonify, make_response
from models import connect_db, Users, db, Full_user, Post, PostImage, Message
from forms import UserForm, LoginForm, AddPost
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut



from sqlalchemy.exc import IntegrityError



app = Flask(__name__, static_folder='static')



app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres.zbdnvxkwfezjvwltqbgm:Vp*4.$Lxsv5kaGL@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///oioi'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)


geolocator = Nominatim(user_agent="your_app_name", timeout=10)


@app.route('/', methods=['GET', 'POST'])
def index():
    cuser = None
    fuser = None

    if "user_id" in session:
        cuser = Users.query.get(session['user_id'])
        if cuser:
            fuser = Full_user.query.filter_by(user_id=cuser.id).first()
        else:
            flash("User not found.", "error")

    else:
        flash("Please log in or sign up.", "error")

    # Fetch all users and posts
    all_users = Full_user.query.all()
    users_dict = {user.id: user for user in all_users}

    posts = Post.query.all()

    # Fetch and associate images with posts
    post_images = PostImage.query.filter(PostImage.post_id.in_([post.id for post in posts])).all()
    posts_dict = {post.id: post for post in posts}
    for img in post_images:
        if hasattr(posts_dict[img.post_id], 'images'):
            posts_dict[img.post_id].images.append(img)
        else:
            posts_dict[img.post_id].images = [img]

    return render_template('index.html', cuser=cuser, fuser=fuser, posts=posts, users_dict=users_dict)


@app.route('/home')
def home_page():
    if "user_id" not in session:
        flash("Please log in or sign up.", "error")
        return redirect('/login')

    # Fetch current user
    cuser = Users.query.get(session['user_id'])
    if not cuser:
        flash("User not found.", "error")
        return redirect('/login')

    # Fetch full user info
    full_user_info = Full_user.query.filter_by(user_id=cuser.id).first()
    if not full_user_info:
        flash("Please complete your user profile.", "message")

    # Fetch all users and posts
    all_users = Full_user.query.all()
    users_dict = {user.id: user for user in all_users}

    # Calculate age for each user
    # for user_id, user in users_dict.items():
    #     user.age = user.calculate_age()

    posts = Post.query.all()
    
    # Fetch and associate images with posts
    post_images = PostImage.query.filter(PostImage.post_id.in_([post.id for post in posts])).all()
    posts_dict = {post.id: post for post in posts}
    for img in post_images:
        if hasattr(posts_dict[img.post_id], 'images'):
            posts_dict[img.post_id].images.append(img)
        else:
            posts_dict[img.post_id].images = [img]

    return render_template('home.html', cuser=cuser, fuser=full_user_info, posts=posts, users_dict=users_dict)



@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = LoginForm()

    if form.validate_on_submit(): 
        username = form.username.data
        password = form.password.data
        new_user = Users.register(username, password)

        try:
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            flash("Registration successful! Welcome!", 'success')
            return redirect('/addprofile')

        except IntegrityError:
            db.session.rollback()
            flash("Username already exists. Please choose a different username.", 'error')

        except Exception as e:
            db.session.rollback()
            flash("An error occurred. Please try again.", 'error')
            print(f"Error during registration: {e}")

    return render_template('register.html', form=form)


"""route for posts"""

@app.route('/posts/<int:id>', methods=['GET'])
def post_page(id):
    fuser = session['user_id']
    post = Post.query.get_or_404(id)
    full_user_info = Full_user.query.filter_by(user_id=post.user_rel.full_user.id).first()

    
    location = geolocator.geocode(post.address)
    latitude = location.latitude if location else None
    longitude = location.longitude if location else None

    return render_template('post.html', post=post, latitude=latitude, longitude=longitude, full_user_info=full_user_info, fuser=fuser)

@app.route('/postes/<int:id>', methods=['GET'])
def postes_page(id):
    post = Post.query.get_or_404(id)
    full_user_info = Full_user.query.filter_by(user_id=post.user_rel.full_user.id).first()

    
    location = geolocator.geocode(post.address)
    latitude = location.latitude if location else None
    longitude = location.longitude if location else None

    return render_template('post_nosignin.html', post=post, latitude=latitude, longitude=longitude, full_user_info=full_user_info)





"""route for editing a post"""

@app.route('/posts/<int:id>/edit', methods=['GET', 'POST'])
def edit_post(id):
    user = Users.query.get(session.get('user_id'))

    post = Post.query.get(id)
    return render_template('edit_post.html')



"""route for adding a profile"""



@app.route('/addprofile', methods=['GET', 'POST'])
def profile_info():
    user = Users.query.get(session.get('user_id'))
    if not user:
        flash('User not found. Please log in first.', "error")
        return redirect('/')

    form = UserForm()

    if form.validate_on_submit():
        Full_user.add_profile(
            user_id=user.id,
            firstname=form.first_name.data,
            lastname=form.last_name.data,
            email=form.email.data,
            image=form.user_image.data,  # Ensure this is a URL
            dob=form.dob.data,
            bio=form.bio.data,
            intro=form.intro.data,
        )

        flash('Profile created successfully!')
        return redirect('/home')

    return render_template('profileadd.html', form=form, fuser=user)





@app.route('/login', methods=['GET', 'POST'])
def login_user():
    if 'user_id' in session:
        flash("You're already logged in.")
        return redirect('/home')
    
    form = LoginForm()

    if form.validate_on_submit(): 
        username = form.username.data
        password = form.password.data

        user = Users.authenticate(username, password)
    
        if user:
            flash(f"Welcome back, {user.username}!")
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect('/home')
        else:
            form.username.errors = ['wrong username or password.']

    return render_template("login.html", form=form)



@app.route('/logout')  
def logout_user():
    flash('See you soon!')
    session.pop('user_id')
    return redirect('/')



@app.route('/users/<int:user_id>', methods=['GET', 'POST'])
def user_page(user_id):
    user = Users.query.get_or_404(user_id)
    form = AddPost()

    if form.validate_on_submit():
        new_post = Post.add_post(
            user_id=user_id,
            title=form.title.data,
            description=form.description.data,
            address=form.address.data,
            neighbor=form.neighbor.data,
            borough=form.borough.data,
            price=form.price.data,
            neighborhood=form.neighborhood.data,
        )

        images = request.files.getlist('images')  # Assuming you get URLs from a file input
        for image in images:
            if image:
                url = image.data  # Get URL data
                PostImage.add_image(post_id=new_post.id, url=url)

        flash('Post added successfully!', 'success')
        return redirect(url_for('home_page'))

    return render_template('user.html', user=user, form=form, fuser=user, posts=Post.query.filter_by(user_id=user.id).all())



@app.route('/users/profile/<int:user_id>', methods=['GET'])
def user_profile(user_id):
    
    cuser = Users.query.get(session['user_id'])
        
    # Retrieve the user and their profile info
    user = Users.query.get_or_404(user_id)
    full_user_info = Full_user.query.filter_by(user_id=user.id).first()
    posts = Post.query.filter_by(user_id=user.id).all()

    # Ensure profile info exists
    if not full_user_info:
        flash("User profile information is incomplete.", "error")
        return redirect('/home')
    
    if cuser and cuser.id == user_id:
        return redirect(f'/users/{user_id}')

    return render_template('profile.html', user=user, full_user_info=full_user_info, posts=posts, cuser=cuser)







@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if "user_id" not in session:
        flash("Please log in first.", "error")
        return redirect('/login')  # Redirect to your login route

    user_id = session['user_id']
    fuser = user_id
    cur_user = user_id

    # Retrieve all conversations for the current user
    all_messages = Message.query.filter(
        (Message.sender_id == user_id) | (Message.receiver_id == user_id)
    ).order_by(Message.timestamp.desc()).all()

    # Dictionary to store the latest message with each unique user
    latest_messages = {}
    for message in all_messages:
        other_user_id = message.receiver_id if message.sender_id == user_id else message.sender_id
        if other_user_id not in latest_messages or message.timestamp > latest_messages[other_user_id].timestamp:
            latest_messages[other_user_id] = message

    latest_messages_with_users = []
    current_user_id = session['user_id']
    for msg in latest_messages.values():
        sender = Users.query.get(msg.sender_id)
        receiver = Users.query.get(msg.receiver_id)

        message_entry = {
            'content': msg.content,
            'timestamp': msg.timestamp,
            'sender': sender,
            'receiver': receiver
        }

        if receiver.id == current_user_id:
            message_entry['sender'], message_entry['receiver'] = receiver, sender

        latest_messages_with_users.append(message_entry)

    # Handle specific chat view if recipient_id is provided
    recipient = None
    messages = []
    if request.args.get('recipient_id'):
        recipient_id = int(request.args.get('recipient_id'))
        recipient = Users.query.get_or_404(recipient_id)
        messages = Message.query.filter(
            ((Message.sender_id == user_id) & (Message.receiver_id == recipient_id)) |
            ((Message.sender_id == recipient_id) & (Message.receiver_id == user_id))
        ).order_by(Message.timestamp.asc()).all()

    return render_template('messages.html', 
                           fuser=fuser,
                           latest_messages=latest_messages,
                           latest_messages_with_users=latest_messages_with_users,
                           recipient=recipient, 
                           messages=messages, cur_user=cur_user)




@app.route('/send_message', methods=['POST'])
def handle_send_message():
    sender_id = session.get('user_id')
    data = request.get_json()
    receiver_id = data.get('recipient_id')
    content = data.get('message')

    if sender_id and receiver_id and content:
        message = Message.send_message(sender_id, receiver_id, content)
        return jsonify({
            'sender_id': sender_id,
            'receiver_id': receiver_id,
            'content': content,
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }), 200
    else:
        return jsonify({'error': 'Invalid data'}), 400


@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword', '')
    posts = Post.query.filter(Post.title.ilike(f'%{keyword}%')).all()
    users_dict = {user.id: user for user in Full_user.query.all()}

    html = render_template('partials/_post_list.html', posts=posts, users_dict=users_dict)

    return jsonify({'html': html})





