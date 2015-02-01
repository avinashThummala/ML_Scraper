# -*- coding: utf-8 -*-

import sys, MySQLdb, hashlib, re
from scrapy.exceptions import DropItem
from scrapy.http import Request

class MercadolibrePipeline(object):

	def __init__(self):

		self.conn = MySQLdb.connect(user='root', passwd='baggio', db='pyScraper', host='localhost', charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()

	def getCoordinate(self, floatStr):

		floatStr = re.sub("[^0123456789\.-]", '', floatStr)

		if floatStr:
			return float(floatStr)		
		else:
			return None							

	def getFloat(self, floatStr):

		floatStr = re.sub("[^0123456789\.]", '', floatStr)

		if floatStr:
			return float(floatStr)		
		else:
			return None			

	def process_item(self, item, spider): 

	    try:

	        self.cursor.execute("""INSERT INTO mercadoLibre VALUES (

				%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
				%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
				%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
				%s, %s
				        	
	        	)""", (

	        	item['ML_Listing_URL'].encode('utf-8'),

				item['ML_Type_of_real_estate'].encode('utf-8'),
				item['ML_Type_of_transaction'].encode('utf-8'), 

				item['ML_Photo_1'].encode('utf-8'),
				item['ML_Photo_2'].encode('utf-8'),
				item['ML_Photo_3'].encode('utf-8'),
				item['ML_Photo_4'].encode('utf-8'),
				item['ML_Photo_5'].encode('utf-8'),
				item['ML_Photo_6'].encode('utf-8'),
				item['ML_Photo_7'].encode('utf-8'),
				item['ML_Photo_8'].encode('utf-8'),
				item['ML_Photo_9'].encode('utf-8'),
				item['ML_Photo_10'].encode('utf-8'),
				item['ML_Video'].encode('utf-8'),

				item['ML_Provincia'].encode('utf-8'),
				item['ML_Barrio'].encode('utf-8'),
				item['ML_Calle'].encode('utf-8'),

				self.getCoordinate(item['ML_Latitude']),
				self.getCoordinate(item['ML_Longitude']),				
				item['ML_Telefone'].encode('utf-8'),

				item['ML_Recamaras'].encode('utf-8'),
				item['ML_Antiguedad'].encode('utf-8'),
				item['ML_Banos'].encode('utf-8'),

				self.getFloat(item['ML_Superficie_construida_m2']),
				item['ML_Superficie_total_m2'].encode('utf-8'),

				item['ML_Disposicion'].encode('utf-8'),
				item['ML_Horario_de_contacto'].encode('utf-8'),
				item['ML_Amueblado'].encode('utf-8'),
				item['ML_Apto_Profesional'].encode('utf-8'),
				item['ML_Balcon'].encode('utf-8'),
				item['ML_Cant_de_pisos_del_edificio'].encode('utf-8'),
				item['ML_Conservacion'].encode('utf-8'),
				self.getFloat(item['ML_Cuota_de_mantenimiento']),
				item['ML_Nro_de_departamentos_por_piso'].encode('utf-8'),
				item['ML_Elevador'].encode('utf-8'),
				item['ML_Estacionamiento'].encode('utf-8'),
				item['ML_Luminosidad'].encode('utf-8'),

				self.getFloat(item['ML_Metros2_de_jardin_comun']),
				self.getFloat(item['ML_Metros2_de_jardin']),

				item['ML_Titulo'].encode('utf-8'),
				item['ML_Descripcion'].encode('utf-8'),

				item['ML_Agua_Corriente'],
				item['ML_Aire_acondicionado'],
				item['ML_Alarma'],
				item['ML_Area_de_juegos_infantiles'],
				item['ML_Asador'],
				item['ML_Calefaccion'],
				item['ML_Cancha_de_squash'],
				item['ML_Cancha_de_tenis'],
				item['ML_Estacionamiento_para_visitantes'],
				item['ML_Gas_Natural'],
				item['ML_Conexion_a_internet'],
				item['ML_Jacuzzi'],
				item['ML_Jardin'],
				item['ML_Luz_electrica'],
				item['ML_Alberca'],
				item['ML_Salon_de_fiesta'],
				item['ML_Salon_de_usos_multiples_SOM'],
				item['ML_Telefono'],
				item['ML_Seguridad'],
				item['ML_Bodega'],
				item['ML_Cisterna'],
				item['ML_Cocina_integral'],
				item['ML_Recepcion'],
				item['ML_Comedor'],
				item['ML_Cuarto_de_TV'],
				item['ML_Cuarto_de_servicio'],
				item['ML_Estudio'],
				item['ML_Gimnasio'],
				item['ML_Living_comedor'],
				item['ML_Patio'],
				item['ML_Playroom'],
				item['ML_Terraza'],
				item['ML_Vestidor'],
				item['ML_Zotehuela'],
				
				item['ML_Moneda'].encode('utf-8'),
				self.getFloat(item['ML_Precio'])

	        ))

	        self.conn.commit()

	    except MySQLdb.Error, e:
	        print "Error %d: %s" % (e.args[0], e.args[1])	       
	        return item
