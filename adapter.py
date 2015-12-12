class PowerSocketInterface(object):
    def active(self):
        raise NotImplementedError("PowerSocket should active")

class EUSocket(PowerSocketInterface):
    def __init__(self, eu_plug):
        self.plug = eu_plug

    def active(self):
        self.plug.eu_connect()


class EUPlug(object):
    def __init__(self):
        self.message = "EU plug connected\n"

    def eu_connect(self):
        print self.message


class CNPlug(object):
    def __init__(self):
        self.message = 'CN plug connected\n'

    def cn_connect(self):
        print self.message

class CNEUAdapter(EUPlug):
    def __init__(self, cn_plug):
        self.message = "CNEU adapter in use"

    def eu_connect(self):
        print self.message
        return cn_plug.cn_connect()

print "plug a eu_plug direct to eu socket"
eu_plug = EUPlug()
socket = EUSocket(eu_plug)
socket.active()

print "plug a cn_plug through a cn_eu_adapter to eu socket"
cn_plug = CNPlug()
adapter = CNEUAdapter(cn_plug)
socket = EUSocket(adapter)
socket.active()
