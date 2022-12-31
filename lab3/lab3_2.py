import random

vlan_mos = [random.randint(1, 10) for i in range(8)]
vlan_kursk = [random.randint(1, 15) for i in range(10)]
vlan_novosib = [random.randint(1, 20) for i in range(15)]
print(vlan_mos, vlan_kursk, vlan_novosib)

vlan_mos = list(set(vlan_mos))
print(len(vlan_mos))

vlan_mos = set(vlan_mos)
vlan_kursk = set(vlan_kursk)
vlan_novosib = set(vlan_novosib)
print(vlan_mos, vlan_kursk, vlan_novosib)

print(vlan_mos & vlan_kursk)

print(vlan_mos & vlan_kursk & vlan_novosib)

print(vlan_novosib - (vlan_mos | vlan_kursk))