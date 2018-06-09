d=dict(A=20,D=45,C=32);
print(d);
for k in d:
    print(k,d[k]);
print("\n");
for k in sorted(d.keys()):
    print(k,d[k])
print("\n");
for k,v in sorted(d.items()):
    print(k,v);
print("\n");
for v in sorted(d.values()):
    print(v)
print("\n",d['A']);
