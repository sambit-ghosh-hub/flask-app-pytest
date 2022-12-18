import json
def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = {'text': 'Hello World changed yet again 2 18th dec'}
    assert expected == json.loads(res.get_data(as_text=True))
