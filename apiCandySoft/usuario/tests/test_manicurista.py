import unittest
from usuario.models.usuario import Usuario
from usuario.models.manicurista import Manicurista
from rol.models import Rol


class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class TestManicurista(unittest.TestCase):
    def test_crear_manicurista(self):
        """Debe crear un manicurista con los campos obligatorios"""
        try:
            rol_manicurista, _ = Rol.objects.get_or_create(nombre="Manicurista")

            usuario = Usuario.objects.create_user(
                username="David_p",
                password="David2323*",
                nombre="David",
                apellido="Pineda",
                correo="david@example.com",
                rol_id=rol_manicurista
            )

            manicurista = Manicurista.objects.create(
                usuario=usuario,
                nombre="David",
                apellido="Pineda",
                tipo_documento="CC",
                numero_documento="54123412",
                correo="david@example.com",
                celular="3009992222",
                fecha_nacimiento="2001-10-22",
                fecha_contratacion="2024-01-12"
            )

            self.assertEqual(manicurista.nombre, "David")
            self.assertEqual(manicurista.apellido, "Pineda")
            self.assertEqual(manicurista.correo, "david@example.com")

            print(f"{Colors.OKGREEN}✔ Manicurista creado correctamente: {usuario.username}{Colors.ENDC}")

        except Exception as e:
            print(f"{Colors.FAIL}✘ Error al crear manicurista: {e}{Colors.ENDC}")
            raise e


if __name__ == '__main__':
    unittest.main(verbosity=2)
