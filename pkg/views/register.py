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

from flask import redirect, request, render_template, Blueprint, flash
from services import users_service, session_service
from utils.constant import SUCCESS_CATEGORY, DANGER_CATEGORY
from utils.validators.models.registration_user import RegistrationUser

FAILED_USER_REGISTRATION_MESSAGE = "Something went wrong!"
SUCCESFULLY_USER_REGISTRATION_MESSAGE = "New user succesfully registered!"

register_bp = Blueprint("register", __name__)

@register_bp.route("/register")
def register_page():
    return render_template("auth/register-page.html")

@register_bp.route("/register/user", methods=["POST"])
def register_user():
    # the RegistrationUser class handles the validation of the form inputs
    try:
        user_validated = RegistrationUser(request.form)
    except ValueError as error:
        flash(str(error), DANGER_CATEGORY)
        session_service.initialize_failed_registering_attempt_data(request.form)
        return redirect("/register")

    created_user_id = users_service.create_new_user(user_validated)
    if not created_user_id:
        flash(FAILED_USER_REGISTRATION_MESSAGE, DANGER_CATEGORY)
        return redirect("/register")
        
    users_service.initialize_user_info_values(created_user_id, user_validated)
    session_service.initialize_session(created_user_id, user_validated.is_doctor)
    session_service.delete_failed_registration_attempt_data()
    flash(SUCCESFULLY_USER_REGISTRATION_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/profile")