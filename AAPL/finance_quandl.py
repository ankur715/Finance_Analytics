# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:07:59 2020

@author: ankur
"""

import pandas_datareader as pdr
import datetime 
aapl = pdr.get_data_yahoo('AAPL', 
                          start=datetime.datetime(2006, 10, 1), 
                          end=datetime.datetime(2012, 1, 1))

aapl.head()