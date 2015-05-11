#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: windpro
CreateDate: 14-9-2
"""
#测试在相同元素个数集合中查找元素的效率
import random
import timeit

class TestData(object):

    # ---- 描述符: 延迟实例化。------------------------ #

    class InstanceDescriptor(object):

        def __get__(self, instance, owner):
            v = getattr(owner, "__instance__", None)
            if not v:
                v = owner()  # 构造参数!
                owner.__instance__ = v

            return v

    # ----------------------------------------------- #

    def __init__(self):
        self.test_count = 10

        self.dict_list = self.build_dict_list()
        self.set_list = self.build_set_list()
        self.list_list = self.build_list_list()

    instance = InstanceDescriptor()

    def build_dict_list(self):
        result = dict()
        for i in xrange(self.test_count):
            item = random.randint(1, 999999)
            result[item] = item
        return result

    def build_set_list(self):
        result = set()
        for i in xrange(self.test_count):
            item = random.randint(1, 999999)
            result.add(item)
        return result

    def build_list_list(self):
        result = list()
        for i in xrange(self.test_count):
            item = random.randint(1, 999999)
            result.append(item)
        return result

#start testing
def test_dict_find_item():
    item = TestData.instance.dict_list
    match_count = 0
    for i in xrange(10000):
        if i in item:
            match_count += 1
    return match_count

def test_set_find_item():
    item = build_set_list()
    match_count = 0
    for i in xrange(10000):
        if i in item:
            match_count += 1
    return match_count

def test_list_find_item():
    item = build_list_list()
    match_count = 0
    for i in xrange(10000):
        if i in item:
            match_count += 1
    return match_count

timeit
# test
