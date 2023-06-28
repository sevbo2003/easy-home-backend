from modeltranslation.translator import translator, TranslationOptions
from apps.products.models import Category


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)