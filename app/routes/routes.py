from flask import render_template, redirect, url_for, flash, jsonify, request, Blueprint
from .. import db
from app.models import User
from flask_httpauth import HTTPBasicAuth

main = Blueprint('main', __name__)
auth = HTTPBasicAuth()

# @auth.verify_password
# def verify_password(username, password):
#     # Simple authentication (replace with secure logic)
#     user = User.query.filter_by(username=username).first()
#     if user and user.password == password:
#         return username

@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@main.route('/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        data = request.form
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        flash('User Successfully created', 'success')
        return redirect(url_for('main.index'))
    return render_template('create_user.html')

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return render_template('index.html', users=users)

@main.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return render_template('user_detail.html', user=user)

@main.route('/users/<int:id>/edit', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        flash('User updated successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('edit_user.html', user=user)

@main.route('/users/<int:id>/delete', methods=['GET', 'DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('main.index'))

@main.route('/users/search', methods=['GET'])
def search_user():
    query = request.args.get('query', '').strip()
    search_by = request.args.get('by', 'name')

    if not query:
        flash('Please enter a search term.', 'warning')
        return redirect(url_for('main.index'))

    if search_by == "id" and query.isdigit():
        users = User.query.filter_by(id=int(query)).all()
    else:
        users = User.query.filter(User.username.ilike(f"%{query}%")).all()

    return render_template('index.html', users=users)
