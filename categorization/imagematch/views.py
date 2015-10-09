from django.forms.models import modelformset_factory
from django.shortcuts import render

from imagematch.models import Image


def match_images(request):
    ImageFormSet = modelformset_factory(
        Image,
        exclude=['zillow_id'],
        extra=0)

    if request.method == 'POST':
        formset = ImageFormSet(request.POST)
        for form in formset:
            form.is_valid()
            form.instance.category = form.cleaned_data["category"]
            form.instance.save()

    pks = map(lambda i: i.id, Image.objects.filter(category=None)[:50])
    formset = ImageFormSet(queryset=Image.objects.filter(pk__in=pks))

    return render(
        request,
        "cat.html",
        {"formset": formset},
        content_type="text/html")
