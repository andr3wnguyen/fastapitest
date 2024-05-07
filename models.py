from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)

    manuscripts = relationship("Manuscript", back_populates="author")


class Manuscript(Base):
    __tablename__ = "manuscripts"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    author_id = Column(String, ForeignKey("authors.id")) #author is uses authors table's id column

    author = relationship("Author", back_populates="manuscripts")
