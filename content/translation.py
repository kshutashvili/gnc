from modeltranslation.translator import translator, TranslationOptions

from .models import Document


class DocumentTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'content',
        'browser_title'
    )


translator.register(Document, DocumentTranslationOptions)
