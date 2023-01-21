from threading import Thread


class AppRunner:


    def __init__(self, function, args):
        self.function = function
        self.args = args
        self.text = True
        self.capture_output = True
        threads = []
        self.stdout = None
        self.stderr = None
    
    def run_one(self, function, args):
        t = Thread(target=function, args=args)
        t.start()
        t.join()
        return t
    
    def run_various(self, function=None, args=None):
        t = Thread(target=self.run_function, args=(function, args))
        self.threads.append(t)

        for x in self.threads:
            x.start()

        for x in self.threads:
            x.join()

        return self.threads
    