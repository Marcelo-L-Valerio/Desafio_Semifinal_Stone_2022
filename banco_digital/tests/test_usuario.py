
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class UsuarioTestCase(TestCase):

    def setUp(self) -> None:
        self.usuario = APIClient()

    def test_cliente_post(self):
        # dado
        usuario = {
            "cod_conta": "1234567891",
            "nome": "Pessoa Teste",
            "tipo": "PF",
            "cpf": "12312312311",
            "email": "teste@hotmail.com.br",
            "saldo_atual": 500.0,
            "data_registro": "2022-07-17"
        }

        #quando
        response = self.client.post('/usuario/', usuario, format='json')

        #entao
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_usuario_post_wront_type_error(self):
        # dado
        usuario = {
            "cod_conta": "1234567891",
            "nome": "Pessoa Teste",
            "tipo": "PJ",
            "cpf": "12312312311",
            "email": "teste@hotmail.com.br",
            "saldo_atual": 500.0,
            "data_registro": "2022-07-17"
        }

        #quando
        response = self.client.post('/usuario/', usuario, format='json')

        #entao
        self.assertEqual(response.status_code, 400)

    def test_usuario_post_cod_conta_error(self):
        # dado
        usuario = {
            "cod_conta": "erapsernum",
            "nome": "Pessoa Teste",
            "tipo": "PF",
            "cpf": "12312312311",
            "email": "teste@hotmail.com.br",
            "saldo_atual": 500.0,
            "data_registro": "2022-07-17"
        }

        #quando
        response = self.client.post('/usuario/', usuario, format='json')

        #entao
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_usuario_post_empty_field_error(self):
        # dado
        usuario = {
            "cod_conta": "1234567891",
            "nome": "Pessoa Teste",
            "tipo": "PJ",
            "email": "teste@hotmail.com.br",
            "saldo_atual": 500.0,
            "data_registro": "2022-07-17"
        }

        #quando
        response = self.client.post('/usuario/', usuario, format='json')

        #entao
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_usuario_post_duplicated_cod_conta_error(self):
        # dado
        usuario = {
            "cod_conta": "1234567891",
            "nome": "Pessoa Teste",
            "tipo": "PF",
            "cpf": "12312312311",
            "email": "teste@hotmail.com.br",
            "saldo_atual": 500.0,
            "data_registro": "2022-07-17"
        }
        usuario_2 = {
            "cod_conta": "1234567891",
            "nome": "Pessoa Teste Junior",
            "tipo": "PF",
            "cpf": "12312312322",
            "email": "testejunior@hotmail.com.br",
            "saldo_atual": 500.0,
            "data_registro": "2022-07-17"
        }

        #quando
        self.client.post('/usuario/', usuario, format='json')
        response = self.client.post('/usuario/', usuario_2, format='json')

        #entao
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_usuario_consultar_saldo(self):
         # dado
        usuario = {
            "cod_conta": "1234567891",
            "nome": "Pessoa Teste",
            "tipo": "PF",
            "cpf": "12312312311",
            "email": "teste@hotmail.com.br",
            "saldo_atual": 500.0,
            "data_registro": "2022-07-17"
        }
        self.client.post('/usuario/', usuario, format='json')

        #quando
        response = self.client.get('/usuario/1234567891/saldo/', format='json')
        print(response)

        #entao
        self.assertEqual(response.status_code, status.HTTP_200_OK)