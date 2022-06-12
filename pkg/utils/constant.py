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

TIME_FORMAT='DD-MM-YYYY HH:MI'
SESSION_ALIVE_TIME_MINUTES = 15
# DB Table user_info keys
NAME_DB_KEY='name'
PHONE_DB_KEY='phone'
ADDRESS_DB_KEY='address'
EMAIL_DB_KEY='email'
COUNTRY_DB_KEY='country'
CITY_DB_KEY='city'
PERSONAL_DOCTOR_ID_DB_KEY='personal_doctor_id'

# Avatar url
DOCTOR_AVATAR_URL='/static/images/doctorAvatar.png'
PATIENT_AVATAR_URL='/static/images/patientAvatar.png'

# Flash categories
SUCCESS_CATEGORY = "success"
DANGER_CATEGORY = "danger"

# Validator lengths
PRESCRIPTION_NAME_LENGTH_MAX = 30
APPOINTMENT_TYPE_LENGTH_MAX = 30
MESSAGE_LENGTH_MAX = 300
SYMPTOM_LENGTH_MAX = 500