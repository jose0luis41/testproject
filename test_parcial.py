import pytest
import json, files

@pytest.fixture
def client(request):
    client = files.app.test_client()
    return client

@pytest.mark.order1
def test_Uno(client):
    testUno = {'filename': 'fileUno', 'content': 'ContenidoUno'}
    testDos = {'filename': 'fileDos', 'content': 'ContenidoDos'}
    ejecucionUno = client.post('/v1.0/files', data = json.dumps(testUno), content_type='application/json')
    ejecucionDos = client.post('/v1.0/files', data = json.dumps(testDos), content_type='application/json')
    assert ejecucionUno.status == '201 CREATED'
    assert ejecucionDos.status == '201 CREATED'
    ejecucionTres = client.get('/v1.0/files', follow_redirects=True)
    assert "fileUno" in ejecucionTres.data
    assert "fileDos" in ejecucionTres.data
    
@pytest.mark.order2
def test_Dos(client):
    testUno  = {'filename': '', 'content':'ContenidoUno'}
    testDos  = {'filename': 'fileUno', 'content':''}
    ejecucionUno = client.post('/v1.0/files', data = json.dumps(testUno), content_type='application/json')
    ejecucionDos = client.post('/v1.0/files', data = json.dumps(testDos), content_type='application/json')
    assert ejecucionUno.status == '400 BAD REQUEST'
    assert ejecucionDos.status == '400 BAD REQUEST'
  
@pytest.mark.order3
def test_Tres(client):
    ejecucion = client.get('/v1.0/files',follow_redirects=True)
    assert "fileUno" in ejecucion.data
    assert "fileDos" in ejecucion.data  
  
@pytest.mark.order4
def test_Cuatro(client):
    ejecucion = client.get('/v1.0/files/recently_created',follow_redirects=True)
    assert "fileDos" in ejecucion.data
    assert "fileUno" in ejecucion.data

@pytest.mark.order5
def test_Cinco(client):
    client.delete('/v1.0/files', follow_redirects=True)
    ejecucion = client.get('/v1.0/files',follow_redirects=True)
    assert "fileUno" not in ejecucion.data
    assert "fileDos" not in ejecucion.data
