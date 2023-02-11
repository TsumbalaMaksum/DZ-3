import DZ3

BMW = DZ3.auto('BMW', 4)
Lamborghini = DZ3.auto('Lamborghini', 2)
Helicopter = DZ3.auto('Helicopter', 4)
Mersedes = DZ3.auto('Mersedes', 3)
Porshe = DZ3.auto('Porshe', 1)
Bus = DZ3.auto('Bus', 8)

max = DZ3.people('Max Tsumbala')
max2 = DZ3.people('Max Kaplun')
vitalik = DZ3.people('Vitalik')
kostya = DZ3.people('Kostya')
anetta = DZ3.people('Anetta')
arsen = DZ3.people('Arsen')
matviy = DZ3.people('Matviy')
vlad = DZ3.people('Vlad')


BMW.add_passengers(max)
BMW.add_passengers(max2)
BMW.add_passengers(vitalik)
BMW.add_passengers(vlad)
BMW.add_passengers(arsen)

Lamborghini.add_passengers(max)
Lamborghini.add_passengers(max2)
Lamborghini.add_passengers(vitalik)

Helicopter.add_passengers(anetta)
Helicopter.add_passengers(matviy)
Helicopter.add_passengers(max2)
Helicopter.add_passengers(vlad)
Helicopter.add_passengers(kostya)

Mersedes.add_passengers(max2)
Mersedes.add_passengers(max)
Mersedes.add_passengers(anetta)
Mersedes.add_passengers(vlad)

Porshe.add_passengers(max)
Porshe.add_passengers(max2)

Bus.add_passengers(kostya)
Bus.add_passengers(vitalik)
Bus.add_passengers(anetta)
Bus.add_passengers(arsen)
Bus.add_passengers(vlad)
Bus.add_passengers(matviy)



BMW.print_all_passengers()
Lamborghini.print_all_passengers()
Helicopter.print_all_passengers()
Mersedes.print_all_passengers()
Porshe.print_all_passengers()
Bus.print_all_passengers()





