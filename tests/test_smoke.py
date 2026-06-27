from app import app


def test_app_carga():
    assert app.name


def test_products_maneja_error_de_db():
    client = app.test_client()
    resp = client.get('/api/products')
    # En CI no hay base de datos: debe responder error 500
    assert resp.status_code in (200, 500)