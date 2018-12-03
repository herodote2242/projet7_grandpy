#!/usr/bin/env python3
# -*- coding: Utf-8 -*

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    gp_question = StringField('Posez une question à Grandpy !',
                              validators=[DataRequired()])
    submit = SubmitField('Demander')
