from app.utils.security import hash_password, verify_password

def test_hash_and_verify():
    password = "supersecure"
    hashed = hash_password(password)
    assert verify_password(password, hashed)
