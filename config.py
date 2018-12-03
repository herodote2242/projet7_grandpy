#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '15djeIJG76ps8A98nbd45Uj5'
