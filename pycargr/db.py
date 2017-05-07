#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

__author__ = 'Florents Tselai'

from .config import REDIS_CAR_KEYSPACE, CACHE_EXPIRE_IN


class RedisCache:
    def __init__(self, redis_con):
        self.redis_con = redis_con

    def car_is_cached(self, car_id):
        return self.redis_con.exists(REDIS_CAR_KEYSPACE.format(car_id))

    def get_cached_car(self, car_id):
        return self.redis_con.hgetall(REDIS_CAR_KEYSPACE.format(car_id))

    def cache_car(self, car_id, car_data, expire_in=CACHE_EXPIRE_IN):
        key = REDIS_CAR_KEYSPACE.format(car_id)
        self.redis_con.hmset(key, car_data)
        self.redis_con.expire(key, expire_in)