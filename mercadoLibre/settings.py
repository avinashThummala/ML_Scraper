# -*- coding: utf-8 -*-

BOT_NAME = 'mercadoLibre'

SPIDER_MODULES = ['mercadoLibre.spiders']
NEWSPIDER_MODULE = 'mercadoLibre.spiders'

ITEM_PIPELINES = {

    'mercadoLibre.pipelines.MercadolibrePipeline': 300,
}
