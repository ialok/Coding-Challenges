#! /usr/bin/env python

import socket
import httplib
import time
from collections import defaultdict


"""
    Example: python >/dev/null 2>&1 < /dev/null &

class MonitorService(object):
    def __init__(self, log_file=None):
        """
            
        """
        self.log_file = log_file

    def _check_http_response(self, service):
        """

        """
        try:
            connection  = httplib.HTTPConnection(service['HOST'], service['PORT'],
                                                service['Timeout'])
            connection.request('HEAD', '/')
            response = connection.getresponse()

            if response.status == 200:
                return ('SUCCESS', response.status, time.time())
            else:
                return ('FAIL', response.status, time.time())
        except socket.error as error_message:
            return ('DEAD', error_message, time.time())


    def _write(self, service, status, state_count):
        """

        """
        
        with open(self.log_file, 'a') as fw:
            total_responses = sum(state_count.values())
            if state_count['DEAD'] == total_responses:
                string = "Service: " + service['NAME'] + " STATUS: DOWN from "
                string += str(status[0][-1]) + " - " + str(status[-1][-1])
                fw.write(string + "\n")
            else:
                string = "Service: " + service['NAME'] + " ValidResponse: "
                string += str(state_count['SUCCESS'])
                string += " InvalidResponse: "
                string += str(state_count['FAIL'])
                string += " ServerDown: " + str(int(state_count['DEAD']*100.0/total_responses))
                string += "% from "  + str(status[0][-1]) + " - " 
                string += str(status[-1][-1])

                fw.write(str(string)+"\n")
               
    def monitor(self, service, polling_interval=10, flush_timeout=30):
        """Sets up monitoring for a given service

        Args:
            service: dictionary containing the service parameters
            polling_interval: time to sleep before starting the next run
            flush_timeout: time to wait before flushing stats to disk

        Returns:
            Nothing
        """

        if flush_timeout<polling_interval:
            flush_timeout = polling_interval
        
        max_status_in_memory = flush_timeout/polling_interval
        status = []
        state_count = defaultdict(int)

        while True:
            state = self._check_http_response(service)
            state_count[state[0]] += 1
            status.append(state)

            if len(status) >= max_status_in_memory:
                self._write(service, status, state_count)
                status = []
                state_count = defaultdict(int)
            print "sleeping"
            time.sleep(polling_interval/100.0)

monitor_service = MonitorService("monitor.log")
service = {'NAME': 'Magnificent', 'HOST': 'localhost', 'PORT': 12345, 'Timeout': 1}

if __name__ == "__main__":
    monitor_service.monitor(service, polling_interval=20, flush_timeout=40)
