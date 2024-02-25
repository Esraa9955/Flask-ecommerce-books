from  flask import  render_template,request,redirect,url_for
from app.models import Product,db
from  app.products import product_blueprint


@product_blueprint.route('',endpoint='product_index')
def product_index():
    products = Product.get_all_objects()

    return render_template("products/index.html", products=products)

@product_blueprint.route("/<int:id>",endpoint="show")
def products_show(id):
    product = Product.get_product_by_id(id)
    return render_template("products/show.html",product=product)

@product_blueprint.route("/create",methods=['GET','POST'],endpoint="create")
def create_product():
    if request.method =='POST':
        product = Product(name=request.form['name'], image=request.form['image'],details=request.form['details'],no_of_Pages=request.form['pages'],price=request.form['price'])
        db.session.add(product)
        db.session.commit()
        #product=Product.save_product(request.form)
        #return redirect((url_for('product.show_url')))
        return  redirect(url_for('products.product_index'))
    return render_template("products/create.html")

@product_blueprint.route("delete/<int:id>", methods=['POST'], endpoint='delete')
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for('products.product_index'))

