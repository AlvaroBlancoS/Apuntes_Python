import unittest
from BinarySearchTree import BinarySearchTree

# Insertar valores de muestra para asegurarse de que el árbol se genera correctamente
values_to_insert = [10, 5, 15, 3, 8, 12, 18]

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        # Insertar valores de muestra para asegurarse de que el árbol se genera correctamente
        values_to_insert = [10, 5, 15, 3, 8, 12, 18]
        for value in values_to_insert:
            self.bst.insert(value)
            print(f"Árbol generado de valores inicialmente insertados: {value}")        
    
    def test_insert_and_find(self):
        # Insertar valores y verificar si existen
        print("Inserción y búsqueda de valores:")
        self.bst.insert(10)
        print("Buscar 10: encontrado.")
        self.bst.insert(5)
        print("Buscar 5: encontrado.")
        self.bst.insert(15)
        print("Buscar 15: encontrado.")
        
        print("Insertado 10, 5, 15 en el árbol.")
        self.assertTrue(self.bst.find(10))
        print("Probar búsqueda de 10: Encontrado.")
        self.assertTrue(self.bst.find(5))
        print("Probar búsqueda de 5: Encontrado.")
        self.assertTrue(self.bst.find(15))
        print("Probar búsqueda de 20: Encontrado.")
        self.assertFalse(self.bst.find(20))
   
    # def test_find_existing_value(self):
    #     print("Prueba de que find(val) devuelve True para valores existentes:")
    #     self.assertTrue(self.bst.find(5))
    #     print("Buscar 5: Encontrado, devuelve True.")
    #     self.assertTrue(self.bst.find(12))
    #     print("Buscar 12: Encontrado, devuelve True.")
         
    def test_higher(self):
        # Insertar valores y verificar el valor superior
        print("Verificar valores superiores:")
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(12)
        
        print("Insertado 10, 5, 15, 12 en el árbol.")
        self.assertEqual(self.bst.higher(5), 10)
        print("Valor superior a 5: 10.")
        self.assertEqual(self.bst.higher(10), 12)
        print("Valor superior a 10: 12.")
        self.assertEqual(self.bst.higher(12), 15)
        print("Valor superior a 12: 15.")
        
        with self.assertRaises(ValueError):
            self.bst.higher(15)  # No hay valor superior a 15
        print("No hay valor superior a 15: Se lanzó ValueError.")

        with self.assertRaises(ValueError):
            self.bst.higher(20)  # Valor no encontrado
        print("Valor 20 no encontrado: Se lanzó ValueError.")    
    
    def test_lower(self):
        # Insertar valores y verificar el valor inferior
        print("Verificar valores inferiores:")
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(8)
        
        print("Insertado 10, 5, 15, 8 en el árbol.")
        self.assertEqual(self.bst.lower(10), 8)
        print("Valor inferior a 10: 8.")
        self.assertEqual(self.bst.lower(8), 5)
        print("Valor inferior a 8: 5.")
        
        with self.assertRaises(ValueError):
            self.bst.lower(5)  # No hay valor inferior a 5
        print("No hay valor inferior a 5: Se lanzó ValueError.")    
        
        with self.assertRaises(ValueError):
            self.bst.lower(20)  # Valor no encontrado
        print("Valor 20 no encontrado: Se lanzó ValueError.")    

    def test_empty_tree(self):
        # Probar árbol vacío
        print("Probar árbol vacío:")
        with self.assertRaises(ValueError):
            self.bst.higher(5)
        print("Valor superior en árbol vacío: Se lanzó ValueError.")    
        
        with self.assertRaises(ValueError):
            self.bst.lower(5)
        print("Valor inferior en árbol vacío: Se lanzó ValueError.")    

if __name__ == '__main__':
    unittest.main()
