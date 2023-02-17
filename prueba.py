from main import Motor,Asiento,Auto

motor=Motor(4, "electrico", 142)
silla=Asiento("blanco", 5000, 435)
carro=Auto("model 3", 33000, list(),"tesla", Motor(4, "electrico", 142), 341)

print(motor.tipo)
print(silla.color)
print(Auto.cantidadCreados)

