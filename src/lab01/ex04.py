m = int(input("Минуты: "))
hours, minutes = divmod(m, 60)
print(f"{hours}:{minutes:02d}")
