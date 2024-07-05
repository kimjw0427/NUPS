from flask import Blueprint, request, jsonify
from app import db
from models import Post
from flask_jwt_extended import jwt_required, get_jwt_identity

board_bp = Blueprint('board_bp', __name__)

@board_bp.route('/<category>', methods=['POST'])
@jwt_required()
def create_post(category):
    if category not in ['자유게시판', '연구과제', '뉴스']:
        return jsonify({"msg": "Invalid category"}), 400

    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    user_id = get_jwt_identity()

    new_post = Post(title=title, content=content, category=category, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    return jsonify({"msg": "Post created successfully"}), 201

@board_bp.route('/<category>', methods=['GET'])
def get_posts(category):
    if category not in ['자유게시판', '연구과제', '뉴스']:
        return jsonify({"msg": "Invalid category"}), 400

    sort_by = request.args.get('sort_by', 'created_at')
    order = request.args.get('order', 'desc')
    search = request.args.get('search', '')

    query = Post.query.filter(Post.category == category)

    if search:
        query = query.filter(Post.title.contains(search) | Post.content.contains(search))

    if order == 'desc':
        query = query.order_by(db.desc(getattr(Post, sort_by)))
    else:
        query = query.order_by(db.asc(getattr(Post, sort_by)))

    posts = query.all()
    return jsonify([{
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "category": post.category,
        "created_at": post.created_at,
        "updated_at": post.updated_at,
        "user_id": post.user_id
    } for post in posts]), 200

@board_bp.route('/<int:post_id>', methods=['PUT'])
@jwt_required()
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    user_id = get_jwt_identity()

    if post.user_id != user_id:
        return jsonify({"msg": "Permission denied"}), 403

    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)

    db.session.commit()

    return jsonify({"msg": "Post updated successfully"}), 200

@board_bp.route('/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    user_id = get_jwt_identity()

    if post.user_id != user_id:
        return jsonify({"msg": "Permission denied"}), 403

    db.session.delete(post)
    db.session.commit()

    return jsonify({"msg": "Post deleted successfully"}), 200