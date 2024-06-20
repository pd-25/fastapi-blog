from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, ShowBlog
from db.models.blog import Blog
from typing import List


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
    blog = db.query(Blog).filter(Blog.id==id).first()
    return blog

def retrieve_all_blogs(db: Session) -> List[Blog]:
    return db.query(Blog).filter(Blog.is_active==True).all()
