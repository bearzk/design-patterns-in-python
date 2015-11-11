from time import strftime

LOG_PATH = ''
LOG_LEVELS = ['info', 'warning', 'error']

def logtime():
    return strftime('%Y-%m-%d %H:%M:%S')

def configure(path):
    global LOG_PATH
    LOG_PATH = path

def log(level, msg):
    if level in LOG_LEVELS:
        print "logged to %s" % LOG_PATH
        print "[%s] %s %s" % (level, logtime(), msg)
    else:
        print "log level not allowed"
