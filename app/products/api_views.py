from app.products import product_blueprint
from app.models import Product, db
from flask_restful import Resource, Api, fields, marshal_with
from flask import request
from app.products.parsers import product_parser


@product_blueprint.route("/api", endpoint="api")
def get_product():
    product = Product.query.all()
    bks = []
    for bk in product:
        bk_data = bk.__dict__
        del bk_data["_sa_instance_state"]
        bks.append(bk_data)
    print(bks)
    return bks


category_serilizer = {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
}

product_serilizer = {
    "id": fields.Integer,
    "name": fields.String,
    "image": fields.String,
    "no_of_Pages": fields.Integer,
    "price": fields.Integer,
    "Category_id": fields.Integer,
    "category_name": fields.Nested(category_serilizer)
}


class ProductList(Resource):
    @marshal_with(product_serilizer)
    def get(self):
        product = Product.query.all()
        return product, 200

    @marshal_with(product_serilizer)
    def post(self):
        print(request.data)
        product_data = product_parser.parse_args()
        print(product_data)
        product = Product.save_product(product_data)
        return product, 201


class ProductResource(Resource):
    @marshal_with(product_serilizer)
    def get(self, id):
        product = Product.get_product_by_id(id)
        return product, 200

    @marshal_with(product_serilizer)
    def put(self):
        product = Product.get_book_by_id(id)
        if product:
            product_data = product_parser.parse_args()
            product.name = product_data["name"]
            product.image = product_data["image"]
            product.price = product_data["price"]
            product.no_of_Pages = product_data["no_of_Pages"]
            product.Category_id = product_data["Category_id"]
            db.session.add(product)
            db.session.commit()
            return product

    def delete(self, id):
        deleted = Product.get_product_by_id(id)
        return deleted, 204

