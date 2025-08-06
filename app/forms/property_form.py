from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, FileField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=120)])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), Length(max=200)])
    area = StringField('Area', validators=[DataRequired(), Length(max=100)])
    city = StringField('City', validators=[DataRequired(), Length(max=100)])
    price = FloatField('Price per Night', validators=[DataRequired(), NumberRange(min=0)])
    max_guests = IntegerField('Max Guests', validators=[DataRequired(), NumberRange(min=1)])
    
    status = SelectField('Status', choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected')
    ], default='active')
    image = FileField('Property Photo', validators=[Optional()])
    submit = SubmitField('List Property')