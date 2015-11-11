import Logger

Logger.configure('/var/log/app')
Logger.log('warning', 'you see a warning')
Logger.log('info', 'this is a info')
Logger.log('error', 'this is an error')
Logger.log('haha', 'this is an error')
