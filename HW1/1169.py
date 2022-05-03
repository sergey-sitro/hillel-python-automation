# Маса 300 жолудів 1 кг. У лісорозсаднику посадили 2 кг жолудів. Не зійшла
# десята частина жолудів. Скільки зійшло саджанців дуба?

acorns_count = 300
acorns_weight = 1

planted_acorns = acorns_count * (acorns_weight * 2)

print(f"Всього посадили {planted_acorns} жолудів")
print(f"Не зійшло {planted_acorns // 10} жолудів :(")
