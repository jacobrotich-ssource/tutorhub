from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str 
    price: float

@app.post('/items/')
def create_item(item: Item):
    return {"name": item.name, "price": item.price}

@app.get('/items/')
def get_item(name: str, price: float):
    return {"name": item.name, "price": item.price}

@app.get("/about")
def about():
    return {
        "name": "StudyHub",
        "purpose": "Learning backend development",
    }

@app.get("/health/db")
def database_health(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable",
        ) from None

    return {
        "status": "ok",
        "database": "reachable",
    }