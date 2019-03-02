#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import os


class Config(object):
    """
    To protect web forms of being attacked by cross-site request forgery,
    this secret key is known only by developpers and maintainers of th app.
    The first term 'SECRET_KEY' looks for the value in the environment
    variables, while the second is used if the first is not founded.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Sf45a21re_f55sfzrTY77-8lzoc'
