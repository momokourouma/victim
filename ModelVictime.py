from typing import List, Optional, Annotated, Union
from pydantic import BaseModel, Field, EmailStr


# PyObjectId = Annotated[str, BeforeValidator(str)]


class VictimeModel(BaseModel):
    nom: str = Field(max_length=30)
    prenom: str = Field(max_length=20)
    adresse: str = Field(max_length=50)
    telephone: str = Field(max_length=30)
    indication: str = Field(max_length=10)
    description: str = Field(max_length=10)
    perte: Union[int, float] = Field(union="left_to_right")
    carte: str = Field(max_length=20)
    statut: Optional[bool] = Field(default=False)


class UpdateVictim(BaseModel):
    nom: Optional[str]
    prenom: Optional[str]
    adresse: Optional[str]
    telephone: Optional[str]
    indication: Optional[str]
    description: Optional[str]
    perte: Optional[Union[int, float]]
    carte: Optional[str]
    statut: Optional[bool]

class Authentification(BaseModel):
    email: EmailStr
    nom: str
    prenom: str
    telephone : str
    password: str