import funcionesMutante
"""
#Adn con 1 mutacion en linea  
adn=["aaaaaa",
     "gcagtg",
     "aaatga",
     "gcggac",
     "atcacc",
     "gttccc"
     ]
#adn con 1 mutacion en columna
adn=["agtacc",
     "actgtg",
     "acttga",
     "acggac",
     "atcacc",
     "gttccc"]
#adn con 1 mutacion en diagonal
adn=["aaaccc",
     "cacacc",
     "ccacgt",
     "gctact",
     "aaaccc",
     "cccaaa"
     ]
#adn con diagonal inversa
adn=["caaccc",
     "cacacc",
     "ccacgt",
     "gccact",
     "aaatca",
     "aaaccc"
     ]
#adn con mas de 1 mutacion
adn=["agtacc",
     "acagtg",
     "aaatga",
     "acggac",
     "atcacc",
     "gttccc"
     ]
     
#adn sin ninguna mutacion
adn=["aaaccc",
     "cccaaa",
     "aaaccc",
     "aaaccc",
     "cccaaa",
     "aaaccc"
     ]
"""

adn=funcionesMutante.AdnCreation()
print(adn)
Mutant=funcionesMutante.is_Mutant(adn)
if Mutant:
     print("El adn es de un mutante")
else:
     print("El adn no es de un mutante")


