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

from datetime import timedelta, datetime, timezone
from flask import session
from utils.constant import SESSION_ALIVE_TIME_MINUTES

def get_user_id():
    return session.get("user_id")

def is_doctor():
    return session.get("is_doctor")

def get_session_ending_time():
    return session.get("session_end_time")

def initialize_session(user_id, is_doctor):
    session["user_id"] = user_id
    session["is_doctor"] = is_doctor
    # Initializing session ending time to current time + minutes set as SESSION_ALIVE_TIME_MINUTES
    session["session_end_time"] = datetime.now(timezone.utc) + timedelta(minutes=SESSION_ALIVE_TIME_MINUTES)
    # if there was failed attempts to login, filled username deletion from the session
    session.pop("filled_username", None)

def logout_user():
    session.pop("user_id", None)
    session.pop("is_doctor", None)
    session.pop("session_end_time", None)

def set_username_after_login_failure(username):
    session["filled_username"] = username

def initialize_failed_registering_attempt_data(form):
    """If registration has failed with incorrect data format, filled input fields saved to session"""
    session["register_username"] = form["username"]
    session["register_password"] = form["password"]
    session["register_name"] = form["name"]
    session["register_email"] = form["email"]
    session["register_phone"] = form["phone"]
    session["register_address"] = form["address"]
    session["register_city"] = form["city"]
    session["register_country"] = form["country"]

def delete_failed_registration_attempt_data():
    """Deleting information saved from failed registration attempts after registration succeeded"""
    session.pop("register_username", None)
    session.pop("register_password", None)
    session.pop("register_name", None)
    session.pop("register_email", None)
    session.pop("register_phone", None)
    session.pop("register_address", None)
    session.pop("register_city", None)
    session.pop("register_country", None)