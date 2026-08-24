# Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:

#   -kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#   -nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random

yksyks = random.randint(0, 9)
ykskaks = random.randint(0, 9)
ykskolme = random.randint(0, 9)

kaksyks = random.randint(1, 6)
kakskaks = random.randint(1, 6)
kakskolme = random.randint(1, 6)
kaksnelj = random.randint(1, 6)

print(f"koodi 1: {yksyks}{ykskaks}{ykskolme}, koodi 2: {kaksyks}{kakskaks}{kakskolme}{kaksnelj}")