#!/usr/bin/env python3
# -*- coding: Utf-8 -*

from flask import render_template, jsonify, request
from grandpy.app import GrandpyApplication
from app.forms import QuestionForm
from app import app


@app.route('/', methods=['GET'])
def ask_question():
    form = QuestionForm()
    return render_template('question.html', title='Site de Grandpy', form=form)


@app.route('/answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    question = data["question"]
    application = GrandpyApplication(question)
    return jsonify(application.get_answer())
