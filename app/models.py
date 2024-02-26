from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from  flask import  url_for
db = SQLAlchemy()

class Category(db.Model):
    __tablename__= 'category'
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    pro = db.relationship('Product', backref='category_name', lazy=True)

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def get_all_category(cls):
        return cls.query.all()

    @classmethod
    def delete_category_by_id(cls, id):
        return cls.query.get_or_404(id)
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String, nullable=True)
    details = db.Column(db.String, nullable=True)
    no_of_Pages = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())

    Category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=True)


    def __str__(self):
        return self.name


    @property
    def image_url(self):
        return url_for('static',filename=f'books/images/{self.image}')

    @property
    def show_url(self):
        return url_for("products.show",id=self.id)

    @property
    def index_url(self):
        return url_for("products.product_index")

    @classmethod
    def get_all_objects(cls):
        return cls.query.all()
    @classmethod
    def get_product_by_id(cls,id):
        return cls.query.get_or_404(id)

    @classmethod
    def save_product(cls,request_data):
        product=cls(**request_data)
        db.session.add(product)
        db.session.commit()
        return product

    @classmethod
    def delete_product(cls,id):
        prd = cls.query.get_or_404(id)
        db.session.delete(prd)
        db.session.commit()
        return True