from flask_wtf import FlaskForm
from wtforms import StringField,DecimalField,TextAreaField,SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField,FileAllowed,FileRequired
class PropertyForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    bedrooms = DecimalField('Number of Bedrooms',validators=[DataRequired()])
    location = StringField('Location',validators=[DataRequired()])
    price  = DecimalField('Price',validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    houseType = SelectField('Type', validators=[DataRequired()],choices=[('ho','House'),('apt','Apartment')])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'],'Images Only')])
    