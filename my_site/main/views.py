from django.shortcuts import redirect, render, HttpResponse
from .models import *
from cart.forms import CartAddProductForm, CartNewProductForm
from .forms import AddProductForm
# Create your views here.

def index(request):
    items = Catalog.objects.all()
    cart_product_form = CartNewProductForm()
    return render(request, 'main/index.html', {'items': items,
                                               'cart_product_form': cart_product_form})


def cheap(request):
    items = Catalog.objects.filter(price__lte=5000)
    return render(request, 'main/index.html', {'items': items})

def detail(request, item_id):
    try:
        item: object = Catalog.objects.get(id = item_id)
        cart_product_form = CartAddProductForm()
    except:
        return redirect("/")
    return (render(request, 'main/detail.html', {'item':item,
                                                 'cart_product_form': cart_product_form}))


def add_product(request):
    if request.method == "POST":
        Catalog(name = request.POST.get('name'), price = request.POST.get('price'), description = request.POST.get('description')).save()  
    else:
        pass
    add_form = AddProductForm()
    return render(request, 'main/add.html', {'add_form': add_form})
    

# # Напишите запрос Django ORM, чтобы получить все незавершенные задачи.
# unfinished_tasks = Task.objects.filter(completed=False)

# for task in unfinished_tasks:
#     print(task.title)

# # Напишите код для обновления email для клиента с именем "John".
# john_customer = Customer.objects.get(name="John")
# john_customer.email = "new_John@gmail.com"
# john_customer.save()

# # Напишите запрос Django ORM для удаления всех клиентов без электронной почты.
# Customer.objects.filter(email__isnull=True).delete()

# # Напишите запрос Django ORM, чтобы получить все книги, написанные определенным автором (например, "J.K. Rowling").
# jk_rowling_books = Book.objects.filter(author__name="J.K. Rowling")

# # Напишите код для добавления новой книги для существующего автора.
# author_jk_rowling = Author.objects.get(name="J.K. Rowling")
# new_book = Book(title="NEW HARRY POTTER", author=author_jk_rowling)
# new_book.save()