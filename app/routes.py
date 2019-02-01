#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import os

from flask import render_template, jsonify, request
from grandpy.app import GrandpyApplication
from app.forms import QuestionForm
from app import app


@app.route('/', methods=['GET'])
def ask_question():
    form = QuestionForm()
    key = os.getenv("GOOGLE")
    return render_template('question.html', title='Site de Grandpy',
        form=form, key=key)


@app.route('/answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    question = data["question"]
    application = GrandpyApplication(question)
    return jsonify(application.get_answer())
