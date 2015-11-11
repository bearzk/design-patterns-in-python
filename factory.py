class AbstractFactory(object):
    def get_product(self, name):
        raise NotImplementedError('get_product not implemented.')

class AbstractProduct(object):
    def shine(self):
        raise NotImplementedError('get_product not implemented.')

class BoxFactory(AbstractFactory):
    def get_product(self, name):
        if 'square' == name:
            return SquareBox()
        elif 'round' == name:
            return RoundBox()
        else:
            raise NotImplementedError('The box you asked not exists.')

class BedFactory(AbstractFactory):
    def get_product(self, name):
        if '2' == str(name):
            return QueenBed()
        elif '1.5' == str(name):
            return DoubleBed()
        else:
            raise NotImplementedError('The bed is not there.')

class SquareBox(AbstractProduct):
    def shine(self):
        print "Oh I'm shining!"

class RoundBox(AbstractProduct):
    def shine(self):
        print "wow I'm shining!"

class QueenBed(AbstractProduct):
    def shine(self):
        print 'Oh no, why am I shining?'

class DoubleBed(AbstractProduct):
    def shine(self):
        print "OK, I'll shine anyway."



factory = BoxFactory()
box = factory.get_product('square')
box.shine()
box = factory.get_product('round')
box.shine()
# box = factory.get_product('triangle')
# box.shine()

factory = BedFactory()
bed = factory.get_product(2)
bed.shine()
bed = factory.get_product(1.5)
bed.shine()
