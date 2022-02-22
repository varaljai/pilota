f = open(f"pilotak.txt","r",encoding="UTF-8")
l = [sor.strip().split(";") for sor in f ]
f.close()
l.remove(l[0])

#3. feladat:
print(f"3.feladat : {len(l)}")

#4. feladat:
ember = l[-1][0]
for sor in l:
    print(f"4. feladat: {ember} ")
    break

#5. feladat
pilotak = "1901"
print("5. feladat:")
for sor in l:
    if sor[1] <= pilotak:
        print(f"      {sor[0]}  ({sor[1]})")
#6. feladat
rajtszam = [int(sor[-1]) for sor in l if sor[-1] != ""]
a = min(rajtszam)
nemzet = ""
for sor in l:
    if str(a) == sor[3]:
        nemzet = sor[2]
print(f"6. feladat: {nemzet}")

#7. feladat
stat = dict()
for sor in rajtszam:
    rajtszam = (sor[-1])
    stat[rajtszam] = stat.get(rajtszam, 0) + 1
    
szamok = []
for sor in stat.items():
        if sor[1] > 1:
            szamok.append(sor)
    
    
    
    


