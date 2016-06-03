# !/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'xy'

from market import marketMonitor

marketMonitor('http://www.wooyun.org/market/', 'wooyun-market-log')
marketMonitor('http://www.wooyun.org/flea/', 'wooyun-flea-log')
