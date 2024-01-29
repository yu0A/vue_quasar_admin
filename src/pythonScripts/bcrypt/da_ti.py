import bcrypt


key = bcrypt.kdf(
        password=b'password',
        salt=b'salt',
        desired_key_bytes=32,
        rounds=100)
key