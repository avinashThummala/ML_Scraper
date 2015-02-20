#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy, sys
from mercadoLibre.items import MercadolibreItem
from scrapy.http import Request
from scrapy import Selector

DOMAIN = 'mercadolibre.com.mx'
URL = 'http://inmuebles.%s/' % DOMAIN

class MLSpider(scrapy.Spider):

    name = 'mlspider'
    allowed_domains = [DOMAIN]
    start_urls = [
        URL
    ]

    def extractText(self, eList, index):

        if len(eList)>index:
            return eList[index].strip()

        else:
            return ''          

    def getDescription(self, hxs):

        description = ""

        for depth in range(5):

            string = "//div[@id=\'itemDescription\']/div/"+("*/"*depth)+"text()"

            eList = hxs.xpath(string).extract()

            for text in eList:
                description+=(text+"\n")
        
        return description                

    def checkList(self, eList, newItem):

        cList=[
            u'Agua Corriente', u'Aire acondicionado', u'Alarma', u'Area de juegos infantiles', u'Asador', u'Calefacci\xf3n', 
            u'Cancha de squash', u'Cancha de tenis', u'Estacionamiento para visitantes', u'Gas Natural', u'Conexi\xf3n a internet', 
            u'Jacuzzi', u'Jard\xedn', u'Luz el\xe9ctrica', u'Alberca', u'Sal\xf3n de fiesta', u'Sal\xf3n de usos múltiples (SOM)', u'Tel\xe9fono', 
            u'Seguridad', u'Bodega', u'Cisterna', u'Cocina integral', u'Recepci\xf3n', u'Comedor', u'Cuarto de TV', u'Cuarto de servicio', 
            u'Estudio', u'Gimnasio', u'Living comedor', u'Patio', u'Playroom', u'Terraza', u'Vestidor', u'Zotehuela'
        ]

        iList=[
            'ML_Agua_Corriente' ,'ML_Aire_acondicionado' ,'ML_Alarma' ,'ML_Area_de_juegos_infantiles' ,'ML_Asador' ,
            'ML_Calefaccion' ,'ML_Cancha_de_squash' ,'ML_Cancha_de_tenis' ,'ML_Estacionamiento_para_visitantes' ,'ML_Gas_Natural' ,
            'ML_Conexion_a_internet' ,'ML_Jacuzzi' ,'ML_Jardin' ,'ML_Luz_electrica' ,'ML_Alberca' ,'ML_Salon_de_fiesta', 
            'ML_Salon_de_usos_multiples_SOM' ,'ML_Telefono' ,'ML_Seguridad' ,'ML_Bodega' ,'ML_Cisterna' ,'ML_Cocina_integral' ,
            'ML_Recepcion' ,'ML_Comedor' ,'ML_Cuarto_de_TV' ,'ML_Cuarto_de_servicio' ,'ML_Estudio' ,'ML_Gimnasio' ,'ML_Living_comedor' ,
            'ML_Patio' ,'ML_Playroom' ,'ML_Terraza' ,'ML_Vestidor' ,'ML_Zotehuela'
        ]

        for x in iList:
            newItem[x]=0            

        for x in eList:

            x=x.strip()

            if x in cList:
                newItem[iList[cList.index(x)]]=1

    def getLocation(self, locationStr, newItem):

        newItem['ML_Latitude'] = ''
        newItem['ML_Longitude'] = ''        

        if locationStr.find('=')==-1 or locationStr.find('&')==-1:                
            return

        locationStrList = locationStr[locationStr.find('=')+1 : locationStr.find('&')].split(',')           
        
        newItem['ML_Latitude'] = self.extractText( locationStrList, 0)
        newItem['ML_Longitude'] = self.extractText( locationStrList, 1)

    def parseItem(self, response):

        hxs = Selector(response)
        
        newItem = MercadolibreItem()

        newItem['ML_Listing_URL'] = response.url
        newItem['ML_Ad_Code'] = self.extractText(hxs.xpath('//span[@class=\'id-item\']/text()').extract(), 0)[12:]

        newItem['ML_Type_of_real_estate'] = self.extractText(hxs.xpath('//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Inmueble:\']/strong/text()').extract(), 0)
        newItem['ML_Type_of_transaction'] = self.extractText( hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Operaci\xf3n:\']/strong/text()").extract(), 0)

        newItem['ML_Photo_1'] = self.extractText(hxs.xpath('//section[@id=\'shortDescription\']/div/figure/div[1]/a/@href').extract(), 0)
        newItem['ML_Photo_2'] = self.extractText(hxs.xpath('//section[@id=\'shortDescription\']/div/figure/div[2]/a/@href').extract(), 0)
        newItem['ML_Photo_3'] = self.extractText(hxs.xpath('//section[@id=\'shortDescription\']/div/figure/div[3]/a/@href').extract(), 0)
        newItem['ML_Photo_4'] = self.extractText(hxs.xpath('//section[@id=\'shortDescription\']/div/figure/div[4]/a/@href').extract(), 0)
        newItem['ML_Photo_5'] = self.extractText(hxs.xpath('//section[@id=\'shortDescription\']/div/figure/div[5]/a/@href').extract(), 0)
        newItem['ML_Photo_6'] = self.extractText(hxs.xpath('//section[@id=\'shortDescription\']/div/figure/div[6]/a/@href').extract(), 0)
        newItem['ML_Photo_7'] = self.extractText(hxs.xpath('//section[@id=\'shortDescription\']/div/figure/div[7]/a/@href').extract(), 0)
        newItem['ML_Photo_8'] = self.extractText(hxs.xpath('//section[@id=\'shortDescription\']/div/figure/div[8]/a/@href').extract(), 0)
        newItem['ML_Photo_9'] = self.extractText(hxs.xpath('//section[@id=\'shortDescription\']/div/figure/div[9]/a/@href').extract(), 0)
        newItem['ML_Photo_10'] = self.extractText(hxs.xpath('//section[@id=\'shortDescription\']/div/figure/div[10]/a/@href').extract(), 0)

        newItem['ML_Video'] = self.extractText(hxs.xpath('//section[@id=\'shortDescription\']/div/figure/div/object/embed/@src').extract(), 0)

        strList = self.extractText(hxs.xpath('//h2[@class=\'location\']/text()').extract(), 0).split(' - ')

        if len(strList) < 3:
            strList=(['']*(3-len(strList)))+strList

        newItem['ML_Provincia'] = strList[-1]
        newItem['ML_Barrio'] = strList[-2]
        newItem['ML_Calle'] = strList[-3]

        newStr = self.extractText(hxs.xpath('//div[@class=\'view-map\']/div/div[@id=\'mapa\']/img/@src').extract(), 0)        
        self.getLocation(newStr, newItem)

        newItem['ML_Telefone'] = self.extractText( hxs.xpath('//span[@class=\'seller-details-box showPhone\']/text()').extract(), 0)

        newItem['ML_Recamaras'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Rec\xe1maras:\']/strong/text()").extract(), 0)
        newItem['ML_Antiguedad'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Antig\xfcedad:\']/strong/text()").extract(), 0)
        newItem['ML_Banos'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Ba\xf1os:\']/strong/text()").extract(), 0)
        newItem['ML_Superficie_construida_m2'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Superficie construida (m\xb2):\']/strong/text()").extract(), 0)
        newItem['ML_Superficie_total_m2'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Superficie total (m\xb2):\']/strong/text()").extract(), 0)
        newItem['ML_Disposicion'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Disposici\xf3n:\']/strong/text()").extract(), 0)

        newItem['ML_Horario_de_contacto'] = self.extractText(hxs.xpath('//dd[@class=\'seller-hours\']/span/text()').extract(), 0)
        newItem['ML_Amueblado'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Amueblado:\']/strong/text()").extract(), 0)
        newItem['ML_Apto_Profesional'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Apto profesional:\']/strong/text()").extract(), 0)        
        newItem['ML_Balcon'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Balc\xf3n:\']/strong/text()").extract(), 0)
        newItem['ML_Cant_de_pisos_del_edificio'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Cant.de pisos del edificio:\']/strong/text()").extract(), 0)

        newItem['ML_Conservacion'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Conservaci\xf3n:\']/strong/text()").extract(), 0)
        newItem['ML_Cuota_de_mantenimiento'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Cuota de mantenimiento ($):\']/strong/text()").extract(), 0)
        newItem['ML_Nro_de_departamentos_por_piso'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Departamentos por piso:\']/strong/text()").extract(), 0)

        newItem['ML_Elevador'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Elevador:\']/strong/text()").extract(), 0)
        newItem['ML_Estacionamiento'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Estacionamiento:\']/strong/text()").extract(), 0)
        newItem['ML_Luminosidad'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Luminosidad:\']/strong/text()").extract(), 0)
        newItem['ML_Metros2_de_jardin_comun'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Metros\xb2 de jard\xedn com\xfan:\']/strong/text()").extract(), 0)
        newItem['ML_Metros2_de_jardin'] = self.extractText(hxs.xpath(u"//div[@id=\'techDataHolder\']/ul/li[span/text()=\'Metros\xb2 de jard\xedn:\']/strong/text()").extract(), 0)

        newItem['ML_Titulo'] = self.extractText(hxs.xpath(u"//h2[@class=\'tit-description\']/span/text()").extract(), 0)
        newItem['ML_Descripcion'] = self.getDescription(hxs)

        self.checkList(hxs.xpath('//div[@id=\'techDataHolder\']/ul[@class=\'other-details\']/li/h3/text()').extract(), newItem)            

        strList = self.extractText(hxs.xpath('//div[@class=\'product-info\']/fieldset/article[1]/strong/text()').extract(), 0).split(' ')
            
        newItem['ML_Moneda'] = self.extractText( strList, 0)
        newItem['ML_Precio'] = self.extractText( strList, 1)

        yield newItem

    def parse(self, response):

        hxs = Selector(response)

        nextURL = hxs.xpath('/*/head/link[@rel=\"next\"]/@href').extract()[0]

        for url in hxs.xpath('//a/@href').extract():

            if not url.startswith('http://'):
                url= URL + url 
                        
            if 'mercadolibre.com.mx/MLM-' in url:
                yield Request(url+"?noIndex=true&showPhones=true", callback=self.parseItem)
                           
        if len(nextURL):                
            yield Request(nextURL, callback=self.parse)                            