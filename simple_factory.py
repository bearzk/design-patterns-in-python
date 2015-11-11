class ChartFactory(object):
    @staticmethod
    def get_chart(name):
        if name == 'pie':
            return Pie()
        elif name == 'histo':
            return Histo()
        elif name == 'wave':
            return Wave()
        elif name == 'random':
            return Random()
        else:
            raise Exception('Not a valid chart name')


class Chart(object):
    def draw(self):
        raise NotImplementedError('draw should be implemented.')
    def erase(self):
        raise NotImplementedError('erase should be implemented.')


class Pie(Chart):
    def draw(self):
        print 'draw a pie'
    def erase(self):
        print 'wipe it out'


class Histo(Chart):
    def draw(self):
        print 'draw a histogram'
    def erase(self):
        print 'wipe it out'


class Wave(Chart):
    def draw(self):
        print 'draw a wave'
    def erase(self):
        print 'wipe it out'

class Random(Chart):
    pass

pie = ChartFactory.get_chart('pie')
pie.draw()
pie.erase()
histo = ChartFactory.get_chart('histo')
histo.draw()
histo.erase()
wave = ChartFactory.get_chart('wave')
wave.draw()
wave.erase()
nothing = ChartFactory.get_chart('nothing')
random = ChartFactory.get_chart('random')
random.draw()
random.erase()
