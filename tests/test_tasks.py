import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from tasks import somar, fatorial
from main import app

# Fixture para mockar time.sleep
@pytest.fixture
def mock_sleep():
    with patch('tasks.time.sleep', return_value=None):
        yield

# Testes Task Somar
def test_somar_numeros_positivos(mock_sleep):
    resultado = somar(2, 3)
    assert resultado == 5

def test_somar_numeros_negativos(mock_sleep):
    resultado = somar(-2, -3)
    assert resultado == -5

def test_somar_com_zero(mock_sleep):
    resultado = somar(10, 0)
    assert resultado == 10

# Testes Task Fatorial
def test_fatorial_numero_positivo(mock_sleep):
    resultado = fatorial(5)
    assert resultado == 120

def test_fatorial_zero(mock_sleep):
    resultado =  fatorial(0)
    assert resultado == 1

def test_fatorial_numero_negativo(mock_sleep):
    with pytest.raises(ValueError, match='Número inválido!'):
        fatorial(-5)

# Teste Endpoints
client = TestClient(app)

def test_calcular_soma(mocker):
    mock_somar_delay = mocker.patch('tasks.somar.delay')
    mock_redis_lpush = mocker.patch('main.redis_client.lpush')
    mock_redis_ltrim = mocker.patch('main.redis_client.ltrim')
    mock_somar_delay.return_value.id = 'fake-task-id'

    response = client.post('/calcular/soma', params={'a':2, 'b':3})

    assert response.status_code == 200
    assert response.json() == {
        'task_id':'fake-task-id',
        'message':'Tarefa de soma enviada para execução!'
    }

    mock_redis_lpush.assert_called_once()
    mock_redis_ltrim.assert_called_once()

def test_calcular_fatorial(mocker):
    mock_fatorial_delay = mocker.patch('tasks.fatorial.delay')
    mock_redis_lpush = mocker.patch('main.redis_client.lpush')
    mock_redis_ltrim = mocker.patch('main.redis_client.ltrim')
    mock_fatorial_delay.return_value.id = 'fake-task-id'

    response = client.post('/calcular/fatorial', params={'n': 5})

    assert response.status_code == 200

    assert response.json() == {
        'task_id':'fake-task-id',
        'message':'Tarefa de fatorial enviada para execução!'
    }

    mock_redis_lpush.assert_called_once()
    mock_redis_ltrim.assert_called_once()