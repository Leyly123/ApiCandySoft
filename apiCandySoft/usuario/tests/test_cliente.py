import unittest
from usuario.models.usuario import Usuario
from usuario.models.cliente import Cliente
from rol.models import Rol


class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class TestCliente(unittest.TestCase):
    def test_crear_cliente(self):
        """Debe crear un cliente con los campos obligatorios"""
        try:
            rol_cliente, _ = Rol.objects.get_or_create(nombre="Cliente")

            usuario = Usuario.objects.create_user(
                username="estefa_a",
                password="Estefa123*",
                nombre="Estefa",
                apellido="Arroyo",
                correo="estefa@example.com",
                rol_id=rol_cliente  
            )

            cliente = Cliente.objects.create(
                usuario=usuario,
                nombre="Estefa",
                apellido="Arroyo",
                tipo_documento="CC",
                numero_documento="431129809",
                correo="estefa@example.com",
                celular="3129991212"
            )

            self.assertEqual(cliente.nombre, "Estefa")
            self.assertEqual(cliente.apellido, "Arroyo")
            self.assertEqual(cliente.correo, "estefa@example.com")

            print(f"{Colors.OKGREEN}✔ Cliente creado correctamente: {usuario.username}{Colors.ENDC}")

        except Exception as e:
            print(f"{Colors.FAIL}✘ Error al crear cliente: {e}{Colors.ENDC}")
            raise e


if __name__ == '__main__':
    unittest.main(verbosity=2)
