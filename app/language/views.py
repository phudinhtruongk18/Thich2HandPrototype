from django.conf.urls.i18n import i18n_patterns
from django.shortcuts import render
from django.utils.translation import activate, get_language
from django.utils.translation import gettext
from django.utils.translation import gettext as _

from .models import Language

# Create your views here.


def _language_id(request):
    language_id = request.session.session_key
    if not language_id:
        language_id = request.session.create()
    return language_id


def language(request):
    try:
        if request.user.is_authenticated:
            if request.POST.get("language") == "vi":
                request.user.language = "vi"
            elif request.POST.get("language") == "en":
                request.user.language = "en"
            else:
                pass
            request.user.save()
            activate(request.user.language)
        else:
            try:
                language = Language.objects.get(
                    language_id=_language_id(request=request)
                )  # Get cart using the _cart_id
            except Language.DoesNotExist:
                language = Language.objects.create(
                    language_id=_language_id(request=request)
                )

            request_language = request.POST.get("language")

            if request_language is not None:
                if request_language == "vi":
                    language.language_code = "vi"
                elif request_language == "en":
                    language.language_code = "en"
                language.save()
            else:
                pass
            activate(language.language_code)
        return True
    except Exception as e:
        print("Debug language", e)
        return False
