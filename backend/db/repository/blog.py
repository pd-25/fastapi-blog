from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, ShowBlog, UpdateBlog
from db.models.blog import Blog
from typing import List

from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import logging
def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    # print(blog)
    # return
    blog = Blog(
        title=blog.title, slug=blog.slug, content=blog.content, author_id=author_id
    )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retrive_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog


def retrieve_all_blogs(db: Session) -> List[Blog]:
    return db.query(Blog).filter(Blog.is_active == True).all()


def update_blog_by_id(id: int, blog: UpdateBlog, db: Session, author_id: int = 1):
    try:
        print(id)
        blog_in_db = db.query(Blog).filter(Blog.id == id).first()

        if not blog_in_db:
            return

        blog_in_db.title = blog.title
        blog_in_db.content = blog.content

        db.add(blog_in_db)
        db.commit()
        
        return blog_in_db

    except SQLAlchemyError as e:
        logger.debug('insertion-Error', exc_info=e)
        raise HTTPException(status_code=500, detail="Insertion Error")

def delete_blog_by_id(id: int, db: Session, author_id: int):
    blog_in_db = db.query(Blog).filter(Blog.id==id)
    if not blog_in_db.first():
        return {"error":f"{id} not found in db"}
    blog_in_db.delete()
    db.commit()
    return {"msg":f"Blog with {id} deleted successfully"}