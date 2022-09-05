contraseña_valida='IntroProgra'
contraseña_usuario=input('Ingrese contraseña')

cont= 0

while contraseña_usuario!=contraseña_valida and cont<=3:
    print('contraseña Erronea, intentelo nuevamente.')
    contraseña_usuario=input('Ingrese Contraseña')
    cont+=1

if contraseña_valida == contraseña_usuario:
    print('Contraseña correcta')
    print('Lo lograste en',cont,'intentos')

if cont==3:
    print('sistema bloqueado, has puesto muchas veces la contraseña erronea')
    