#!/usr/bin/env python3
# -*- coding: Utf-8 -*

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ResetField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    gp_question = StringField(validators=[DataRequired()])
    submit = SubmitField('Et zou !')
    reset = ResetField('Oups...')
