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

from database.db import db
from sqlalchemy.exc import SQLAlchemyError

USER_PRESCRIPTIONS_QUERY = "SELECT prescription_id, visible \
                            FROM   user_prescriptions \
                            WHERE  user_id = :user_id"

SINGLE_PRESCRIPTION_QUERY = "SELECT id, name, amount_per_day \
                             FROM   prescriptions \
                             WHERE  id = :prescription_id"

GET_PRESCRIPTIONS_OVERVIEW_QUERY = "SELECT \
                                        (SELECT value \
                                         FROM   user_info \
                                         WHERE  key = 'name' \
                                         AND    user_id = U.id) \
                                    AS user_name, \
                                    COUNT(Up.user_id) \
                                    AS current_prescriptions, \
                                    ABS(COUNT(Up.user_id) - (SELECT COUNT(id) \
                                                             FROM   user_prescriptions \
                                                             WHERE  user_id = U.id)) \
                                    AS past_prescriptions \
                                    FROM users U \
                                        LEFT JOIN user_prescriptions Up \
                                             ON  U.id = Up.user_id \
                                             AND Up.visible = TRUE \
                                        WHERE U.id IN \
                                                (SELECT user_id \
                                                 FROM   user_info \
                                                 WHERE  key = 'personal_doctor_id' \
                                                 AND    value = :doctor_id) \
                                    GROUP BY U.id \
                                    ORDER BY current_prescriptions DESC"
                                    
GET_ALL_NOT_SIGNED_PRESCRIPTIONS_QUERY = "SELECT id, name, amount_per_day \
                                          FROM   prescriptions \
                                          WHERE  id NOT IN \
                                                   (SELECT prescription_id \
                                                    FROM   user_prescriptions \
                                                    WHERE  user_id = :user_id \
                                                    AND    visible = TRUE)"

UPDATE_USER_PRESCRIPTION_QUERY = "UPDATE user_prescriptions \
                                  SET    visible = :visible \
                                  WHERE  user_id = :user_id \
                                  AND    prescription_id = :prescription_id"

ADD_USER_PRESCRIPTION_QUERY = "INSERT INTO user_prescriptions (prescription_id, user_id) \
                               VALUES (:prescription_id, :user_id)"

CREATE_NEW_PRESCRIPTION_QUERY = "INSERT INTO prescriptions (name, amount_per_day) \
                                 VALUES (:name, :amount_per_day)"

def get_all_not_signed_prescription(user_id):
    try:
        return db.session.execute(GET_ALL_NOT_SIGNED_PRESCRIPTIONS_QUERY,
                                 {"user_id": user_id}
                                 ).fetchall()
    except SQLAlchemyError:
        raise

def get_user_prescriptions(user_id):
    try:
        return db.session.execute(USER_PRESCRIPTIONS_QUERY,
                                 {"user_id": user_id}
                                 ).fetchall()
    except SQLAlchemyError:
        raise

def get_prescription_info_by_id(prescription_id):
    try:
        return db.session.execute(SINGLE_PRESCRIPTION_QUERY,
                                 {"prescription_id": prescription_id}
                                 ).fetchone()
    except SQLAlchemyError:
        raise

def update_prescription_from_user(user_id, prescription_id, bool_value):
    """Changing user_prescription table "visible" value to given parameter (bool_value)"""
    try:
        is_success = db.session.execute(UPDATE_USER_PRESCRIPTION_QUERY,
                                       {"user_id": user_id,
                                        "prescription_id": prescription_id,
                                        "visible": bool_value})
        # if nothing updated, there was not connection on user_prescriptions table earlier
        if not is_success.rowcount:
            add_new_prescription_to(user_id, prescription_id)

        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        raise

def add_new_prescription_to(user_id, prescription_id):
    try:
        db.session.execute(ADD_USER_PRESCRIPTION_QUERY,
                          {"user_id": user_id,
                           "prescription_id": prescription_id})
    except SQLAlchemyError:
        raise

def create_new_prescription(prescription_name, amount_per_day):
    try:
        db.session.execute(CREATE_NEW_PRESCRIPTION_QUERY,
                          {"name": prescription_name,
                           "amount_per_day": amount_per_day})
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        return False

def get_prescriptions_overview(doctor_id):
    try:
        return db.session.execute(GET_PRESCRIPTIONS_OVERVIEW_QUERY,
                                 {"doctor_id": doctor_id}
                                 ).fetchall()
    except SQLAlchemyError:
        raise