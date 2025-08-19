import unittest
from insumo.models import Insumo, Marca

class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

class TestInsumo(unittest.TestCase):
    def test_crear_insumo(self):
        """Debe crear un insumo con los campos obligatorios"""
        try:
            marca_insumo, _ = Marca.objects.get_or_create(id="3")
            
            insumo = Insumo.objects.create(
                nombre="Top coat",
                stock=10,
                marca_id=marca_insumo
            )
            
            self.assertEqual(insumo.nombre, "Top coat")
            self.assertEqual(insumo.stock, 10)

            print(f"{Colors.OKGREEN}✔ Insumo creado correctamente: {insumo.nombre}{Colors.ENDC}")

        except Exception as e:
            print(f"{Colors.FAIL}✘ Error al crear el insumo: {e}{Colors.ENDC}")
            raise e  


if __name__ == '__main__':
    unittest.main(verbosity=2)
