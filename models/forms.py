from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import data_required, Length, Email, EqualTo, ValidationError
from models.forms import *
from flask_login import current_user

class FormCriarSubPost(FlaskForm):
    description = TextAreaField('', validators=[data_required()])
    botao_submit_criarsubpost = SubmitField('Responder Post')


class FormCriarPost(FlaskForm):
    title = StringField('Titulo', validators=[data_required()])
    description = TextAreaField('Post', validators=[data_required()])
    botao_submit_criarpost = SubmitField('Criar Post')



class FormCriarConta(FlaskForm):
    user_name = StringField('Nome de Usuário', validators=[data_required()])
    name = StringField('Nome Completo', validators=[data_required()])
    password1 = PasswordField('Senha', validators=[data_required()])
    password2 = PasswordField('Confirmação da Senha',validators=[data_required(), EqualTo('senha')])
    admin = BooleanField('Admin')
    botao_submit_criarconta = SubmitField('Criar Conta')

class FormLogin(FlaskForm):
    user_name = StringField('Nome de Usuário', validators=[data_required()])
    password = PasswordField('Senha', validators=[data_required()])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[data_required()])
    email = StringField('E-mail', validators=[data_required(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    java = BooleanField('Java')
    python = BooleanField('Python')
    html = BooleanField('HTML')
    javascript = BooleanField('JavaScript')
    sql = BooleanField('SQL')
    botao_submit_editarperfil = SubmitField('Confirmar Edição')
