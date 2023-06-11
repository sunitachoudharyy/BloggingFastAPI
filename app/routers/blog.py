from fastapi import FastAPI, Response, status, HTTPException, Depends,APIRouter
from sqlalchemy.orm import Session
from typing import List,Optional
from .. import models, schemas, oauth2
from ..database import get_db
from sqlalchemy import func

router = APIRouter(
    prefix= "/blogs", 
    tags = ['Blogs']
)

@router.get("/",  response_model= List[schemas.BlogOut])

def get_blogs(db: Session = Depends(get_db), current_user: int= Depends(oauth2.get_current_user),
Limit: int = 10,skip: int = 0,search:Optional[str] = ""):
    # cursor.execute("""SELECT * FROM blogs""")
    # blogs = cursor.fetchall()
    # print(blogs)
    print(search)

    # blogs = db.query(models.Blog).filter(models.Blog.title.contains(search)).limit(Limit).offset(skip).all()

    blogs = db.query(models.Blog, func.count(models.Vote.blog_id).label("votes")).join(
         models.Vote, models.Vote.blog_id == models.Blog.id, isouter=True).group_by(models.Blog.id).filter(models.Blog.title.contains(search)).limit(Limit).offset(skip).all()
     

    return blogs
    


@router.post("/", status_code= status.HTTP_201_CREATED, response_model= schemas.Blog)
def create_blogs(blog: schemas.BlogCreate, db: Session = Depends(get_db), current_user: int= Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO blogs (title,content, published) VALUES (%s, %s, %s) RETURNING * """,
    #                (blog.title, blog.content, blog.published))
    # new_blog = cursor.fetchone()

    # conn.commit()
   
    new_blog = models.Blog(owner_id=current_user.id, **blog.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog
   

@router.get("/{id}", response_model= schemas.BlogOut)
def get_blog(id: int, db: Session = Depends(get_db),  current_user: int= Depends(oauth2.get_current_user)):
    #  cursor.execute("""SELECT * FROM blogs WHERE id = %s""", (str(id),))
    #  blog = cursor.fetchone()
    #   
    #  blog = db.query(models.Blog).filter(models.Blog.id == id).first()
     blog =  db.query(models.Blog, func.count(models.Vote.blog_id).label("votes")).join(
         models.Vote, models.Vote.blog_id == models.Blog.id, isouter=True).group_by(models.Blog.id).filter(models.Blog.id == id).first()

     if not blog:
         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                             detail = f"blog with id: {id} was not found")
     
     
     return  blog



@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_blog(id : int, db: Session = Depends(get_db),  current_user: int= Depends(oauth2.get_current_user)):

    # cursor.execute(
    #     """ DELETE FROM blogs WHERE id =  %s returning *""", (str(id),))
    # deleted_blog = cursor.fetchone()
    # conn.commit()
    
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    
    blog = blog_query.first()

    if blog == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= f"blog with id: {id} does not exist")
    
    if blog.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    
    blog_query.delete(synchronize_session=False)
    db.commit()
   
    return Response (status_code= status.HTTP_204_NO_CONTENT)



@router.put("/{id}",  response_model=schemas.Blog)
def update_blog(id:int, updated_blog: schemas.BlogCreate, db: Session = Depends(get_db), current_user: int= Depends(oauth2.get_current_user)):

    
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    
    blog = blog_query.first()


    if blog == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= f"blog with id: {id} does not exist")
    
    if blog.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    
    blog_query.update(updated_blog.dict(), synchronize_session=False)
   
    db.commit()

    return  blog_query.first()



