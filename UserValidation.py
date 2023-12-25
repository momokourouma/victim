from pydantic import Field, BaseModel, EmailStr
from HashingPassword import hashingPassword
from typing import List, Optional, Annotated



class Validation(BaseModel):
    email: EmailStr
    password: str