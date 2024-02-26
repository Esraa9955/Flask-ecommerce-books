from flask_restful import reqparse
product_parser = reqparse.RequestParser()
product_parser.add_argument('name', type=str, required=True, help='Name of the book is required')
product_parser.add_argument('image', type=str)
product_parser.add_argument('no_of_Pages', type=int)
product_parser.add_argument('price', type=float)
product_parser.add_argument('Category_id', type=int)