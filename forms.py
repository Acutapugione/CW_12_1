from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisterForm(FlaskForm):
    name = StringField(
        "Ім'я:",
        validators=[
            DataRequired("Ім'я"),
            Length(min=1, message="Треба хоча б 1 символи"),
        ],
    )
    password = PasswordField(
        "Пароль:",
        validators=[
            DataRequired("Пароль"),
        ],
    )
    password_confirm = PasswordField(
        "Підтвердіть пароль:",
        validators=[
            DataRequired("Знову пароль"),
            EqualTo('password')
        ],
    )
    submit = SubmitField("Зареєструватися")