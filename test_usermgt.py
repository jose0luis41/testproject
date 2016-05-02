import pytest
import usermgt

@pytest.fixture
def client(request):
    client = usermgt.app.test_client()
    return client

def get_users(client):
	return client.get('/api/v1.0/usermgt/users',follow_redirects=True)

def test_get_users(client):
	result = get_users(client)
	assert b'operativos' in result.data


