from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from app.models import Category

class ProductForm(FlaskForm):
    name= StringField('Name', validators=[DataRequired()] )
    image= StringField("Image")
    no_of_Pages= IntegerField("Number of pages",validators=[DataRequired()])
    price= IntegerField("Price", validators=[DataRequired()])
    Category_id = QuerySelectField("Category", query_factory=lambda:Category.get_all_category())