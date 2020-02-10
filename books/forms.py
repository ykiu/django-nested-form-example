from django.forms import ModelForm, inlineformset_factory
from .models import Auther, Book

class ModelFormWithFormSetMixin:

    def __init__(self, *args, **kwargs):
        super(ModelFormWithFormSetMixin, self).__init__(*args, **kwargs)
        self.formset = self.formset_class(
            instance=self.instance,
            data=self.data if self.is_bound else None,
        )

    def is_valid(self):
        return super(ModelFormWithFormSetMixin, self).is_valid() and self.formset.is_valid()

    def save(self, commit=True):
        saved_instance = super(ModelFormWithFormSetMixin, self).save(commit)
        self.formset.save(commit)
        return saved_instance


class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = ('title',)

BookFormSet = inlineformset_factory(
    parent_model=Auther,
    model=Book,
    form=BookForm,
    extra=3
)


class AutherForm(ModelFormWithFormSetMixin, ModelForm):

    formset_class = BookFormSet

    class Meta:
        model = Auther
        fields = ('name',)
