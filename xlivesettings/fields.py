import logging

from django import forms
from xlivesettings.widgets import LocalizedStringValueFieldWidget

log = logging.getLogger(__name__)

class LocalizedStringValueField(forms.MultiValueField):
    def __init__(self, langs=[], *args, **kwargs):
        self.langs = langs
        fields = [forms.CharField() for _ in langs]
        widget = LocalizedStringValueFieldWidget(langs)
        super(LocalizedStringValueField, self).__init__(fields=fields, widget=widget, *args, **kwargs)

    def compress(self, values):
        return tuple(zip(self.langs, values))
