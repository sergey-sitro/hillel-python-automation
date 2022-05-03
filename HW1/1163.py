# У бурті було 600 кг кавунів. Першого дня продали 1/6 всіх кавунів,
# а другого - на 27 кг більше. Скільки кілограмів кавунів залишилося?

total_watermelons = 600
print("Всього кавунів:", total_watermelons)

sold_first_day = total_watermelons / 6
print(f"Першого дня продали {int(sold_first_day)} кавунів")

sold_second_day = sold_first_day + 27
print(f"Другого дня продали {int(sold_second_day)} кавунів")

remaining_watermelons = total_watermelons - sold_first_day - sold_second_day
print(f"Залишилося {int(remaining_watermelons)} кавунів")
