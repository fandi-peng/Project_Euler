
def self_powers():
    return str(sum([i ** i for i in range(1, 1001)]))[-10:]

print self_powers()
