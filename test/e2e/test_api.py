# test_api.py
import uuid
import pytest
import requests

def post_to_add_batch(ref, sku, qty, eta):
	url = config.get_api_url()
	r = requests.post(
		f'{url}/add_batch',
		json={'ref': ref, 'sku': sku, 'qty': qty, 'eta': eta})
	assert r.status_code == 201


@pytest.mark.usefixtures('postgres_db')
@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_201_and_allocated_batch():
	sku, othersku = random_sku(), random_sku('other')
	earlybatch = random_batchref(1)
	laterbatch = random_batchref(2)
	otherbatch = random_batchref(3)
	post_to_add_batch(laterbatch, sku, 100, '2011-01-02')
	post_to_add_batch(earlybatch, sku, 100, '2011-01-01')
	post_to_add_batch(otherbatch, othersku, 100, None)
	data = {'orderid': random_orderid(id), 'sku':sku, 'qty': 3}
	url = config.get_api_url()
	r = requests.post(f'{url}/allocate', json=data)
	assert r.status_code == 201
	assert r.json()['batchref'] == earlybatch