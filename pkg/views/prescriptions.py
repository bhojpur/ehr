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
from services import prescriptions_service
from utils.constant import SUCCESS_CATEGORY, DANGER_CATEGORY
from utils.validators.auth_validator import requires_doctor_role, requires_session_time_alive

NEW_PRESCRIPTION_ADDED_MESSAGE = "New prescription created successfully!"
ADDED_PRESCRIPTION_TO_PATIENT_MESSAGE = "Prescription added to patient successfully!"
DELETED_PRESCRIPTION_FROM_PATIENT_MESSAGE = "Prescription removed from patient successfully!"

FAILED_PRESCRIPTION_CREATION_MESSAGE = "Prescription couldn't be created!"

prescriptions_bp = Blueprint("prescriptions", __name__)

@prescriptions_bp.route("/create-prescription", methods=["POST"])
@requires_doctor_role
@requires_session_time_alive
def create_prescription():
    is_success = prescriptions_service.create_new_prescription(request.form["prescription_name"],
                                                               request.form["amount_per_day"])
    if is_success:
        flash(NEW_PRESCRIPTION_ADDED_MESSAGE, SUCCESS_CATEGORY)               
    else:
        flash(FAILED_PRESCRIPTION_CREATION_MESSAGE, DANGER_CATEGORY)  
    return redirect("/profile")

@prescriptions_bp.route("/appointment/<int:appli_id>/prescription/<int:prescription_id>/patient/<int:user_id>", methods=["POST"])
@requires_doctor_role
@requires_session_time_alive
def update_user_prescription(appli_id, prescription_id, user_id):
    is_visible = request.form["is_visible"] == "True"
    prescriptions_service.update_prescription_from_user(user_id,
                                                        prescription_id,
                                                        is_visible)
    if is_visible:
        flash(ADDED_PRESCRIPTION_TO_PATIENT_MESSAGE, SUCCESS_CATEGORY)                       
    else:
        flash(DELETED_PRESCRIPTION_FROM_PATIENT_MESSAGE, SUCCESS_CATEGORY)                       
    return redirect(f"/appointment/{appli_id}/patient/{user_id}")