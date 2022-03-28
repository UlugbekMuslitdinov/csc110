def polarity(x):
    x = str(x)
    if x == "0":
        return "Zero"
    elif x[0] == "-":
        return "Negative"
    else:
        return "Positive"

# <==========================================TESTS=====================================================>

print(polarity(1))
print(polarity(-1))
print(polarity(0))
