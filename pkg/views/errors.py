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

from flask import render_template, jsonify, Blueprint
from flask_wtf.csrf import CSRFError
from sqlalchemy.exc import SQLAlchemyError

errors_bp = Blueprint("error", __name__)

@errors_bp.app_errorhandler(CSRFError)
def csrf_error(error):
    return jsonify(error=str(error)), 400

@errors_bp.app_errorhandler(KeyError)
def key_error(error):
    return jsonify(error=str(error)), 400

@errors_bp.app_errorhandler(401)
def user_not_authorized(error):
    return jsonify(error=str(error)), 401

@errors_bp.app_errorhandler(404)
def page_not_found(error):
    return render_template("error/404.html"), 404

@errors_bp.app_errorhandler(405)
def not_allowed_method(error):
    return jsonify(error=str(error)), 405

@errors_bp.app_errorhandler(500)
def internal_server_error(error):
    return render_template("error/500.html"), 500

@errors_bp.app_errorhandler(SQLAlchemyError)
def database_error(error):
    # logging could be done here for
    return jsonify(error="Something went wrong with DB operation."), 500