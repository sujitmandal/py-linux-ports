#!/usr/bin/env python
# Author : Sujit Mandal
#Data : 10-01-202
#Github: https://github.com/sujitmandal
#This programe is create by Sujit Mandal
"""
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
"""

import sys
import json
import socket
import subprocess
from datetime import datetime

subprocess.call('clear', shell=True)

def portScan(ip, ports):
    start = datetime.now()
    scan_date = str(start).split()[0]
    start_time  = str(start).split()[1].split('.')[0]

    remoteServerIP = socket.gethostbyname(ip)
    print( "-" * 60)
    print( "    Please wait, scanning remote host", remoteServerIP)
    print( "-" * 60)

    try:
        open_port_list = []
        open_port_result = []
        close_port_list = []
        close_port_result = []

        for port in range(1, ports):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))

            if result == 0:
                print("...")
                open_port_list.append(port)
                open_port_result.append('Open')
            else:
                close_port_list.append(port)
                close_port_result.append('Close')

            sock.close()

    except KeyboardInterrupt:
        print( "You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print( 'Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print( "Couldn't connect to server")
        sys.exit()

    end = datetime.now()
    end_time  = str(end).split()[1].split('.')[0]
    total_time = str(end - start).split('.')[0]

    port_info = {}
    if len(open_port_list) != 0:
        port_info['Port Open'] = dict(zip(open_port_list, open_port_result))
    else:
        port_info['Port Open'] = 'No Port is Open'

    open_data = {}

    open_data['Time Info'] = {'Date' : scan_date,
                'Start Time' : start_time,
                'End Time' : end_time,
                'Total Time' : total_time}

    port_info.update(open_data)


    print('\n')
    print( 'Scanning Started in: ', start_time)
    print( 'Scanning Completed in: ', end_time)
    print('Total Time Take : ', total_time)

    return(port_info)

if __name__ == '__main__':
    IpAddress = ""
    #IpAddress = "192.168.122.195"
    PortNumber = 65000

    result = portScan(IpAddress, PortNumber)

    print(json.dumps(result, indent=4))

    with open('result.json', 'w') as i:
        json.dump(result, i)
