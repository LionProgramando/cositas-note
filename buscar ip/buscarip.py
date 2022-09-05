import socket   

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(f'El nombre de tu ordenador/computador es: {hostname}')
print(f'tu dirección ip es: {ip}')