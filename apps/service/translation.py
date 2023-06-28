from modeltranslation.translator import translator, TranslationOptions
from apps.service.models import Service


class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'content',)

translator.register(Service, ServiceTranslationOptions)
