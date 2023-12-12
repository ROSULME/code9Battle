
alfabet= "abcdefghijklmnopqrstuvwxyz"
antreUser = input("Antre yon direksyon ('<' oswa '>'),antite plas pou deplase, let pou komanse: ")


direksyon, dep, let_chwazi = antreUser[0], antreUser[1], antreUser[2:]


if direksyon not in ['<', '>']:
    print('Tanpri, antre yon direksyon ki korek: "<" pou agoch, ">" pou adwat.')
    exit()

if not dep.isdigit():
    print("Tanpri, antre yon  chif.")
    exit()

pozisyon = alfabet.find(let_chwazi)
if direksyon == '>':
    nouvo_pozisyon = (pozisyon + int(dep)) % 26
else:
    nouvo_pozisyon = (pozisyon - int(dep)) % 26


nouvo_let = alfabet[nouvo_pozisyon]
print(F"nouvo let lan se : {nouvo_let}" )
