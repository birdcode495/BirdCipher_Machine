import hashlib

class HASH:

	def generaHash(h):

		digest = h.hexdigest()
		return digest


# x = 0

# while x < 1:

# 	print("Elige el algoritmo a usar: ")
# 	print("1: - SHA 256")
# 	print("2: - SHA 512")
# 	print("3: - Finalizar programa")


# 	nAlgoritmo = int(input())

# 	print("Introduce datos a hashear: ")

# 	datos = input()

# 	algoritmo = ""

# 	if nAlgoritmo != 3:

# 		if nAlgoritmo == 1:

# 			algoritmo = 'sha256'

# 		elif nAlgoritmo == 2:

# 			algoritmo = "sha512"


# 		bdatos = bytes(datos, 'utf-8')
# 		h = hashlib.new(algoritmo, bdatos)
# 		hash1 = HASH.generaHash(h)

# 		print()
# 		print(hash1)
# 		print()
# 		x = 0

# 	else:

# 		x = 1

# print("The end")

algoritmo = 'sha256'









