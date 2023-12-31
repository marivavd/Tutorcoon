from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, BooleanField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    status = StringField('Ваш статус', validators=[DataRequired()])
    phone_number = StringField('Номер телефона', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


    def get_public(self):
        return {'name': self.name.data,
                'surname': self.surname.data,
                'email': self.email.data,
                'phone_number': self.phone_number.data,
                'password': self.password.data,
                'status': self.status.data}



    def check_password(self, that):
        return self.password.data == that

    def check_password_again(self):
        return self.password.data == self.password_again.data


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Доступ')