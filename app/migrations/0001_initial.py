# Generated by Django 3.2.7 on 2021-09-27 17:33

from django.db import migrations, models
import django.db.models.deletion
import django_cpf_cnpj.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', django_cpf_cnpj.fields.CNPJField(max_length=18)),
                ('telefone', models.CharField(max_length=14)),
                ('endereco', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('estoque', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(max_length=255)),
                ('imagem', models.CharField(max_length=255)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresa')),
            ],
        ),
    ]
