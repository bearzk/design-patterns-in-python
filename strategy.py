class MovieTicket(object):
    def set_price(self, price):
        self.price = price

    def set_discount_strategy(self, strategy):
        self.strategy = strategy

    def get_discount_price(self):
        print round(self.price * self.strategy.get_discount(), 2)

    def get_price(self):
        print self.price

class DiscountStrategy(object):
    def get_discount(self):
        raise NotImplementedError('get_discount not implemented')


class StudentDiscountStrategy(DiscountStrategy):
    def get_discount(self):
        return 0.5


class SeniorDiscountStrategy(DiscountStrategy):
    def get_discount(self):
        return 0.7


class TuesdayDiscountStrategy(DiscountStrategy):
    def get_discount(self):
        return 1.0 / 3


ticket = MovieTicket()

student = StudentDiscountStrategy()
senior = SeniorDiscountStrategy()
tuesday = TuesdayDiscountStrategy()

ticket.set_price(17)
ticket.get_price()
ticket.set_discount_strategy(student)
ticket.get_discount_price()
ticket.set_discount_strategy(senior)
ticket.get_discount_price()
ticket.set_discount_strategy(tuesday)
ticket.get_discount_price()
