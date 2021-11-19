# Generated by Django 2.2.5 on 2019-09-23 09:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0004_auto_20190923_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='beneficio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='descripcion',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='descuento_compra',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='familia',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='fecha_compra',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='iva',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='marca',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='observaciones',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='pedido_proveedor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='precio_compra',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='precio_coste',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='precio_medio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='precio_venta',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='pvp_iva',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='referencia',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='reservados',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='stock_optimo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='stockable',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='subfamilia',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='tipo',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='a1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='a2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='b1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='b2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='ci',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='cl',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='cod417',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='cv',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='d1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='d2',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='d3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='d6',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='e',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='ep',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='ep1',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='ep2',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='ep3',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='ep4',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f1',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f11',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f15',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f2',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f21',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f3',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f31',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f4',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f5',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f51',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f6',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f61',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f7',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f71',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f8',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='f81',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='g',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='g1',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='g2',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='j',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='j1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='j2',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='j3',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='k',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='k1',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='k2',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='l',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='l0',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='l1',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='l2',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='libre',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='m1',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='m4',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='num_serie',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o1',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o11',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o12',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o13',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o14',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o21',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o22',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o23',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='o3',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='observaciones',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='opciones_hom_tipo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p1',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p11',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p2',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p21',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p3',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p5',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='p51',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='q',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='r',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='reformas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='s1',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='s11',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='s2',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='t',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='u1',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='u2',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='v7',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='v8',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='v9',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_tecnica',
            name='z',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='alarmas',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='banco',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='ccc',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='cif',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='cod_postal',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='cuenta_caja',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='cuenta_contable',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='cuenta_ingresos',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='cuenta_retencion',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='dir_banco',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='forma_pago',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='intracomunitario',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='irpf',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='iva',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='localidad',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='medio_pago',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='movil',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nueva_alarma',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='observaciones',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='pais',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='persona_contacto',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='provincia',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='saldo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='web',
            field=models.URLField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='asegurado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='combustible',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='fecha_cobro',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='fecha_inspeccion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='fecha_reparacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='kilometros',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='libro_mantenimiento',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='num_albaran',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='num_factura',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='num_peritacion',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='num_presupuesto',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='observaciones',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='tipo_descuento',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='vendedor_oper',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='asegurado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='aseguradora',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='bastidor',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='color',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='kilometros',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='modelo',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='num_poliza',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='observaciones',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='placa_oval',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='tipo_motor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
