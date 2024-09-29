from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'your_secret_key'  
app.config['MONGO_URI'] = 'mongodb://localhost:27017/blog' 
mongo = PyMongo(app)

@app.route('/')
def index():
    posts = mongo.db.posts.find()
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def add_post():
    title = request.form.get('title')
    content = request.form.get('content')
    mongo.db.posts.insert_one({'title': title, 'content': content})
    flash('Post added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/edit/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        mongo.db.posts.update_one({'_id': ObjectId(post_id)}, {'$set': {'title': title, 'content': content}})
        flash('Post updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit.html', post=post)

@app.route('/delete/<post_id>')
def delete_post(post_id):
    mongo.db.posts.delete_one({'_id': ObjectId(post_id)})
    flash('Post deleted successfully!', 'danger')
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
