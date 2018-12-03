#!/usr/bin/env python3
# -*- coding: Utf-8 -*

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import QuestionForm
from flask.json import jsonify


@app.route('/')
@app.route('/question', methods=['GET', 'POST'])
def question_page():
    form = QuestionForm()
    if form.validate_on_submit():
        flash('Voici la réponse de Grandpy :'.format(form.gp_question.data))
        return redirect(url_for('question'))
    return render_template('question.html', title='Site de Grandpy', form=form)


@app.route('/answer')
def answer_page():
    return render_template('answer.html', title='Réponse de Grandpy')
