# Viene de un tema de Pirámides de pruebas de seguridad de desarrollo de pruebas unitarias mediante IA generativa
import unittest
from Validation.ValidationV2 import ScriptPython

class ScriptPythonTest(unittest.TestCase):
    
    #Pruebas para get_username
    def test_username_valid(self):
        self.assertEqual(ScriptPython.get_username("valid_username123"), "valid_username123")
    
    def test_username_invalid(self):
        with self.assertRaises(ValueError):
            ScriptPython.get_username("invalid username!")

    def test_username_unexpected(self):
        with self.assertRaises(TypeError):  # Asumiendo que un TypeError debe ser lanzado
            ScriptPython.get_username(None)

    #Pruebas para password    
    def test_password_valid(self):
        self.assertEqual(ScriptPython.get_password("password123"), "password123")

    def test_password_invalid(self):
        with self.assertRaises(ValueError):
            ScriptPython.get_password("short")

    def test_password_unexpected(self):
        with self.assertRaises(TypeError):  # Asumiendo que un TypeError debe ser lanzado
            ScriptPython.get_password(12345678)            

    #Pruebas para get_email
    def test_email_valid(self):
        self.assertEqual(ScriptPython.get_email("email@example.com"), "email@example.com")

    def test_email_invalid(self):
        with self.assertRaises(ValueError):
            ScriptPython.get_email("email@com")

    #Pruebas para get_sql_query 
    def test_sql_query_valid(self):
        self.assertEqual(ScriptPython.get_sql_query("SELECT * FROM users"), "SELECT * FROM users")

    def test_sql_query_invalid(self):
        with self.assertRaises(ValueError):
            ScriptPython.get_sql_query("DROP TABLE users")

if __name__ == '__main__':
    unittest.main()
