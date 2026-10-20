price = float(input("price=").replace(",", "."))
discount = float(input("discount=").replace(",", "."))
vat = float(input("vat=").replace(",", "."))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"{'База после скидки:':<19}{base:.2f} ₽")
print(f"{'НДС:':<19}{vat_amount:.2f} ₽")
print(f"{'Итого к оплате:':<19}{total:.2f} ₽")
