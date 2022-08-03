import base64
import hashlib
password = 'maks123456'
h = hashlib.sha256(password.encode())
print(base64.b64encode(h.digest()))