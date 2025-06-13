
def modificar_imutavel(numero):
    print(f"  -> Dentro da função (antes): {numero}")
    numero = 100  
    print(f"  -> Dentro da função (depois): {numero}")

def modificar_mutavel(lista):
    print(f"  -> Dentro da função (antes): {lista}")
    lista.append(30) 
    print(f"  -> Dentro da função (depois): {lista}")

valor_int = 10
print(f"Valor int (antes): {valor_int}")
modificar_imutavel(valor_int)
print(f"Valor int (depois): {valor_int}")

print("-" * 20)

valor_list = [10, 20]
print(f"Valor list (antes): {valor_list}")
modificar_mutavel(valor_list)
print(f"Valor list (depois): {valor_list}")