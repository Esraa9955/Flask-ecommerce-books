from flask import Flask
from flask import request,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #Initialize the application  in the main of the current module
books=[{"id":1, "name":"math","image":"1.png"},{"id":2, "name":"arbic","image":"2.png"},{"id":3, "name":"physics","image":"3.png"}]

name='esraa'
print(name)
@app.route("/")
def hello_Ghaza():
  return "<h1 style='color:red' >Hello form main page</h1>"




@app.route("/stor")
def get_books():
  print(request)
  return books

@app.route("/stor/<int:id>")

def book_profile(id):
  bks=list(filter(lambda book: book['id'] == id, books))
  if bks:
    return  bks[0]
  return "book not found"


#  for book in books:
#    if book["id"] ==id:
#      return book
#  return "book not found"

def customRoute():
  return"welcome to Custom Route"

app.add_url_rule("/custom",view_func=customRoute)


@app.route("/products",endpoint='prducts.index')
def products_index():
  products = Product.query.all()
  return render_template("products/index.html",products=products)

@app.route("/products/<int:id>",endpoint="product.show")
def products_show(id):
  product = Product.query.get_or_404(id)
  return render_template("products/show.html",product=product)

@app.errorhandler(404)
def get_404(error):
  return render_template("error/error404.html")


@app.route("/products/create",methods =['GET', 'POST'], endpoint='product.create')
def create_product():
    ## post
    print(request.form)
    if request.method == 'POST':
        product = Product(name=request.form['name'], image=request.form['image'])
        db.session.add(product)
        db.session.commit()
        # return "Saved
        return redirect(url_for('prducts.index'))
    return render_template("products/create.html")
@app.route("/bks/home")
def books_home():
  return render_template("/books/home.html",name="esraa",books=books)

@app.route("/test",endpoint="test_url")
def test():
  return "test"
@app.route("/books/land")
def books_land():
  return render_template("books/landing.html",books=books)

@app.route("/books/<int:id>",endpoint="book_show")
def show_book(id):
  bks=list(filter(lambda book: book['id'] == id, books))
  if bks:
    return  render_template("books/profile.html",book=bks[0])
  return "book not found"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db=SQLAlchemy(app)

class Product(db.Model):
  __tablename__ = "products"
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String) 
  image= db.Column(db.String,nullable=True)


  def __str__(self):
    return f"{self.name}"
if __name__ == '__main__':
  
  app.run(debug=True)


