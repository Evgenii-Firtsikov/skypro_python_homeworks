def bank(X, Y):
  for _ in range(Y):
      X += X * 0.1
  return X
initial_deposit = 1000  
years = 5  
final_amount = bank(initial_deposit, years)
print(f"Сумма на счету спустя {years} лет: {final_amount:.2f} рублей")
