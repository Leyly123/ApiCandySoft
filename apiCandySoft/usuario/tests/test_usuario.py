import unittest
from usuario.models.usuario import Usuario
from rol.models import Rol

class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

class TestUsuario(unittest.TestCase):
    def test_crear_usuario(self):
        """Debe crear un usuario con los campos obligatorios"""
        try:
            rol_usuario, _ = Rol.objects.get_or_create(nombre="Recepcionista")
            
            user = Usuario.objects.create_user(
                username="Luz_c",
                password="luz277*",
                nombre="Luz",
                apellido="Ciro",
                correo="luz@example.com",
                rol_id=rol_usuario
            )
            
            self.assertEqual(user.nombre, "Luz")
            self.assertEqual(user.apellido, "Ciro")
            self.assertEqual(user.correo, "luz@example.com")

            print(f"{Colors.OKGREEN}✔ Usuario creado correctamente: {user.username}{Colors.ENDC}")

        except Exception as e:
            print(f"{Colors.FAIL}✘ Error al crear usuario: {e}{Colors.ENDC}")
            raise e  


if __name__ == '__main__':
    unittest.main(verbosity=2)
