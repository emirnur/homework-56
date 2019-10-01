from django.views.generic import TemplateView


class ListView(TemplateView):
    context_key = 'objects'
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.get_objects()
        return context

    def get_objects(self):
        return self.model.objects.all()
