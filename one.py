points = 0
good_answ = 0
print()
print("Привіь, давай грати !")



vidpovidy = input("Мяч круглий (так - ні)")

if vidpovidy == "так":
  points = points + 1
  good_answ = good_answ + 1
  print("Вірно, в тебе ", points, "балів")
else:
  print("Не вірно, в тебе ", points, "балів")
  good_answ = 0



vidpovidy = input("Земля кругла (так - ні)")
if vidpovidy == "так":
  points = points + 1
  good_answ = good_answ + 1
  print("Вірно, в тебе ", points, "балів")
  print("відповіді підряд: ", good_answ)
else:
  print("Не вірно, в тебе ", points, "балів")
  good_answ = 0