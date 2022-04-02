from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from .forms import ImageForm, ApartmentForm
from .models import *


def index(request):
    return render(request, 'index.html')


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    apts = Apartment.objects.filter(category_id=slug)
    return render(request, 'category-detail.html', locals())

def apt_detail(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    image = apartment.get_image
    image = apartment.images.exclude(id=image.id)
    return render(request, 'apt-detail.html', locals())

def add_information(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    if request.method == 'POST':
        apt_form = ApartmentForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if apt_form.is_valid() and formset.is_valid():
            apartment = apt_form.save()
            for form in formset.cleaned_data:
                image = form['image']
                Image.objects.create(image=image, apartment=apartment)
            return redirect(apartment.get_absolute_url())
    else:
        apt_form = ApartmentForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'add_inf.html', locals())


def update_info(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    apt_form = ApartmentForm(request.POST or None, instance=apartment)
    formset = ImageFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.filter(apartment=apartment))
    if apt_form.is_valid() and formset.is_valid():
        apartment = apt_form.save()

        for form in formset:
            image = form.save(commit=False)
            image.apartment = apartment
            apartment.save()
            return redirect(apartment.get_absolute_url())
    return render(request, 'update-info.html', locals())



def delete_info(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    if request.method =="POST":
        apartment.delete()
        messages.add_message(request, messages.SUCCESS, 'Successfully deleted!')
        return redirect('home')
    return render(request, 'delete-info.html')

