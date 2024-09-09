# Solicitar ingreso al usuario
precio = int(input("ingrese el precio: "))
monto_pago = int(input("ingrese el pago: "))

# Realizar cálculos
vuelto = monto_pago - precio
print("su vuelto es de",vuelto)
# Calcular cuantos billetes de a $ 1.000 se requieren
billetes_20000 = int( vuelto / 20000)
vuelto = vuelto - (billetes_20000 * 20000) #vuelto % 20000
print(billetes_20000,"billetes de $20000")
# Calcular billetes de $20000
billetes_20000 = int( vuelto / 20000)
# Calcular billetes de $10000
billetes_10000 = int( vuelto / 10000)
vuelto = vuelto - (billetes_10000 * 10000) #vuelto % 10000
print(billetes_10000,"billetes de $10000")
# Calcular billetes de $5000
billetes_5000 = int( vuelto / 5000)
vuelto = vuelto - (billetes_5000 * 5000) #vuelto % 5000
print(billetes_5000,"billetes de $5000")
# Calcular billetes de $2000
billetes_2000 = int( vuelto / 2000)
vuelto = vuelto - (billetes_2000 * 2000) #vuelto % 2000
print(billetes_2000,"billetes de $2000")
# Calcular billetes de $1000
billetes_1000 = int( vuelto / 1000)
vuelto = vuelto - (billetes_1000 * 1000) #vuelto % 1000
print(billetes_1000,"billetes de $1000")
# Calcular monedas de $ 500 se requieren
monedas_500 = int( vuelto / 500)
vuelto = vuelto % 500
vuelto = vuelto - (monedas_500 * 500) #vuelto % 500
print(monedas_500,"monedas de $500")
# Calcular monedas de a $ 100 se requieren
monedas_100 = int( vuelto / 100)
vuelto = vuelto - (monedas_100 * 100) #vuelto % 100
print(monedas_100,"monedas de $100")
# Calcular monedas de a $ 50 se requieren
monedas_50 = int( vuelto / 50)
vuelto = vuelto - (monedas_50 * 50) #vuelto % 50
print(monedas_50,"monedas de $50")
# Calcular monedas de a $ 10 se requieren
monedas_10 = int ( vuelto / 10)
vuelto = vuelto - (monedas_10 * 10) #vuelto % 10
print(monedas_10,"monedas de $10")
# Mostrar el resultado
print(f"- {billetes_20000} billetes de $20.000")
print(f"- {billetes_10000} billetes de $10.000")
print(f"- {billetes_5000} billetes de $5.000")
print(f"- {billetes_2000} billetes de $2.000")
print(f"- {billetes_1000} billetes de $1.000")
print(f"- {monedas_500} monedas de $500")
print(f"- {monedas_100} monedas de $100")
print(f"- {monedas_50} monedas de $50")
print(f"- {monedas_10} monedas de $10")