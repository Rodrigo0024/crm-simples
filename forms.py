from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ClienteForm(FlaskForm):
    nome = StringField("Nome", [validators.DataRequired()])
    email = StringField("Email", [validators.DataRequired(), validators.Email()])
    telefone = StringField("Telefone")