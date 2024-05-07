from sqlalchemy.orm import Session

import models
import schemas


def get_author(db: Session, user_id: int):
    return db.query(models.Author).filter(models.Author.id == id).first()


def get_author_by_email(db: Session, email: str):
    return db.query(models.Author).filter(models.Author.email == email).first()


def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_user = models.Author(email=author.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_manuscripts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Manuscript).offset(skip).limit(limit).all()


def create_user_manuscript(db: Session, item: schemas.ManuscriptCreate, user_id: int):
    db_item = models.Manuscript(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item