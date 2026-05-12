import os

# Mock das variáveis de ambiente
os.environ['MEU_USUARIO'] = 'admin@email.com'
os.environ['MINHA_SENHA'] = 'admin123'

from fastapi.testclient import TestClient
from main import app

import pytest

client = TestClient(app)

# Mock Redis
@pytest.fixture(autouse=True)
def mock_redis(mocker):
    mock_redis_client = mocker.patch('main.redis_client', autospec=True)
    mock_redis_client.get.return_value = None

# Login com sucesso
def test_autenticacao_usuario_com_sucesso():
    response = client.post(
        '/login',
        json={
            'email': 'admin@email.com',
            'senha': 'admin123'
        }
    )

    assert response.status_code == 200

    assert response.json()['message'] == ('Login realizado com sucesso!')

# Email incorreto
def test_autenticacao_usuario_com_erro():
    response = client.post(
        '/login',
        json={
            'email': 'usuario_incorreto@email.com',
            'senha': 'admin123'
            }
        )
    
    assert response.status_code == 401

    assert response.json()['detail'] == ('Usuario ou senha incorretos')

# Senha incorreta
def test_autenticacao_senha_com_erro():
    response = client.post(
        '/login',
        json= {
            'email': 'admin@email.com',
            'senha': 'senha_incorreta'
        }       
    )
    assert response.status_code == 401

    assert response.json()['detail'] == ('Usuario ou senha incorretos')

