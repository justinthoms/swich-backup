from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from bson.objectid import ObjectId
import os
from datetime import timedelta



app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

# MongoDB configuration
MONGO_URI = "mongodb+srv://tsradmin:xJXXyxMpz14ksSnq@tsr-backup-sw.gofzs.mongodb.net/?retryWrites=true&w=majority&appName=TSR-BACKUP-SW"
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)
db = mongo.cx['network_management']
switch_collection = db['switches']

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Mock User class for authentication
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    if user_id == "admin":
        return User(user_id)
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            user = User('admin')
            login_user(user)
            session.permanent = True
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    switches = switch_collection.find()
    return render_template('index.html', switches=switches)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_switch():
    if request.method == 'POST':
        switch_data = {
            "name": request.form['name'],
            "hostname": request.form['hostname'],
            "port": int(request.form['port']),
            "username": request.form['username'],
            "password": request.form['password'],
            "brand": request.form['brand'],
            "services": request.form['services']
        }
        switch_collection.insert_one(switch_data)
        flash('Switch added successfully!')
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit_switch(id):
    switch = switch_collection.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        updated_data = {
            "name": request.form['name'],
            "hostname": request.form['hostname'],
            "port": int(request.form['port']),
            "username": request.form['username'],
            "password": request.form['password'],
            "brand": request.form['brand'],
            "services": request.form['services']
        }
        switch_collection.update_one({'_id': ObjectId(id)}, {'$set': updated_data})
        flash('Switch updated successfully!')
        return redirect(url_for('index'))
    return render_template('edit.html', switch=switch)

@app.route('/delete/<id>')
@login_required
def delete_switch(id):
    switch_collection.delete_one({'_id': ObjectId(id)})
    flash('Switch deleted successfully!')
    return redirect(url_for('index'))

@app.route('/backup')
@login_required
def backup():
    switches = switch_collection.find()
    backup_folder = 'backups'
    os.makedirs(backup_folder, exist_ok=True)
    for switch in switches:
        filename = f"{backup_folder}/{switch['name']}_backup.txt"
        with open(filename, 'w') as f:
            f.write(f"Name: {switch['name']}\n")
            f.write(f"Hostname: {switch['hostname']}\n")
            f.write(f"Port: {switch['port']}\n")
            f.write(f"Username: {switch['username']}\n")
            f.write(f"Brand: {switch['brand']}\n")
            f.write(f"Services: {switch['services']}\n")
    flash('Backup completed successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
