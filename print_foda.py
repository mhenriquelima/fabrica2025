_frase = str(input("frase > ").strip().lower())
print("sua frase tem {} a's, o primeiro apareceu na posição {} e o ultimo {}".format(_frase.count("a"), _frase.find("a"), _frase.rfind("a")))
