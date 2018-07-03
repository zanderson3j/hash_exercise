class Hashmap:

    def __init__(self):
        self.size = 10
        self.data = [None] * self.size
        self.loadFactor = 0.75
        self.elements = 0

    def put(self, key, value):
        element = self.hashFunction(key)
        while(self.data[element] != None and self.data[element][0] != key):
            element = (element + 1) % self.size
        if(self.data[element] == None):
            self.elements = self.elements + 1
        self.data[element] = (key, value)
        if((float(self.elements) / float(self.size)) > self.loadFactor):
            self.resize()

    def get(self, key):
        element = self.hashFunction(key)
        while(self.data[element] != None and self.data[element][0] != key):
            element = (element + 1) % self.size
        if(self.data[element] == None):
            return self.data[element]
        else:
            return self.data[element][1]

    def hashFunction(self, key):
        sum = 0
        for c in key:
            sum = sum + ord(c)
        return sum % self.size

    def resize(self):
        oldData = self.data[:]
        self.size = self.size * 2
        self.data = [None] * self.size
        self.elements = 0
        for i in oldData :
            if(i != None):
                self.put(i[0], i[1])
