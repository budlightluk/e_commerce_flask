from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import DataRequired, Email, Length


class CheckoutForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=150)])
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=255)])
    credit_card_number = StringField('Credit Card Number', validators=[DataRequired()])
    submit = SubmitField('Place Order')
