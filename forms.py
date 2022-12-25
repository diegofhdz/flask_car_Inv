from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
import zxcvbn as zxc


class UserLoginForm(FlaskForm):

    def check_password(form, field):
        result = zxc.password_strength(field.data)
        if result < 3:
            raise ValidationError("Weak Password, try a stronger password")
        else:
            return True

    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), check_password])
    submit_button = SubmitField()