def gcd(a,b):
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)
def simplify_fraction(fraction):
    gcdd = gcd(fraction[0],fraction[1])
    return (fraction[0] // gcdd, fraction[1] // gcdd)

print (simplify_fraction((63,462)))
