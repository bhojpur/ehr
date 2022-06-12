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

from flask import redirect, request, render_template, flash, Blueprint
from services import users_service, session_service
from utils.constant import DANGER_CATEGORY, SUCCESS_CATEGORY
from utils.validators.auth_validator import requires_login, requires_session_time_alive
from utils.validators.models.settings_user import SettingsUser

INFORMATION_UPDATED_MESSAGE = "Information updated successfully!"

settings_bp = Blueprint("settings", __name__)

@settings_bp.route("/settings")
@requires_login
@requires_session_time_alive
def settings():
    user_id = session_service.get_user_id()
    user_info = users_service.get_user_info(user_id)
    return render_template("settings/edit-settings-page.html",
                            user_info=user_info)

@settings_bp.route("/settings/update", methods=["POST"])
@requires_login
@requires_session_time_alive
def update_settings():
    user_id = session_service.get_user_id()
    try:
        user_validated = SettingsUser(request.form)
    except ValueError as error:
        flash(str(error), DANGER_CATEGORY)
        return redirect("/settings")

    users_service.update_settings_values(user_id, user_validated)
    flash(INFORMATION_UPDATED_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/settings")