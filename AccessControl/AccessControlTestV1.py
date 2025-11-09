import unittest
from flask import session
from AccessControl.AccessControlV2 import app, authenticate, check_role

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test_secret_key'
        self.client = app.test_client()
        self.client.testing = True

    def test_authentication_success(self):
        with self.client:
            response = self.client.post('/login', data=dict(username='admin', password='adminpass'))
            self.assertEqual(response.status_code, 302)  # Check redirection
            self.assertEqual(session['username'], 'admin')
            self.assertEqual(session['role'], 'admin')

    def test_authentication_failure(self):
        response = self.client.post('/login', data=dict(username='admin', password='wrongpass'))
        self.assertEqual(response.status_code, 401)

    def test_role_authorization(self):
        with self.client:
            self.client.post('/login', data=dict(username='admin', password='adminpass'))
            self.assertTrue(check_role('admin'))
            response = self.client.get('/admin')
            self.assertEqual(response.data.decode(), 'Admin Panel - only for admins')

    def test_unauthorized_admin_access(self):
        # Try accessing admin panel without correct role
        with self.client:
            self.client.post('/login', data=dict(username='user', password='userpass'))
            response = self.client.get('/admin')
            self.assertNotEqual(response.data.decode(), 'Admin Panel - only for admins')
            self.assertEqual(response.status_code, 302)  # Redirection to index

if __name__ == '__main__':
    unittest.main()
