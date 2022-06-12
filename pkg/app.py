#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 Bhojpur Consulting Private Limited, India. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from os import getenv

app = Flask(__name__, static_folder="static", static_url_path='/static/')

#app.config["SECRET_KEY"] = "12345678"
#app.config['WTF_CSRF_SECRET_KEY'] = "12345678"
app.secret_key = getenv("SECRET_KEY")
app.config["WTF_CSRF_SECRET_KEY"] = getenv("WTF_CSRF_SECRET_KEY")
app.config["FLASK_ENV"] = getenv("FLASK_ENV")
csrf = CSRFProtect(app)

from views import appointments, auth, errors, messages, \
       prescriptions, profiles, register, settings

app.register_blueprint(appointments.appointments_bp)
app.register_blueprint(auth.auth_bp)
app.register_blueprint(errors.errors_bp)
app.register_blueprint(messages.messages_bp)
app.register_blueprint(prescriptions.prescriptions_bp)
app.register_blueprint(profiles.profiles_bp)
app.register_blueprint(register.register_bp)
app.register_blueprint(settings.settings_bp)