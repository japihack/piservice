# Generated by Django 2.2.5 on 2019-09-23 09:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0003_cliente_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='beneficio',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='descripcion',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='descuento_compra',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='familia',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='fecha_compra',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='iva',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='marca',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='observaciones',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='pedido_proveedor',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='precio_compra',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='precio_coste',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='precio_medio',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='precio_venta',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='pvp_iva',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='referencia',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='reservados',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='stock',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='stock_optimo',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='stockable',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='subfamilia',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='tipo',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='observaciones',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='a1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='a2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='b1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='b2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='ci',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='cl',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='cod417',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='cv',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='d1',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='d2',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='d3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='d6',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='e',
            field=models.CharField(max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='ep',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='ep1',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='ep2',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='ep3',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='ep4',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f1',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f11',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f15',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f2',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f21',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f3',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f31',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f4',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f5',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f51',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f6',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f61',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f7',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f71',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f8',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f81',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='g',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='g1',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='g2',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='j',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='j1',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='j2',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='j3',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='k',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='k1',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='k2',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='l',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='l0',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='l1',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='l2',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='libre',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='m1',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='m4',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='num_serie',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o1',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o11',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o12',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o13',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o14',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o21',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o22',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o23',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o3',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='observaciones',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='opciones_hom_tipo',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p1',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p11',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p2',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p21',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p3',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p5',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p51',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='q',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='r',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='reformas',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='s1',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='s11',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='s2',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='t',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='u1',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='u2',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='v7',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='v8',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='v9',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='z',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='asegurado',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='combustible',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='fecha_cobro',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='fecha_inspeccion',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='fecha_reparacion',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='kilometros',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='libro_mantenimiento',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='num_albaran',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='num_factura',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='num_peritacion',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='num_presupuesto',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='observaciones',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='tipo_descuento',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='vendedor_oper',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='aseguradora',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='bastidor',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='color',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='modelo',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='num_poliza',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='observaciones',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='placa_oval',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='tipo_motor',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]