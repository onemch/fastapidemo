from fastapi import APIRouter
from logging import exception
from typing import List
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from fastapi import FastAPI, HTTPException
from model import User
import db
from db import DB_User

router = APIRouter()


@router.get('/user', response_model=List[User])
async def selectUserList(db: Session = Depends(db.get_db)):
    userList = db.query(DB_User).all()
    return userList


@router.get('/user/{user_id}', response_model=User)
async def selectUserById(id: int, db: Session = Depends(db.get_db)):
    user = db.query(DB_User).filter(DB_User.id == id).first()
    return user


@router.post('/user', response_model=User)
async def insertUser(user: User, db: Session = Depends(db.get_db)):
    userDB = DB_User(**user.dict())
    db.add(userDB)
    # db.add(user)
    db.commit()
    # db.refresh()
    return user


@router.put('/user', response_model=User)
async def updateUser(user: User, db: Session = Depends(db.get_db)):
    selectUserById = db.query(DB_User).filter(DB_User.id == user.id).first()
    if selectUserById is None:
        raise HTTPException(status_code=404, detail="Don't exist user!!")

    selectUserById.username = user.username
    selectUserById.password = user.password
    selectUserById.email = user.email
    selectUserById.sex = user.sex

    db.commit()
    db.refresh(selectUserById)
    return selectUserById


@router.delete('/user')
async def deleteUser(id: int, db: Session = Depends(db.get_db)):
    selectUserById = db.query(DB_User).filter(DB_User.id == id).first()
    if selectUserById is None:
        raise HTTPException(status_code=404, detail="Don't exist user")

    db.delete(selectUserById)
    db.commit()
    return "OK"
