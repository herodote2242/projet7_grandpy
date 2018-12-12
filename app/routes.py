#!/usr/bin/env python3
# -*- coding: Utf-8 -*

from flask import render_template, flash, redirect
from app import app
from app.forms import QuestionForm
from flask.json import jsonify


@app.route('/', methods=['GET'])
def ask_question():
    form = QuestionForm()
    return render_template('question.html', title='Site de Grandpy', form=form)


@app.route('/answer', methods=['POST'])
def get_answer():
    form = QuestionForm()
    if form.validate_on_submit():
        return redirect('/')
    # supprimer la partie en dessous qui considère que le formulaire est valable.
    else:
        flash('Rédigez la question dans la boîte !')
    return render_template('answer.html', title='Réponse de Grandpy')
