from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Email, ValidationError
from app import db
from app.models import Usuario, Tarefa

class UsuarioForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    btnSubmit = SubmitField('Cadastrar')
    
    def validate_email(self, email):
        if Usuario.query.filter(Usuario.email == email.data).first():
            raise ValidationError('Usuário já cadastrado')
        
    def save(self):
        user = Usuario(
            nome = self.nome.data,
            email = self.email.data
        )
        db.session.add(user)
        db.session.commit()
        return user


class TarefaForm(FlaskForm):
    desc_tarefa = StringField('Descrição Tarefa:', validators=[DataRequired()])
    nome_setor = StringField('Setor:', validators=[DataRequired()])
    prioridade = SelectField('Prioridade:', choices=[("Baixa", "Baixa"),
                                                     ("Média", "Média"),
                                                     ("Alta", "Alta")], validators=[DataRequired()])
    data_cadastro = DateField('Data do Cadastro:', validators=[DataRequired()])
    status = SelectField('Status:', choices=[
        ('A fazer', 'A fazer'),
        ('Fazendo', 'Fazendo'),
        ('Pronto', 'Pronto')], validators=[DataRequired()])
    id_usuario = SelectField('Usuário Destinado:', coerce=int, validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')



    def __init__(self, *args, **kwargs):
        super(TarefaForm, self).__init__(*args, **kwargs)
        self.id_usuario.choices = [(usuario.id, usuario.nome) for usuario in Usuario.query.all()]

    def save(self):
        task = Tarefa(
            desc_tarefa=self.desc_tarefa.data,
            nome_setor=self.nome_setor.data,
            prioridade=self.prioridade.data,
            data_cadastro=self.data_cadastro.data,
            status=self.status.data,
            id_usuario=self.id_usuario.data
        )
        db.session.add(task)
        db.session.commit()