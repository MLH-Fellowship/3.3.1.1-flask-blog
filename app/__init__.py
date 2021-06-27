import os
from flask import Flask, render_template
from . import db

app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

# from dotenv import load_dotenv

# load_dotenv()
# app = Flask(__name__)

# ROUTES
# @app.route('/')
# def index():
#     return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

# @app.route('/profiles')
# def my_profiles():
#     return render_template('profiles.html', title="Meet the Fellows", url=os.getenv("URL"))

# @app.route('/wishlist')
# def my_wishlist():
#     return render_template('wishlist.html', title="Our Wishlists", url=os.getenv("URL"))

@app.route('/blog')
def my_blog():
    return render_template('blog.html', title="Blog", url=os.getenv("URL"))