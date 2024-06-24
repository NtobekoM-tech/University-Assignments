#Test program for the validate function in the numberutil module
#Ntobeko Mhlongo
#08 April 2024

"""
>>> import timeutil
>>> timeutil.validate('3446 p.m.')
False
>>> timeutil.validate('100:30 a.m.')
False
>>> timeutil.validate('01:27 a.m.')
False
>>> timeutil.validate('12:59 am')
False
>>> timeutil.validate('5:3 a.m.')
False
>>> timeutil.validate('7:25 p.m.')
True






"""
import doctest
doctest.testmod(verbose=True)