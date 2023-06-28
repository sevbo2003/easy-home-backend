from modeltranslation.translator import translator, TranslationOptions
from apps.products.models import Category, Product, Parameter, Document


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(Product, ProductTranslationOptions)


class ParameterTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Parameter, ParameterTranslationOptions)


class DocumentTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Document, DocumentTranslationOptions)
