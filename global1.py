"""l = 10  #l is gloabal
def function1(n):
    #l = 5
    m = 8
    print(l, m)
    print(n, "i have printed")
function1("This is me")
# print(m)"""
x = 89
def davide():
    x = 40
    def mezbah():
        global x
        x = 30
    print("befor calling mezbah()", x)
    mezbah()
    print("after calling mezbah()",x)

davide()
print(x)
