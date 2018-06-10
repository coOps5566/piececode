#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

def time_func():
    print 'run main()'
    a= '2018-06-10T02:53:39'
    b= time.mktime(time.strptime(a,'%Y-%m-%dT%H:%M:%S'))
    print 'str to seconds: ',b
    c= b+ 8*3600
    print '---',c

def main():
    time_func()


main()
