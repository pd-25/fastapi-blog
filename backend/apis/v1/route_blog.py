from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.blog import CreateBlog, ShowBlog
from db.repository.blog import create_new_blog, retrive_blog, retrieve_all_blogs
from typing import List, Optional

router = APIRouter()

@router.post("/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog 

# @router.get("/{id}", response_model=ShowBlog)
# def get_blog(id: int, db: Session = Depends(get_db)):
#     blog = retrive_blog(id=id, db=db)
#     if not blog:
#         raise HTTPException(detail=f"Blog with {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
#     return blog

@router.get("/", response_model=List[ShowBlog])
@router.get("/{id}", response_model=ShowBlog)
def get_blog(id: Optional[int] = None, db: Session = Depends(get_db)):
    if id:
        blog = retrive_blog(id=id, db=db)
        if not blog:
            raise HTTPException(detail=f"Blog with ID {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
        return blog
    else:
        blogs = retrieve_all_blogs(db=db)
        return blogs
