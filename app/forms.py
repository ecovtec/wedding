from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email
from app.models import Guest


class RSVPForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={
                       "placeholder": "Name"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={
                        "placeholder": "Email"})
    attending = SelectField('Attending', choices=[
        ('yes', 'Yes'), ('no', 'No')])
    submit = SubmitField('Submit')

    def validate_email(self, email):
        guest = Guest.query.filter_by(email=email.data).first()
        if guest is not None:
            raise ValidationError('Email already used.')
