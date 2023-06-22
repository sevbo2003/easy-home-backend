from modeltranslation.translator import translator, TranslationOptions
from apps.news.models import News, Category


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content',)

translator.register(News, NewsTranslationOptions)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)