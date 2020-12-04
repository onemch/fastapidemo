from fastapi import FastAPI
from routers import users

app = FastAPI()

app.include_router(users.router)


@app.get('/')
def welcome():
    return 'welcome'


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8099)
