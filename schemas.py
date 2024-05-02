from pydantic import BaseModel

#basemodel will have everything needed - other classes inherit from it e.g. manuscriptBase has title, and Manuscript inherits this and adds id and owner_id
class ManuscriptBase(BaseModel):
    title: str


class ManuscriptCreate(ManuscriptBase):
    pass


class Manuscript(ManuscriptBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    email: str


class AuthorCreate(AuthorBase):
    name: str


class Author(AuthorBase):
    id: int
    manuscripts: list[Manuscript] = []

    class Config:
        orm_mode = True