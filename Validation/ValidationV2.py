# Viene de un tema de Pirámides de pruebas de seguridad de desarrollo de pruebas unitarias mediante IA generativa
import re

class ScriptPython:
    
    @staticmethod
    def get_username(userName):
        """ Valida el nombre de usuario, solo permite alfanuméricos y guiones bajos. """
        if re.match("^[a-zA-Z0-9_]*$", userName):
            return userName
        raise ValueError("Invalid username. Only alphanumeric characters and underscores are allowed.")

    @staticmethod
    def get_password(password):
        """ Valida la contraseña, debe tener al menos 8 caracteres de longitud. """
        if len(password) >= 8:
            return password
        raise ValueError("Invalid password. It must be at least 8 characters long.")

    @staticmethod
    def get_email(email):
        """ Valida el formato del correo electrónico. """
        if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            return email
        raise ValueError("Invalid email address format.")

    @staticmethod
    def get_sql_query(query):
        """ Valida una consulta SQL, prohibe operaciones destructivas como DROP y DELETE. """
        if "DROP" not in query.upper() and "DELETE" not in query.upper():
            return query
        raise ValueError("Invalid SQL query. Destructive operations are not allowed.")
