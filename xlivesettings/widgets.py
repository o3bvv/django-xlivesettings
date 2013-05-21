import logging

from django import forms
from django.utils.safestring import mark_safe

from xlivesettings import settings as x_setts

log = logging.getLogger(__name__)

class LocalizedStringValueFieldWidget(forms.MultiWidget):
    def __init__(self, langs=[], attrs=None):
        widgets = []
        for lang in langs:
            widget = forms.TextInput(attrs=attrs)
            widget.lang = lang
            widgets.append(widget)
        super(LocalizedStringValueFieldWidget, self).__init__(widgets, attrs)

    def value_from_datadict(self, data, files, name):
        try:
            return data.get(name, None).rsplit()
        except AttributeError:
            return [widget.value_from_datadict(data, files, name + '_%s' % i) for i, widget in enumerate(self.widgets)]

    def decompress(self, value):
        return dict(value) if value else {}

    def render(self, name, value, attrs=None):
        log.debug("render")
        if self.is_localized:
            for widget in self.widgets:
                widget.is_localized = self.is_localized
        # value is a list of values, each corresponding to a widget
        # in self.widgets.
        if not isinstance(value, dict):
            value = self.decompress(value)
        output = []
        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id', None)
        for i, widget in enumerate(self.widgets):
            lang_code = widget.lang
            try:
                widget_label = unicode(x_setts.LANGUAGES_DICT.get(lang_code, lang_code))
                widget_value = value[lang_code]
            except:
                widget_label, widget_value, lang_code = None, None, None
            if id_:
                final_attrs = dict(final_attrs, id='%s_%s' % (id_, i))

            output.append('<div class="form-row xsettings-multi-input">')
            output.append('<label for="%s">%s:</label>' % (final_attrs['id'], widget_label))
            output.append(widget.render(name + '_%s' % i, widget_value, final_attrs))
            output.append('</div>')

        return mark_safe(self.format_output(output))
