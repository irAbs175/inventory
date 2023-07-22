# Generated by Django 4.2.3 on 2023-07-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Materials",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "material_author",
                    models.CharField(max_length=40, verbose_name="اپراتور ثبت"),
                ),
                ("material_name", models.CharField(max_length=300, verbose_name="نام")),
                ("material_code", models.CharField(max_length=50, verbose_name="کد")),
                ("material_color", models.CharField(max_length=50, verbose_name="رنگ")),
                (
                    "material_quantity",
                    models.PositiveIntegerField(null=True, verbose_name="موجودی"),
                ),
                (
                    "material_location",
                    models.CharField(max_length=50, verbose_name="انبار"),
                ),
                (
                    "material_hall",
                    models.CharField(max_length=20, verbose_name="سالن انبار"),
                ),
                ("material_unit", models.CharField(max_length=20, verbose_name="واحد")),
                (
                    "material_date",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="زمان دقیق ثبت"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="فعال / غیرفعال"),
                ),
                (
                    "is_available",
                    models.BooleanField(
                        default=True, verbose_name="موجودی / عدم موجودی"
                    ),
                ),
            ],
            options={
                "verbose_name": "ماده اولیه",
                "verbose_name_plural": "مواد اولیه",
            },
        ),
        migrations.CreateModel(
            name="MaterialsCardex",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(max_length=40, verbose_name="اپراتور ثبت")),
                (
                    "material",
                    models.CharField(max_length=50, verbose_name="ماده اولیه"),
                ),
                (
                    "factor_number",
                    models.CharField(max_length=50, verbose_name="شماره فاکتور"),
                ),
                (
                    "number",
                    models.PositiveIntegerField(null=True, verbose_name="تعداد"),
                ),
                (
                    "description",
                    models.CharField(max_length=300, verbose_name="شرح عملیات"),
                ),
                ("operation", models.CharField(max_length=20, verbose_name="عملیات")),
                (
                    "date",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="زمان ثبت"
                    ),
                ),
            ],
            options={
                "verbose_name": "کاردکس",
                "verbose_name_plural": "کاردکس مواد اولیه",
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product_author",
                    models.CharField(max_length=40, verbose_name="اپراتور ثبت"),
                ),
                (
                    "product_name",
                    models.CharField(max_length=300, verbose_name="نام کالا"),
                ),
                (
                    "product_code",
                    models.CharField(max_length=50, verbose_name="کد کالا"),
                ),
                (
                    "product_color",
                    models.CharField(max_length=50, verbose_name="رنگ کالا"),
                ),
                (
                    "product_quantity",
                    models.PositiveIntegerField(null=True, verbose_name="موجودی کالا"),
                ),
                (
                    "product_location",
                    models.CharField(max_length=50, verbose_name="انبار کالا"),
                ),
                (
                    "product_hall",
                    models.CharField(max_length=20, verbose_name="سالن انبار کالا"),
                ),
                ("product_unit", models.CharField(max_length=20, verbose_name="واحد")),
                (
                    "product_date",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="زمان دقیق ثبت"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="فعال / غیرفعال"),
                ),
                (
                    "is_available",
                    models.BooleanField(
                        default=True, verbose_name="موجودی / عدم موجودی"
                    ),
                ),
            ],
            options={
                "verbose_name": "کالا",
                "verbose_name_plural": "کالاها",
            },
        ),
        migrations.CreateModel(
            name="ProductsCardex",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(max_length=40, verbose_name="اپراتور ثبت")),
                ("product", models.CharField(max_length=50, verbose_name="کالا")),
                (
                    "factor_number",
                    models.CharField(max_length=50, verbose_name="شماره فاکتور"),
                ),
                (
                    "number",
                    models.PositiveIntegerField(null=True, verbose_name="تعداد"),
                ),
                (
                    "description",
                    models.CharField(max_length=300, verbose_name="شرح عملیات"),
                ),
                ("operation", models.CharField(max_length=20, verbose_name="عملیات")),
                (
                    "date",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="زمان ثبت"
                    ),
                ),
            ],
            options={
                "verbose_name": "کاردکس",
                "verbose_name_plural": "کاردکس کالاها",
                "ordering": ["-date"],
            },
        ),
    ]