#!/usr/bin/env python
import random
import httplib, urllib
import time

class DigitalFoosballSimulator(object):
    def __init__ (self, ip="127.0.0.1", port="80"):
        self.table = "main"
        self.ip = ip
        self.port = port
        self.token = random.randint(1,65535)
        self.context = ""

    def _sendRequest(self, team, tag=None):
        params = {'@token': self.token, '@table': self.table}
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "User-Agenet": "Arduino/DigitalKicker"
                  }
        conn = httplib.HTTPConnection(self.ip, self.port)
        conn.set_debuglevel(1)
        if tag:
            params['@tag'] = tag
            context = self.context + "/events/rfid/%s" % team
        else:
            context = self.context + "/events/goals/%s" % team
        params = urllib.urlencode(params)

        conn.request("POST", context, params, headers)
        return conn.getresponse()       

    def sendVisitorGoal(self):
        response = self._sendRequest("visitors")
        print response.status, response.reason

    def sendHomeGoal(self):
        response = self._sendRequest("home")
        print response.status, response.reason

    def addRFIDVistor(self, id):
        response = self._sendRequest("visitors", id)
        print response.status, response.reason

    def addRFIDHome(self, id):
        response = self._sendRequest("home", id)
        print response.status, response.reason

if __name__ == "__main__":

    sim = DigitalFoosballSimulator()

    sim.sendVisitorGoal()

    for x in range(0):
        time.sleep(2)
        sim.sendHomeGoal()
        time.sleep(2)
        sim.sendVisitorGoal()
    
