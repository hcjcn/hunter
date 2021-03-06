#!/ usr/bin/env
# coding=utf-8
#
# Copyright 2019 ztosec & https://www.zto.com/
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""
author: b5mali4
"""
from exception.hunter_web_exception import BaseHunterException

__all__ = ["TasksDataNotExistException", "UserTasksDataNotExistException", "UsersDataNotExistException"]


class TasksDataNotExistException(BaseHunterException):
    def __init__(self):
        BaseHunterException.__init__(self, "没有从task表中找到符合条件的记录")


class UserTasksDataNotExistException(BaseHunterException):
    def __init__(self):
        BaseHunterException.__init__(self, "没有从user_task表中找到符合条件的记录")


class UsersDataNotExistException(BaseHunterException):
    def __init__(self):
        BaseHunterException.__init__(self, "没有从user表中找到符合条件的记录")
