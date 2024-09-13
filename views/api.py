from flask import Blueprint, jsonify
from models.models import User, Post

api = Blueprint("api", __name__)


@api.route("/api/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify(
        [
            {
                "id": user.id,
                "name": user.name,
                "username": user.username,
                "email": user.email,
                "posts": [
                    {"id": post.id, "title": post.title, "body": post.body}
                    for post in user.posts
                ],
            }
            for user in users
        ]
    )


@api.route("/api/posts", methods=["GET"])
def get_posts():
    posts = Post.query.all()
    return jsonify(
        [
            {
                "id": post.id,
                "title": post.title,
                "body": post.body,
                "user": (
                    {"id": post.user.id, "name": post.user.name} if post.user else None
                ),
            }
            for post in posts
        ]
    )


@api.route("/api/users_without_posts", methods=["GET"])
def get_users_without_posts():
    users = User.query.outerjoin(Post).filter(Post.id == None).all()
    return jsonify(
        [
            {"id": user.id, "name": user.name, "username": user.username, "email": user.email}
            for user in users
        ]
    )

