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

from utils.constant import NAME_DB_KEY, MESSAGE_LENGTH_MAX
from utils.validators.input_validator import is_valid_input
from repositories import message_repository
from services import users_service

def get_sent_messages(user_id):
    sent_messages = message_repository.get_sent_messages(user_id)
    return format_messages(sent_messages)

def get_received_messages(user_id):
    received_messages = message_repository.get_received_messages(user_id)
    return format_messages(received_messages)

def format_messages(messages_list):
    formatted_messages = []
    # message is a tuple value of (user_id, content, time)
    for message in messages_list:
        formatted_messages.append({
            "toOrfrom": users_service.get_user_info_by_key(message.user_id, NAME_DB_KEY),
            "content": message.content,
            "sent_at": message.time
        })
    return formatted_messages

def add_new_message(content, sender_user_id, receiver_user_id):
    if is_valid_input(content, MESSAGE_LENGTH_MAX):
        return message_repository.add_new_message(content, 
                                                  sender_user_id, 
                                                  receiver_user_id)
    return False