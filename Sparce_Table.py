class IdempotentSparseTable:
    ''' Answer range queries for an idempotent function
    '''
 
    def __init__(self, data, f):
        '''
        :param data: The data, a list
        :param f: An idempotent function. MUST BE IDEMPOTENT
        '''
        self.f = f
        self.n = len(data)
        self.st = [[d] for d in data]
        k = self.n.bit_length()
        for j in range(1, k):
            for i in range(self.n - (1 << j) + 1):
                self.st[i].append(self.f(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1]))
        self.logs = [0, 0]
        for i in range(2, self.n + 1):
            self.logs.append(self.logs[i // 2] + 1)
 
    def rmq(self, l, r):
        j = self.logs[r - l]
        return self.f(self.st[l][j], self.st[r - (1 << j)][j])
 
