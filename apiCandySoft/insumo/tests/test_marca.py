import unittest
from insumo.models import Marca

class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

class TestMarca(unittest.TestCase):
    def test_crear_marca(self):
        """Debe crear una marca con el campo obligatorio"""
        try:
            marca = Marca.objects.create(
                nombre="OPI"
            )
            
            self.assertEqual(marca.nombre, "OPI")

            print(f"{Colors.OKGREEN}✔ Marca creada correctamente: {marca.nombre}{Colors.ENDC}")

        except Exception as e:
            print(f"{Colors.FAIL}✘ Error al crear la marca: {e}{Colors.ENDC}")
            raise e  


if __name__ == '__main__':
    unittest.main(verbosity=2)
