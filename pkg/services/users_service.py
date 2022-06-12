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

from repositories import users_repository
from utils.constant import NAME_DB_KEY, PHONE_DB_KEY, ADDRESS_DB_KEY, EMAIL_DB_KEY, \
     COUNTRY_DB_KEY, CITY_DB_KEY

def get_user_info(user_id):
    return {
        "name": get_user_info_by_key(user_id, NAME_DB_KEY),
        "phone": get_user_info_by_key(user_id, PHONE_DB_KEY),
        "email": get_user_info_by_key(user_id, EMAIL_DB_KEY),
        "address": get_user_info_by_key(user_id, ADDRESS_DB_KEY),
        "country": get_user_info_by_key(user_id, COUNTRY_DB_KEY),
        "city": get_user_info_by_key(user_id, CITY_DB_KEY)
    }

def get_user_personal_doctor_info(doctor_id):
    return {
        "name": get_user_info_by_key(doctor_id, NAME_DB_KEY),
        "phone": get_user_info_by_key(doctor_id, PHONE_DB_KEY),
        "id": doctor_id
    }

def get_user_info_by_key(user_id, key):
    """Fetches value from user_info table which is signed to the parameter (key).
       If fetched_value None -> key value is not set for the user_id"""
    fetched_value = users_repository.get_user_info_by_key(user_id, key)
    if fetched_value:
        return fetched_value[0]
    return "(unknown)"

def is_username_taken(username):
    return users_repository.is_username_taken(username)

def get_doctor_patients(doctor_id):
    fetched_patients = users_repository.get_doctor_patients(doctor_id)
    return format_users(fetched_patients)

def get_all_doctors():
    fetched_doctors = users_repository.get_all_doctors()
    return format_users(fetched_doctors)

def format_users(fetched_users):
    formatted_users = []
    for user in fetched_users:
        formatted_users.append({
            "user_id": user.user_id,
            "name": get_user_info_by_key(user.user_id, NAME_DB_KEY)
        })

    return formatted_users

def update_settings_values(user_id, user):
    "Updates user_info table values if user has filled the input with the request"
    if user.name:
        update_user_info_by_key(user_id, NAME_DB_KEY, user.name)

    if user.phone:
        update_user_info_by_key(user_id, PHONE_DB_KEY, user.phone)

    if user.email:
        update_user_info_by_key(user_id, EMAIL_DB_KEY, user.email)

    if user.address:
        update_user_info_by_key(user_id, ADDRESS_DB_KEY, user.address)

    if user.city:
        update_user_info_by_key(user_id, CITY_DB_KEY, user.city)

    if user.country:
        update_user_info_by_key(user_id, COUNTRY_DB_KEY, user.country)

def update_user_info_by_key(user_id, key, new_value):
    users_repository.update_user_info_by_key(user_id, key, new_value)

def create_new_user(user):
    return users_repository.create_new_user(user)

def initialize_user_info_values(user_id, user):
    return users_repository.initialize_user_info_values(user_id, user)