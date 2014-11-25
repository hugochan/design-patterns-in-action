#!/usr/bin/env python
#encoding=utf-8

EUROToUSD = 1.2411
EUROToCAD = 1.3960
EUROToAUD = 1.4383
import pdb

class AbstractHandler(object):
    """docstring for AbstractHandler"""
    def __init__(self):
        self.successor = None
    def setSuccessor(self, successor):
        self.successor = successor
    def handleRequest(self, msg):
        pass


class USDHandler(AbstractHandler):
    """docstring for """
    def __init__(self):
        super(AbstractHandler, self).__init__()
    def handleRequest(self, msg):
        if msg[3] == "USD":
            amount = range(2)
            amount[0] = msg[0]*EUROToUSD
            amount[1] = "USD"
        else:
            if self.successor != None:
                amount = self.successor.handleRequest(msg)
            else:
                amount = None
        return amount

class CADHandler(AbstractHandler):
    """docstring for """
    def __init__(self):
        super(AbstractHandler, self).__init__()
    def handleRequest(self, msg):
        if msg[3] == "CAD":
            amount = range(2)
            amount[0] = msg[0]*EUROToCAD
            amount[1] = "CAD"
        else:
            if self.successor != None:
                amount = self.successor.handleRequest(msg)
            else:
                amount = None
        return amount

class AUDHandler(AbstractHandler):
    """docstring for """
    def __init__(self):
        super(AbstractHandler, self).__init__()
    def handleRequest(self, msg):
        if msg[3] == "AUD":
            amount = range(2)
            amount[0] = msg[0]*EUROToAUD
            amount[1] = "AUD"
        else:
            if self.successor != None:
                amount = self.successor.handleRequest(msg)
            else:
                amount = None
        return amount

class AbstractDecorator(AbstractHandler):
    """docstring for AbstractDecorator"""
    def __init__(self, pre_decorator):
        super(AbstractHandler, self).__init__()
        self.pre_decorator = None
        self.description = "AbstractDecorator"
    def getDescription(self):
        pass
    def convert(self, amount):
        pass

class ValutaDecorator(AbstractDecorator):
    """docstring for ValutaDecorator"""
    def __init__(self, pre_decorator):
        super(AbstractDecorator, self).__init__()
        self.description = "valuta"
        self.pre_decorator = pre_decorator
    def getDescription(self):
        return self.description
    def convert(self, amount):
        amount = self.pre_decorator.handleRequest(amount)
        amount_conversion = amount
        amount_conversion[0] = str(amount[0])
        return amount_conversion

class ExpDecorator(AbstractDecorator):
    """docstring for ExpDecorator"""
    def __init__(self, pre_decorator):
        super(AbstractDecorator, self).__init__()
        self.description = "exp"
        self.pre_decorator = pre_decorator
    def getDescription(self):
        return self.description
    def convert(self, amount):
        amount_conversion = ["%e"%float(self.pre_decorator.convert(amount)[0]), amount[3]]
        return amount_conversion

class RoundDecorator(AbstractDecorator):
    """docstring for ValutaDecorator"""
    def __init__(self, pre_decorator):
        super(AbstractDecorator, self).__init__()
        self.description = "round"
        self.pre_decorator = pre_decorator
    def getDescription(self):
        return self.description
    def convert(self, amount):
        amount_conversion = ["%.2e"%float(self.pre_decorator.convert(amount)[0]), amount[3]]
        return amount_conversion

class client(object):
    """docstring for client"""
    def __init__(self):
        pass
    def convert_CoR(self, msg):
        usd_handler = USDHandler()
        cad_handler = CADHandler()
        aud_handler = AUDHandler()
        
        usd_handler.setSuccessor(cad_handler)
        cad_handler.setSuccessor(aud_handler)
        aud_handler.setSuccessor(None)
        
        amount = usd_handler.handleRequest(msg)
        return amount
    def convert_CoR_Decorator(self, amount):
        usd_handler = USDHandler()
        cad_handler = CADHandler()
        aud_handler = AUDHandler()
        
        usd_handler.setSuccessor(cad_handler)
        cad_handler.setSuccessor(aud_handler)
        aud_handler.setSuccessor(None)
        
        v = ValutaDecorator(usd_handler)
        e = ExpDecorator(v)
        r = RoundDecorator(e)
        amount_conversion = r.convert(amount)
        return amount_conversion

if __name__ == '__main__':
    var = raw_input("Enter Amount in Euro: ")
    var = var.split(" ")
    var[0] = float(var[0])
    #var = [1, "Euro", "to", "USD"]
    c = client()
    #amount = c.convert_CoR(var)
    #print "converted amount: " + str(amount[0])
    amount_conversion = c.convert_CoR_Decorator(var)
    print "converted amount: " + amount_conversion[0] + " " + amount_conversion[1]
