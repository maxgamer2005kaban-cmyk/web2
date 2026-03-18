from django.db import models

class Director(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Полное имя")
    birth_year = models.IntegerField(verbose_name="Год рождения")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"
        db_table = "directors"

class ProductType(models.Model):
    title = models.CharField(max_length=128, verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип продукта"
        verbose_name_plural = "Типы продуктов"
        db_table = "product_types"

class VideoProduct(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    release_year = models.IntegerField(verbose_name="Год выпуска")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Видеопродукт"
        verbose_name_plural = "Видеопродукты"
        db_table = "video_products"
