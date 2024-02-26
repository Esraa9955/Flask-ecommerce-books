from  app.category import  category_blueprint
from  app.models import Category
from  flask import  render_template
@category_blueprint.route('/home',methods=['GET'],endpoint='home')
def categor_home():
    return "<h1>welcom to home</h2>"

@category_blueprint.route('/', methods=['GET'],endpoint='index')
def categoy_index():
    categories=Category.get_all_category()
    return render_template('categories/index.html',categories=categories)
