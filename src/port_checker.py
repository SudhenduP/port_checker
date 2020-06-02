#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
#import re
import sys
import pandas as pd
import os


def get_checklist(severportfile):
    #port_checklist = pd.read_csv(r'C:\Users\Sudhendu-BCT\Python_Practice\PortChecker\check_port_list.csv')
    
    port_checklist = pd.read_csv(input_file)
    port_checklist.insert(loc=2,column="Status",value = '')
    return port_checklist

def check_server(address, port):
    
    # Create a TCP socket
    timeout = 40 #timeout in seconds
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.settimeout(timeout)
    print ("Attempting to connect to %s on port %s" % (address, port))
    try:
        s.connect((address, port))
        #print ("Connected to %s on port %s" % (address, port))
        return "Connected to %s on port %s" % (address, port)
    except socket.error as error:
        #print ("Connection to %s on port %s failed: %s")
        return "Connection to %s on port %s failed: %s" % (address, port, error)
    finally:
        s.close()

def check_create_status(severportfile):
    print ('Reading from files: ' +severportfile)

    get_file= get_checklist(severportfile)
    
    for i in range(len(get_file)) : 
        print("Started Processing") 
        address = get_file.loc[i, "IP"]
        port = get_file.loc[i, "Port"]
        check = check_server(address, port)
        #get_file = get_file.append({'Status':check},ignore_index=True)
        get_file.loc[i, 'Status'] = check
        print (check)
        #print(get_file)
        print("Finished Processing") 
    result_dirname = os.getcwd()+ '\\result'
    result_filename ='out_server_port.csv'
    if not os.path.exists(result_dirname):
        os.mkdir(result_dirname)
    fullname = os.path.join(result_dirname, result_filename)    
    get_file.to_csv(index=False, path_or_buf=fullname)
    print('Result written to file. Please check the file:  ' +fullname)
    sys.exit(not check)


if __name__ == '__main__':
    #from optparse import OptionParser
    #parser = OptionParser()
    #parser.add_option("-f", "--severportfile", dest="severportfile", default='NA', help="ADDRESS for server", metavar="SERVERPORTFILE")

    try:
        input_file =os.getcwd()+ '\input\in_server_port.csv'
        path.exists(input_file)

    except:
        print("Please check if you have /input/in_server_port.csv file present")
    print("Started reading the csv file in input directory: " +input_file)
    check_create_status(input_file) 