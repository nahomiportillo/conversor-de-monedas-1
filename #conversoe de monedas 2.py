#conversor de monedas 
print("--------------------------")
print("---CONVERSOR DE MONEDAS---")
print("--------------------------")

while True:
    r = input('''
        Menu
        1.Dolares a Quetzales 
        2.Dolares a Euros
        3.Euros a Dolares
        4.Euros a Quetzales 
        5.Quetzales a Dolares
        6.Quetzales a Euros
        7.salir
        seleccione una opcion: ''')

    if r == '1':
       def dolque(dolar):
        dq = dolar * 7.74
        print ("el valor de la moneda es de: ",dq) 
        return 
    elif r == '2':
      def doleu(dolar):
       de = dolar * 0.91
       print ("el valor de la moneda es de: ",de)
       return  
    
    elif r == '3':
      def eudol(euro):
       ed = euro * 1.9
       print ("el valor de la moneda es de: ",ed)
       return  

    elif r == '4':
     def euque(euro):
      eq = euro * 8.47
      print ("el valor de la moneda es de: ",eq)
      return  

    elif r == '5':
     def quedol(quetzales):
      qd = quetzales * 0.13
      print ("el valor de la moneda es de: ",qd)
      return  
    
    elif r == '6':
     def queeu(quetzales):
      qe = quetzales * 0.12
      print ("el valor de la moneda es de: ",qe)
      return 

    elif r == '7':
       print("gracias por usar el conversor de monedas")
       break 

    if r == '1':
      dolque(10)
    elif r == '2':
      doleu (10)
    elif r == '3':
      eudol(10)
    elif r == '4':
      euque(10)
    elif r == '5':
      quedol(10)
    elif r == '6':
      queeu(10)
