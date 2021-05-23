#tabela de fahrenheit para celcius de 50 a 150

f = 49.0
celcius = 0

for i in range (50,151,1):
    celcius = 5/9 * (f - 32)
    f += 1
    print("fahrenheit =",f,"celcius = %.2f" %celcius)