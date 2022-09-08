

class BulmaMixin(object):
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.widget.input_type in ('text', 'email', 'password', 'number', 'url'):
                visible.field.widget.attrs['class'] = 'input'
            elif visible.field.widget.input_type == 'file':
                visible.field.widget.template_name = 'file_input.html'