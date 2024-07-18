from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Item,Category
from .forms import NewItemForm,EditItemForm



def items(request):
    query= request.GET.get('query','')
    category_id= request.GET.get('category',0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    

    if category_id:
        items = items.filter(category_id=category_id)


    if query:

        items = items.filter(name__icontains =query)



    return render(request,"item/items.html",{
        "items":items,
        "query":query,
        "categories":categories,
        "category_id":int(category_id),
        })


def detail(request,id):
    item = get_object_or_404(Item,id=id)
    related_item = Item.objects.filter(category = item.category, is_sold=False).exclude(id=id) [0:3]


    return render(request,'item/detail.html',{
        "item":item,
        'related_item':related_item,
        })

@login_required
def new(request):
    if request.method =='POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid:
            item =form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail',id=item.id)
    else:
        form =NewItemForm()
    return render(request,'item/newitem.html',{
        "form":form,})

@login_required
def delete(request,id):

    
    item = get_object_or_404(Item,id=id,created_by=request.user)
    item.delete()

    return render(request,'dashboard/index.html')

@login_required
def edit(request,id):
    item = get_object_or_404(Item,id=id,created_by=request.user)
    
    if request.method =='POST':
        form = EditItemForm(request.POST, request.FILES,instance=item,)

        if form.is_valid:
            item.save()
            return redirect('item:detail',id=item.id)
    else:
        form =EditItemForm(instance=item)
    return render(request,'item/edit.html',{
        "form":form,})