import jwt
from datetime import datetime, timedelta
import os

SECRET = os.getenv("JWT_SECRET", "supersecret")

payload = {
    "service": "api",
    "exp": datetime.utcnow() + timedelta(minutes=10)   # Token expires in 10 minutes
}

token = jwt.encode(payload, SECRET, algorithm="HS256")

print("Your Token:")
print(token)
