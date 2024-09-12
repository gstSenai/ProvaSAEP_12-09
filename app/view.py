from app import app, db
from flask import render_template, redirect, url_for,flash
from app.models import Usuario, Tarefa
from app.forms import UsuarioForm, TarefaForm


@app.route("/")
def homepage():
    dados = Tarefa.query.order_by(Tarefa.nome_setor)
    context = {'dados': dados.all()}
    return render_template('index.html', context=context)

@app.route('/cadastro/usuario', methods=['GET', 'POST'])
def UserNovo():
    form = UsuarioForm()
    if form.validate_on_submit():
        form.save() 
        flash("Usuario Cadastrado com Sucesso") 
        return redirect(url_for('homepage'))
    return render_template('cadastro_usuario.html', form=form)

@app.route('/cadastro/tarefa', methods=['GET', 'POST'])
def TarefaNovo():
    form = TarefaForm()
    if form.validate_on_submit():
        form.save()
        flash("Tarefa Cadastrada com Sucesso")   
        return redirect(url_for('homepage'))
    return render_template('cadastro_tarefa.html', form=form)

@app.route('/post/delete/<int:tarefa_id>', methods=['POST'])
def delete_tarefa(tarefa_id):
    task = Tarefa.query.get_or_404(tarefa_id)
    db.session.delete(task)
    db.session.commit()  
    return redirect(url_for('homepage'))

@app.route('/editar/tarefa/<int:tarefa_id>', methods=['GET', 'POST'])
def editar_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    form = TarefaForm(obj=tarefa)
    if form.validate_on_submit():
        form.populate_obj(tarefa)
        db.session.commit()
        flash('Tarefa atualizada com sucesso!')
        return redirect(url_for('homepage'))

    return render_template('edit_task.html', form=form, tarefa=tarefa)



