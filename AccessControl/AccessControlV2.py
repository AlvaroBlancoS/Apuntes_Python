from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super_secret_key'

users_db = {
    'admin': {'password': 'adminpass', 'role': 'admin'},
    'user': {'password': 'userpass', 'role': 'user'}
}

def authenticate(username, password):
    user = users_db.get(username)
    if user and user['password'] == password:
        session['username'] = username
        session['role'] = user['role']
        return True
    return False

def logout():
    session.clear()

def check_role(role):
    return session.get('role') == role

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if authenticate(username, password):
        return redirect(url_for('index'))
    return 'Invalid credentials', 401

@app.route('/logout')
def logout_route():
    logout()
    return redirect(url_for('index'))

@app.route('/')
def index():
    if 'username' in session:
        return f'Hello, {session["username"]}!'
    return 'You are not logged in.'

@app.route('/admin')
def admin_panel():
    if check_role('admin'):
        return 'Admin Panel - only for admins'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
