temperatura=float(input("Digite a temperatura (°C): "))
umidade= float(input("Digite a umidade (%): "))
if temperatura >25 and umidade >60:
    print ("Ar quente e umido")
elif temperatura >25 and umidade <60:
    print ("Ar quente e seco")
elif temperatura <=25 and umidade >60:
     print ("Ar frio e umido")
elif temperatura <=25 and umidade <60:
    print ("Ar frio e seco")        
