from fastapi import FastAPI
from app.database.connection import Base, engine, SessionLocal
from app.models.product import Product
from app.schemas.products import ProductRequest

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API funcionando"}

# Products
@app.post("/product/create")
def create_product(product_request: ProductRequest):

    db = SessionLocal()

    new_product = Product(
        name=product_request.name,
        price=product_request.price,
        quantity=product_request.quantity
        )
    
    db.add(new_product)
    db.commit()
    db.close()
    
    return f"{new_product}"

@app.get("/products/list")
def list_products():

    db = SessionLocal()

    products_list = db.query(Product).all()
    db.close()
    
    return products_list

@app.get("/product/{id}")
def select_product(id: int):

    db = SessionLocal()
    product = db.query(Product).filter(Product.id == id).first()
    
    db.close()

    if product is None:
        return {"error": "Produto não encontrado"}
    
    return product

@app.delete("/product/delete/{id}")
def delete_product(id: int):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == id).first()

    if product is None:
        db.close()
        return {"error": "Produto não encontrado"}
    
    db.delete(product)
    db.commit()
    db.close()

    return product

@app.patch("/products/update/{id}")
def update_product(product_request: ProductRequest, id: int):

    db = SessionLocal()
    
    product = db.query(Product).filter(Product.id == id).first()
    product.name = product_request.name
    product.price = product_request.price
    product.quantity = product_request.quantity
    
    db.commit()
    db.refresh(product)
    db.close()

    return product