from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RecordForm
from .models import Record

# Create your views here.


def demo_model(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            age = form.cleaned_data["age"]
            gender = form.cleaned_data["gender"]
            salary = form.cleaned_data["salary"]

            pre = Record.objects.create(
                name=name, age=age, gender=gender, salary=salary
            )
            pre.save()
            if pre.predict_ads_click():
                print("----->", pre.purchased)
                return redirect("demo_model")
            else:
                messages.error(request, "Predict failed!")
    else:
        form = RecordForm()

    result_list = Record.objects.all()
    result_list = result_list[::-1]
    context = {
        "form": form,
        "pre": pre if "pre" in locals() else None,
        "result_list": result_list,
    }
    return render(request, "binary_model/predict.html", context=context)
