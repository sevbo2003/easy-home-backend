from modeltranslation.translator import translator, TranslationOptions
from apps.about.models import TeamMember


class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('position',)