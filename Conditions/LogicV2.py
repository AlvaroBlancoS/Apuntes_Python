edad = 23
es_vip = True
tiene_entrada = False

if edad < 18:
    print("No puedes entrar: eres menor de edad")
elif edad < 25 and es_vip:
    print("Puedes entrar: menor de 25 y eres VIP")
elif edad >= 25 and tiene_entrada:
    print("Puedes entrar: mayor de 25 y tienes entrada")
else:
    print("No puedes entrar: no cumples los requisitos")
