from flask import Blueprint, render_template, request, redirect, url_for
from models.models import User, Post, db

views = Blueprint("views", __name__)


@views.route("/", endpoint="index" )
def index():
    return render_template("index.html")


@views.route("/information", endpoint="information")
def information():
    users_with_posts = User.query.join(Post).all()
    users_without_posts = User.query.outerjoin(Post).filter(Post.id is None).all()
    return render_template(
        "information.html",
        users_with_posts=users_with_posts,
        users_without_posts=users_without_posts
    )


@views.route("/add_users", methods=["GET", "POST"],endpoint="add_users")
def add_users():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        email = request.form["email"]
        user = User(name=name, username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("views.information"))
    return render_template("add_users.html")
