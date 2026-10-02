#Sort a dictionary by values.
d={"A":90,"B":60,"C":50,"D":10}
s=dict(sorted(d.items(), key=lambda item: item[1]))
print(s)
