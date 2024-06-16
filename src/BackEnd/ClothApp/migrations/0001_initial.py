# Generated by Django 5.0.6 on 2024-06-10 18:00

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen_url', models.URLField(default='https://www.shutterstock.com/image-vector/error-500-page-empty-symbol-260nw-1711106146.jpg')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion_corta', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('imagen_url', models.URLField(default='https://www.shutterstock.com/image-vector/error-500-page-empty-symbol-260nw-1711106146.jpg')),
                ('contenido', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prenda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=100)),
                ('imagen_url', models.URLField(default='https://www.shutterstock.com/image-vector/error-500-page-empty-symbol-260nw-1711106146.jpg')),
                ('talla', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3)),
                ('cantidad_stock', models.PositiveIntegerField(default=0)),
                ('material', models.CharField(choices=[('Algodón', 'Algodón'), ('Poliéster', 'Poliéster'), ('Lino', 'Lino'), ('Lana', 'Lana'), ('Seda', 'Seda'), ('Nylon', 'Nylon'), ('Lycra', 'Lycra')], max_length=50)),
                ('precio_original', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_rebajado', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('tipo_prenda', models.CharField(choices=[('Sudaderas', 'Sudaderas'), ('Camisas', 'Camisas'), ('Camisetas', 'Camisetas'), ('Polos', 'Polos'), ('Pantalón', 'Pantalón'), ('Top', 'Top'), ('Faldas', 'Faldas'), ('Vestidos', 'Vestidos'), ('Calcetines', 'Calcetines'), ('Calzado', 'Calzado'), ('Baño', 'Baño'), ('Accesorios', 'Accesorios')], default='Camisetas', max_length=50)),
                ('color', models.CharField(choices=[('Amarillo', 'Amarillo'), ('Azul', 'Azul'), ('Azul Celeste', 'Azul Celeste'), ('Azul Eléctrico', 'Azul Eléctrico'), ('Azul Marino', 'Azul Marino'), ('Azul Oscuro', 'Azul Oscuro'), ('Azul Turquesa', 'Azul Turquesa'), ('Beige', 'Beige'), ('Blanco', 'Blanco'), ('Blanco Roto', 'Blanco Roto'), ('Blanco y Negro', 'Blanco y Negro'), ('Caqui', 'Caqui'), ('Coral', 'Coral'), ('Granate', 'Granate'), ('Gris', 'Gris'), ('Gris Oscuro', 'Gris Oscuro'), ('Lila', 'Lila'), ('Marrón', 'Marrón'), ('Multicolor', 'Multicolor'), ('Naranja', 'Naranja'), ('Negro', 'Negro'), ('Oro', 'Oro'), ('Plata', 'Plata'), ('Rojo', 'Rojo'), ('Rosa', 'Rosa'), ('Verde', 'Verde'), ('Verde Oscuro', 'Verde Oscuro')], default='Blanco', max_length=20)),
                ('genero', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer'), ('Niño', 'Niño'), ('Niña', 'Niña')], default='Hombre', max_length=6)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClothApp.marca')),
            ],
            options={
                'verbose_name': 'Prenda',
                'verbose_name_plural': 'Prendas',
            },
        ),
    ]
