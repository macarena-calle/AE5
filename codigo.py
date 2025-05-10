def primos(a):
    nuevo= int(a)
    for i in range (2,nuevo):
        if nuevo%i==0:
            return False
    return True