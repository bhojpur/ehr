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

from flask import redirect, request, flash, Blueprint
from services import messages_service, session_service
from utils.constant import SUCCESS_CATEGORY, DANGER_CATEGORY
from utils.validators.auth_validator import requires_login, requires_session_time_alive

SUCCESS_SENT_MESSAGE = "Message sent successfully!"
UNSUCCESS_SENT_MESSAGE = "Couldn't deliver that message!"

messages_bp = Blueprint("message", __name__)

@messages_bp.route("/send-message", methods=["POST"])
@requires_login
@requires_session_time_alive
def send_message():
    sender_id = int(session_service.get_user_id())
    receiver_id = int(request.form["receiver_id"])
    is_success = messages_service.add_new_message(request.form["content"],
                                                  sender_id,
                                                  receiver_id)
    if is_success:
        flash(SUCCESS_SENT_MESSAGE, SUCCESS_CATEGORY)
    else:
        flash(UNSUCCESS_SENT_MESSAGE, DANGER_CATEGORY)
    return redirect("/profile")
    