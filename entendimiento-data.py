
"""      
Objetivos del taller:,
Mejorar estrategía de ocupación y se basa en 3 frentes:,
Una vez que un cliente realiza una reserva, entender los factores que determinan la duración de la,
estadía, la probabilidad de cancelación y la influencia de características como el tipo de,
hotel, la composición del grupo de huéspedes o el canal de reservación es vital para el,
éxito del negocio
  
El dataset suministrado contiene alrededor de 32 columnas y 58895 filas.,
Contiene información relacionada al servicio de hospedaje ofrecido por un hotel o un resort. Asimismo, contiene informacion del estado y fecha de la reserva, el pais, las personas que se alojaron, el tipo de plan escogido por el usuario, la compañia encargada del pago o la reserva,entre otras.,
Los tipos de datos encontrados en el dataset son: text, boolean, integer, numeric y date.,
Top 5 atributos:,
* reservation_status      (Cualitativa nominal):,
* hotel                   (Cualitativa nominal),
* stays_in_weekend_nights (cuantitativa discreta),
* stays_in_week_nights    (cuantitativa discreta),
* lead_time               (cuantitativa discreta)

"""
print("Hola")
print("Hola")


df = pd.read_csv("data/hotel_bookings_modified.csv")
print(df.head())


