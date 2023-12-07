from django.db import models

# Create your models here.
class Catalog(models.Model):
    name = models.CharField(verbose_name="Название товара", max_length=60)
    price = models.IntegerField(verbose_name="Цена",)
    photo = models.ImageField(verbose_name="Фото товара", upload_to="photo/%Y/%m/%d/", default='photo\2023\11\16\Empty.png')
    description = models.TextField(verbose_name="Описание товара", default='')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория", null=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = "Товары"
        ordering = ['name']

class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=60)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
        ordering = ['name']


# Создайте модель Task с полями title (CharField) и completed (BooleanField).    
class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title

# Создайте модель Customer с полями name (CharField) и email (EmailField).    
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name

# Создайте две модели: Author (с полями name - CharField) и Book (с полями title - CharField и author - ForeignKey).    
class Author(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)    
    def __str__(self) -> str:
        return self.title

# # CRUD
# save()
# # Create
# # Создаете объект модели, наполняете значениями, потом save()
# # >>> a = Catalog()
# # >>> a.name = 'Спортивные носки'
# # >>> a.price = 500
# # >>> a.save()
# # Read
# all()
# get()
# count()
# filter()
# # Update
# # Сначала read запрос. Приравниваете значения из запроса, потом save()
# # Delete
# delete()
