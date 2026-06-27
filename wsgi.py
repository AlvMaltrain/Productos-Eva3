import time
from app import app, init_db, get_db_connection

def _wait_for_db(retries= 30, delay=2):
    """Espera a que MYSQL acepte conexiones antes de inicializar"""
    for i in range(retries):
        conn = get_db_connection()
        if conn is not None:
            conn.close()
            print(f"[wsgi] DB disponible (intento {i + 1})")
            return True
        print(f"[wsgi] DB no disponible reintento {i + 1}/{retries}...")
        time.sleep(delay)
    return False

# Se ejecuta UNA sola vez (guinicorn --preload)
if _wait_for_db():
    init_db()
else:  
    print("[wsgi] ADVERTENCIA: no se pudo conectar a la DB al iniciar")

# gunicorn busca el objeto 'app'