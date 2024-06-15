from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(AboutUniversity)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')