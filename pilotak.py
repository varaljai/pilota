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
stats = dict()
for sor in l:
    rajtszam = sor[-1]
    stats[rajtszam] = stats.get(rajtszam, 0) + 1
    
szamok = [sor for sor in stats.items() if sor[1] > 1 ]
szamok.remove(szamok[0])
rajtszamok = [sor[0] for sor in szamok]

print(f"7. feladat: {rajtszamok[0]},{rajtszamok[1]},{rajtszamok[2]},{rajtszamok[3]}")
    
    
    
    


