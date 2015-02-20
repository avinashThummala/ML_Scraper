#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy

class MercadolibreItem(scrapy.Item):

	ML_Listing_URL = scrapy.Field()
	ML_Ad_Code = scrapy.Field()

	ML_Type_of_real_estate = scrapy.Field()
	ML_Type_of_transaction = scrapy.Field()

	ML_Photo_1 = scrapy.Field()
	ML_Photo_2 = scrapy.Field()
	ML_Photo_3 = scrapy.Field()
	ML_Photo_4 = scrapy.Field()
	ML_Photo_5 = scrapy.Field()
	ML_Photo_6 = scrapy.Field()
	ML_Photo_7 = scrapy.Field()
	ML_Photo_8 = scrapy.Field()
	ML_Photo_9 = scrapy.Field()
	ML_Photo_10 = scrapy.Field()
	ML_Video = scrapy.Field()

	ML_Provincia = scrapy.Field()
	ML_Barrio = scrapy.Field()
	ML_Calle = scrapy.Field()

	ML_Latitude = scrapy.Field()
	ML_Longitude = scrapy.Field()	
	ML_Telefono = scrapy.Field()

	ML_Recamaras = scrapy.Field()
	ML_Antiguedad = scrapy.Field()
	ML_Banos = scrapy.Field()

	ML_Superficie_construida_m2 = scrapy.Field()
	ML_Superficie_total_m2 = scrapy.Field()

	ML_Disposicion = scrapy.Field()
	ML_Horario_de_contacto = scrapy.Field()
	ML_Amueblado = scrapy.Field()
	ML_Apto_Profesional = scrapy.Field()
	ML_Balcon = scrapy.Field()
	ML_Cant_de_pisos_del_edificio = scrapy.Field()
	ML_Conservacion = scrapy.Field()
	ML_Cuota_de_mantenimiento = scrapy.Field()
	ML_Nro_de_departamentos_por_piso = scrapy.Field()
	ML_Elevador = scrapy.Field()
	ML_Estacionamiento = scrapy.Field()
	ML_Luminosidad = scrapy.Field()

	ML_Metros2_de_jardin_comun = scrapy.Field()
	ML_Metros2_de_jardin = scrapy.Field()

	ML_Titulo = scrapy.Field()
	ML_Descripcion = scrapy.Field()

	ML_Agua_Corriente = scrapy.Field()
	ML_Aire_acondicionado = scrapy.Field()
	ML_Alarma = scrapy.Field()
	ML_Area_de_juegos_infantiles = scrapy.Field()
	ML_Asador = scrapy.Field()
	ML_Calefaccion = scrapy.Field()
	ML_Cancha_de_squash = scrapy.Field()
	ML_Cancha_de_tenis = scrapy.Field()
	ML_Estacionamiento_para_visitantes = scrapy.Field()
	ML_Gas_Natural = scrapy.Field()
	ML_Conexion_a_internet = scrapy.Field()
	ML_Jacuzzi = scrapy.Field()
	ML_Jardin = scrapy.Field()
	ML_Luz_electrica = scrapy.Field()
	ML_Alberca = scrapy.Field()
	ML_Salon_de_fiesta = scrapy.Field()
	ML_Salon_de_usos_multiples_SOM = scrapy.Field()	
	ML_Telefone = scrapy.Field()
	ML_Seguridad = scrapy.Field()
	ML_Bodega = scrapy.Field()
	ML_Cisterna = scrapy.Field()
	ML_Cocina_integral = scrapy.Field()
	ML_Recepcion = scrapy.Field()
	ML_Comedor = scrapy.Field()
	ML_Cuarto_de_TV = scrapy.Field()
	ML_Cuarto_de_servicio = scrapy.Field()
	ML_Estudio = scrapy.Field()
	ML_Gimnasio = scrapy.Field()
	ML_Living_comedor = scrapy.Field()
	ML_Patio = scrapy.Field()
	ML_Playroom = scrapy.Field()
	ML_Terraza = scrapy.Field()
	ML_Vestidor = scrapy.Field()
	ML_Zotehuela = scrapy.Field()
	
	ML_Moneda = scrapy.Field()
	ML_Precio = scrapy.Field()