from httpx import AsyncClient


async def test_add_specifit_operations(ac: AsyncClient):
    response = await ac.post('/operations', json={
        'id':2,
        'quantity': '25.5',
        'figi': 'figi_CODE',
        'instrument_type': 'bond',
        'date': '2023-06-19T00:00:00',
        'type': 'Выплата купонов',
    })

    assert response.status_code == 200

async def test_get_specific_operations(ac:AsyncClient):
    responce = await ac.get('/operations', params={
        "operations_type": 'Выплата купонов',
    })

    assert responce.status_code == 200
    assert responce.json()['status'] == 'success'
    assert len(responce.json()['data']) == 1