class OrderLog:
    def __init__(self, size):
        self.log = list()
        self.size = size

    def __repr__(self):
        return str(self.log)

    def record(self, order_id):
        self.log.append(order_id)
        if len(self.log) > self.size:
            self.log = self.log[1:]

    def get_last(self, i):
        return self.log[-i]


log = OrderLog(5)
log.record(1)
log.record(2)
print(log.log)
log.record(3)
log.record(4)
log.record(5)
print(log.log)
log.record(6)
log.record(7)
log.record(8)
print(log.log)
print(log.get_last(4))
print(log.get_last(1))