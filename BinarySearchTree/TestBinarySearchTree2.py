import unittest
from BinarySearchTree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()  # Crear una nueva instancia de BinarySearchTree
        # Insertar valores de muestra para asegurarse de que el árbol se genera correctamente
        values_to_insert = [10, 5, 15, 3, 8, 12, 18]
        for value in values_to_insert:
            self.bst.insert(value)
        print("Árbol generado con los valores: 10, 5, 15, 3, 8, 12, 18.")

    def test_insert_and_find(self):
        print("Prueba de búsqueda de valores inicialmente insertados:")
        self.assertTrue(self.bst.find(10))
        print("Buscar 10: Encontrado.")
        self.assertTrue(self.bst.find(5))
        print("Buscar 5: Encontrado.")
        self.assertTrue(self.bst.find(12))
        print("Buscar 12: Encontrado.")
        self.assertFalse(self.bst.find(20))
        print("Buscar 20: No encontrado.")
    
    def test_higher(self):
        print("Verificar valores superiores:")
        self.assertEqual(self.bst.higher(5), 8)
        print("Valor superior a 5: 8.")
        self.assertEqual(self.bst.higher(10), 12)
        print("Valor superior a 10: 12.")
        self.assertEqual(self.bst.higher(18), None)
        print("No hay valor superior a 18.")
        
        with self.assertRaises(ValueError):
            self.bst.higher(20) # No hay valor superior a 20
        print("Valor 20 no encontrado: Se lanzó ValueError.")
    
    def test_lower(self):
        print("Verificar valores inferiores:")
        self.assertEqual(self.bst.lower(10), 8)
        print("Valor inferior a 10: 8.")
        self.assertEqual(self.bst.lower(5), 3)
        print("Valor inferior a 5: 3.")
        
        with self.assertRaises(ValueError):
            self.bst.lower(3)
        print("No hay valor inferior a 3: Se lanzó ValueError.")
        
        with self.assertRaises(ValueError):
            self.bst.lower(20)
        print("Valor 20 no encontrado: Se lanzó ValueError.")

    def test_empty_tree(self):
        empty_bst = BinarySearchTree()
        print("Probar un árbol vacío:")
        with self.assertRaises(ValueError):
            empty_bst.higher(5)
        print("Valor superior en árbol vacío: Se lanzó ValueError.")
        
        with self.assertRaises(ValueError):
            empty_bst.lower(5)
        print("Valor inferior en árbol vacío: Se lanzó ValueError.")

if __name__ == '__main__':
    unittest.main()
