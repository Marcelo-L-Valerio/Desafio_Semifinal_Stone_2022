
from django.test import TestCase
from rest_framework import status


class TransferenciaTestCase(TestCase):

    def test_transferencia_realizada(self):
        # dado
        usuario = {
            "cod_conta": "1234567890",
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
        self.client.post('/usuario/', usuario, format='json')
        self.client.post('/usuario/', usuario_2, format='json')

        transferencia = {
            "cod_transferencia": "123456789123456",
            "conta_origem": "1234567890",
            "conta_destino": "1234567891",
            "valor": 500.0,
            "data_transferencia": "2022-07-17"
        }

        #quando

        response = self.client.post('/transferencias/', transferencia, format='json')

        #entao
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_transferencia_saldo_insulficiente_error(self):
        # dado
        usuario = {
            "cod_conta": "1234567890",
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
        self.client.post('/usuario/', usuario, format='json')
        self.client.post('/usuario/', usuario_2, format='json')

        transferencia = {
            "cod_transferencia": "123456789123456",
            "conta_origem": "1234567890",
            "conta_destino": "1234567891",
            "valor": 1000.0,
            "data_transferencia": "2022-07-17"
        }

        #quando

        response = self.client.post('/transferencias/', transferencia, format='json')

        #entao
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_transferencia_cod_conta_inexistente_error(self):
        # dado
        usuario = {
            "cod_conta": "1234567890",
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
        self.client.post('/usuario/', usuario, format='json')
        self.client.post('/usuario/', usuario_2, format='json')

        transferencia = {
            "cod_transferencia": "123456789123456",
            "conta_origem": "1234567892",
            "conta_destino": "1234567891",
            "valor": 500.0,
            "data_transferencia": "2022-07-17"
        }

        #quando

        response = self.client.post('/transferencias/', transferencia, format='json')

        #entao
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_transferencia_cod_conta_repetido_error(self):
        # dado
        usuario = {
            "cod_conta": "1234567890",
            "nome": "Pessoa Teste",
            "tipo": "PF",
            "cpf": "12312312311",
            "email": "teste@hotmail.com.br",
            "saldo_atual": 500.0,
            "data_registro": "2022-07-17"
        }

        self.client.post('/usuario/', usuario, format='json')

        transferencia = {
            "cod_transferencia": "123456789123456",
            "conta_origem": "1234567890",
            "conta_destino": "1234567890",
            "valor": 500.0,
            "data_transferencia": "2022-07-17"
        }

        #quando

        response = self.client.post('/transferencias/', transferencia, format='json')

        #entao
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)