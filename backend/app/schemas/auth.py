from pydantic import BaseModel, EmailStr


# ===========================
# Login Request
# ===========================

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# ===========================
# Token Response
# ===========================

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ===========================
# Token Data
# ===========================

class TokenData(BaseModel):
    user_id: str