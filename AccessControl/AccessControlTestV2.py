import unittest
from flask import request, session
from AccessControl.AccessControlV2 import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test_secret_key'
        self.client = app.test_client()
        self.client.testing = True

    # 1. Asegurar de que los mecanismos de autenticación sean seguros y no puedan eludirse
    def test_authentication_success(self):
        with self.client:
            response = self.client.post('/login', data=dict(username='admin', password='adminpass'))
            self.assertEqual(response.status_code, 302)  # Espera redirección
            self.assertIn('username', session)
            self.assertEqual(session['username'], 'admin')
            self.assertEqual(session['role'], 'admin')

    def test_authentication_failure(self):
        with self.client:
            response = self.client.post('/login', data=dict(username='admin', password='wrongpass'))
            self.assertEqual(response.status_code, 401)
            self.assertNotIn('username', session)
    
    # 2. Verificar que los esquemas de autorización implementen correctamente modelos de control de acceso basado en roles u otros
    def test_authorization_roles(self):
        with self.client:
            self.client.post('/login', data=dict(username='admin', password='adminpass'))
            response = self.client.get('/admin')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Admin Panel', response.data.decode())

    # 3. Verifique que no pueda ocurrir una escalada de privilegios cuando un usuario menores privilegios obtenga indebidamente mayores derechos de acceso
    def test_privilege_escalation_prevention(self):
        with self.client:
            self.client.post('/login', data=dict(username='user', password='userpass'))
            response = self.client.get('/admin')
            self.assertNotEqual(response.status_code, 200)
            self.assertNotIn('Admin Panel', response.data.decode())
    
    # 4. Confirmar que el acceso a operaciones sensibles (como funciones administrativas) esté restringido adecuadamente
    def test_sensitive_operations_access(self):
        with self.client:
            # Asegura que el acceso al panel admin es denegado sin usuario logueado
            response = self.client.get('/admin')
            self.assertNotEqual(response.status_code, 200)
            self.assertNotIn('Admin Panel', response.data.decode())

if __name__ == '__main__':
    unittest.main()
