from fastapi import FastAPI
from app.database.connection import Base, engine, SessionLocal
from app.models.product import Product

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API funcionando"}

@app.post("/create-product")
def create_product():

    db = SessionLocal()

    new_product = Product(
        name="Mouse",
        price=150.0,
        quantity=10
    )

    db.add(new_product)
    db.commit()
    db.close()
    
    return {"message": "Produto criado"}