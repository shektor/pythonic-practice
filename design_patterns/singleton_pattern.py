
class Singleton():
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class Logger(Singleton):
    
    def __init__(self):
        self._log = []
    
    def write(self, record):
        self._log.append(record)
        print('Record written to log')
    
    def records(self):
        for record in self._log:
            print(record)


class Blogger(Singleton):
    
    def __init__(self):
        self._log = []
    
    def write(self, record):
        self._log.append(record)
        print('Record written to log')
    
    def records(self):
        for record in self._log:
            print(record)


if __name__ == '__main__':
    log = Logger()
    log2 = Logger()
    blog = Blogger()

    log.write('log log')
    log2.write('log2 log2')
    blog.write('blog blog')

    print('RECORDS log')
    log.records()
    print('RECORDS log2')
    log2.records()
    print('RECORDS blog')
    blog.records()
