from re import split
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages, auth

from .forms import KhungDangKi
from .models import Taikhoan
from carts.views import _cart_id
from carts.models import Cart, CartItem


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = KhungDangKi(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]

            user = Taikhoan.objects.create_user(first_name=first_name,
                                                last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your Aram Account'
            message = render_to_string('accounts/active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            send_email = EmailMessage(mail_subject, message, to=[email])
            send_email.send()
            messages.success(request, "Confirm your email address to complete the registration")
            return redirect('register')
        else:
            messages.error(request, "Register failed!")
    else:
        form = KhungDangKi()
    context = {'form': form}
    return render(request, 'accounts/register.html', context=context)


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                cart_items = CartItem.objects.filter(cart=cart)
                if cart_items.exists():
                    product_variation = []
                    for cart_item in cart_items:
                        variations = cart_item.variations.all()
                        product_variation.append(list(variations))
                    cart_items = CartItem.objects.filter(user=user)
                    existing_variation_list = [list(item.variations.all()) for item in cart_items]
                    id_items = [item.id for item in cart_items]

                    for product in product_variation:
                        if product in existing_variation_list:
                            index = existing_variation_list.index(product)
                            item_id = id_items[index]
                            item = CartItem.objects.get(id=item_id)
                            item.quantiny += 1
                            item.user = user
                            item.save()
                        else:
                            cart_items = CartItem.objects.filter(cart=cart)
                            for item in cart_items:
                                item.user = user
                                item.save()
            except Exception:
                print(str(Exception))
            auth.login(request=request, user=user)
            messages.success(request, "Login successful")

            url = request.META.get('HTTP_REFERER')
            try:
                query = request.utils.urlparse(url).query
                params = dict(x.split("x") for x in query.split("&"))
                if 'next' in params:
                    next_page = params['next']
                    return redirect(next_page)
            except Exception:
                return redirect('dashboard')
        else:
            messages.error(request, "Login failed!")
            messages.error(request, "Make sure that your Aram Account is activated !")
    context = {
        'email': email if 'email' in locals() else '',
        'password ': password if 'password' in locals() else '',
    }
    return render(request, 'accounts/login.html', context=context)


@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out!')
    return redirect('login')


@login_required(login_url="login")
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Taikhoan.objects.get(pk=uid)
    except Exception:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account is activated, please login!")
        return render(request, 'accounts/login.html')
    else:
        messages.error(request, "Activation link is invalid!")
        return redirect('shopping_center')


def reset_password_validate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Taikhoan.objects.get(pk=uid)
    except Exception:
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid'] = uid
        messages.info(request,'Reset your password')
        return redirect('reset_password')
    else:
        messages.error(request,"This link has been expired!")
        return redirect('shopping_center')


def reset_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Taikhoan.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,"Password reset successful")
            return redirect('login')
        else:
            messages.error(request,"Password do not match")
    return render(request, 'accounts/reset_password.html')


def forgotPassword(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            user = Taikhoan.objects.get(email__exact=email)

            cur_site = get_current_site(request)
            mail_subject = 'Reset your password'
            message = render_to_string('accounts/reset_password_email.html',{
                'user': user,
                'domain': cur_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            send_email = EmailMessage(mail_subject,message,to=[email])
            send_email.send()

            messages.success(request,"Password reset email has been sent to your email address")
    except Exception:
        messages.error(request, "Account does not exist!")
    finally:
        context = {
            'email': email if 'email' in locals() else '',
        }
    return render(request, "accounts/forgotPassword.html", context=context)


@login_required(login_url="login")
def change_password(request):
    if request.method == 'POST':
        email = request.user.email
        cur_password = request.POST.get('cur_password')

        user = auth.authenticate(email=email, password=cur_password)
        if user is not None:
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password != confirm_password:
                messages.info(request, "The password confirmation does not match.")
            else:
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request, "Password reset successful")

                try:
                    cur_site = get_current_site(request)
                    mail_subject = 'Password reset successful'
                    message = render_to_string('accounts/change_email.html', {
                        'user': user,
                        'domain': cur_site.domain,
                    })
                    send_email = EmailMessage(mail_subject, message, to=[email])
                    send_email.send()
                except Exception:
                    print(str(Exception))

                return redirect('login')
        else:
            messages.info(request,"Wrong current password!")
    return render(request, "accounts/change_password.html")
