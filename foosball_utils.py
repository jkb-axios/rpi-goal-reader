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
        context = ""
        try:
            conn = httplib.HTTPConnection(self.ip, self.port)
            conn.set_debuglevel(1)
            if tag:
                params['@tag'] = tag
                context = self.context + "/events/rfid/%s" % team
            else:
                context = self.context + "/events/goals/%s" % team
            params = urllib.urlencode(params)

            conn.request("POST", context, params, headers)
            response = conn.getresponse()
            print response.status, response.reason
            return response.status, response.reason
        except Exception, e:
            txt = 'exception when sending request\n  params:%s\n  headers:%s\n  context:%s\n'%(params,headers,context)
            print 'ERROR:',txt
            return 'ERROR', txt

    def sendVisitorGoal(self):
        return self._sendRequest("visitors")

    def sendHomeGoal(self):
        return self._sendRequest("home")

    def addRFIDVistor(self, id):
        return self._sendRequest("visitors", id)

    def addRFIDHome(self, id):
        return self._sendRequest("home", id)

if __name__ == "__main__":

    sim = DigitalFoosballSimulator()

    sim.sendVisitorGoal()

    for x in range(0):
        time.sleep(2)
        sim.sendHomeGoal()
        time.sleep(2)
        sim.sendVisitorGoal()
    
