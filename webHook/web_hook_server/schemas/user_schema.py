from pydantic import BaseModel

class user_schema(BaseModel):
    name: str
    ap_paterno: str
    email: str