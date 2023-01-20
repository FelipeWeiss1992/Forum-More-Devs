from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import data_required, Length, Email, EqualTo, ValidationError
from models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[data_required()])
    email = StringField('E-mail', validators=[data_required(), Email()])
    senha = PasswordField('Senha', validators=[data_required(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha',validators=[data_required(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[data_required(), Email()])
    senha = PasswordField('Senha', validators=[data_required(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[data_required()])
    email = StringField('E-mail', validators=[data_required(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    curso_excel = BooleanField('Curso Excel')
    curso_vba = BooleanField('Curso VBA')
    curso_powerbi = BooleanField('Curso Power BI')
    curso_python = BooleanField('Curso Python')
    curso_sql = BooleanField('Curso SQL')
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('E-mail já cadastrado')
        
