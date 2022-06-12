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

from datetime import datetime, timezone
from functools import wraps
from flask import redirect, flash, abort
from utils.constant import DANGER_CATEGORY
from services.appointments_service import is_appointment_signed_to_user
from services import session_service

MUST_SIGN_IN_MESSAGE = "No access to the page! Please sign in!"
SESSION_EXPIRED_MESSAGE = "Your session has expired! Please sign in again!"
NOT_AUTHORIZED_CALL_MESSAGE = "Not authorized call!"
NOT_AUTHORIZED_TO_THE_APPOINTMENT_PAGE ="Got lost? Nothing there for you!"

def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session_service.get_user_id() is None:
            flash(MUST_SIGN_IN_MESSAGE, DANGER_CATEGORY)
            return redirect("/sign-in")
        return f(*args, **kwargs)
    return decorated_function

def requires_doctor_role(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session_service.is_doctor():
            abort(401, description = NOT_AUTHORIZED_CALL_MESSAGE)
        return f(*args, **kwargs)
    return requires_login(decorated_function)

def requires_session_time_alive(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if has_session_expired():
            flash(SESSION_EXPIRED_MESSAGE, DANGER_CATEGORY)
            session_service.logout_user()
            return redirect("/sign-in")
        return f(*args, **kwargs)
    return decorated_function

def has_session_expired():
    return session_service.get_session_ending_time() < datetime.now(timezone.utc)

def requires_appointment_signed_to_user(f):
    """Validates that appointment id belonging to user and session user_id matching
       to patient_id given as url parameter.
       For doctor role these checks are not executed"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session_service.is_doctor():
            if not has_access_to_appointment(kwargs):
                flash(NOT_AUTHORIZED_TO_THE_APPOINTMENT_PAGE, DANGER_CATEGORY)
                return redirect("/profile")
        return f(*args, **kwargs)
    return decorated_function

def has_access_to_appointment(kwargs):
    appointment_id = int(kwargs["appo_id"])
    patient_id = int(kwargs["patient_id"])
    user_id = session_service.get_user_id()
    return user_id == patient_id \
            and is_appointment_signed_to_user(patient_id, appointment_id)