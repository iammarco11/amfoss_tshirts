from django.shortcuts import render
from tshirt.forms import UserForm, UserProfileInfoForm , CartForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse ,Http404, HttpRequest
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Tshirt, Cart
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect, render
def index(request):
    return render(request,'tshirt/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'tshirt/registeration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'tshirt/login.html', {})
class ProductDetailView(DetailView):
    model = Tshirt
    template_name = 'tshirt/product-detail.html'
    

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['form'] = CartForm(initial={'product': self.get_object()})
        return context

    def post(self, request, *args, **kwargs):
        
        form = CartForm(self.request.POST)
        self.object = self.get_object()
        if form.is_valid():
            form = form.save(commit=False)
            form.user = self.request.user
            form.save()
            return redirect('tshirt:cart')
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class CartView(ListView):
    template_name = 'tshirt/cart.html'
    model = Cart
    def post(self, request, *args, **kwargs):
        cart_id = self.request.POST.get('cart_id')
        cart_obj = Cart.objects.filter(id=cart_id).first()
        if cart_obj:
            cart_obj.delete()
            return redirect('tshirt:cart')
        raise Http404()
     
class ProductListView(ListView):
    template_name = 'tshirt/index.html'
    model = Tshirt
    