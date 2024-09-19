from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)

print("Les valeurs d'IMC calculées :")
print(bmi, type(bmi))

print("\nRésultats de apply_limit (limite = 26) :")
print(apply_limit(bmi, 26))