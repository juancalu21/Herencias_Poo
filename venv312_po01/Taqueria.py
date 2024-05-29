
def main():

    menu={
        "TACO": 4.00,
        "PERRO": 6.00,
        "QUESADILLA": 3.00,
        "PAPAS": 2.00,
        "NUGUETS": 8.00
    }
    order_total=0.0
    while True:
        try:
            item=input("Ingrese su articulo de su pedido: ")
        except EOFError:
            break
            
        item=item.upper()
        if item in menu:
            order_total += menu[item]
            print("$",order_total)
        elif item =="COD":
            print(f"el total de su pedido es ${order_total: .2f} ")
            break
        else:
            print("Articulo invalido")

if __name__=="__main__":
    main()
    