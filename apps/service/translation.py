from modeltranslation.translator import translator, TranslationOptions
from apps.service.models import Service, KeyFeatures


class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'content',)

translator.register(Service, ServiceTranslationOptions)


class KeyFeaturesTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(KeyFeatures, KeyFeaturesTranslationOptions)
