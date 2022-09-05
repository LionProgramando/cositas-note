barra_de_pan = float(3.49)
descuento_x_barra_de_pan_que_no_son_del_dia = 60

cant_pan = int(input('Ingrese las barras de pan que no son del día\n'))

cant_x_precio = cant_pan * barra_de_pan
descuento = (barra_de_pan * descuento_x_barra_de_pan_que_no_son_del_dia) /100
descuento_aplicado = cant_x_precio - (cant_pan * descuento) 
print('Las barras de pan sin descuento sale:',round(cant_x_precio,2))
print('60% de descuento x pan',round(descuento,2))
print('Descuento aplicado',round(descuento_aplicado,2))
