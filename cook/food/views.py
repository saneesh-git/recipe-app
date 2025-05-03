from django.shortcuts import render,redirect
from.models import recipie_tbl
# Create your views here.
def index(request):
    return render(request,'index.html')

def addrecpe(request):
    if request.method == 'POST':
        title = request.POST.get("title") 
        img = request.POST.get("image")
        ingrts= request.POST.get("ingrediants")
        dscptn= request.POST.get("description")
        instn= request.POST.get("instructions")
        obj = recipie_tbl.objects.create(title=title,image=img,description=dscptn,ingrediants=ingrts,instructions=instn)
        obj.save()
        if obj:
            return redirect('/addrecpe')
    return render(request,'addrecpe.html')
def searchrecipie(request):
    rec = []
    if request.method == 'POST':
        ing = request.POST.get('ing', '').strip()
        if ing:
            rec = recipie_tbl.objects.filter(ingre__icontains=ing)
    return render(request, "search.html", {"rec": rec})