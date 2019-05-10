# Generated by Django 2.1.3 on 2019-04-03 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='接口名称')),
                ('body', models.TextField(verbose_name='主体信息')),
                ('url', models.CharField(max_length=200, verbose_name='请求地址')),
                ('method', models.CharField(max_length=10, verbose_name='请求方式')),
                ('relation', models.IntegerField(verbose_name='节点id')),
            ],
            options={
                'db_table': 'API',
                'verbose_name': '接口信息',
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='用例名称')),
                ('relation', models.IntegerField(verbose_name='节点id')),
                ('length', models.IntegerField(verbose_name='API个数')),
                ('tag', models.IntegerField(choices=[(1, '冒烟用例'), (2, '集成用例'), (3, '监控脚本')], default=2, verbose_name='用例标签')),
            ],
            options={
                'db_table': 'Case',
                'verbose_name': '用例信息',
            },
        ),
        migrations.CreateModel(
            name='CaseStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='用例名称')),
                ('body', models.TextField(verbose_name='主体信息')),
                ('url', models.CharField(max_length=200, verbose_name='请求地址')),
                ('method', models.CharField(max_length=10, verbose_name='请求方式')),
                ('step', models.IntegerField(verbose_name='顺序')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Case')),
            ],
            options={
                'db_table': 'CaseStep',
                'verbose_name': '用例信息 Step',
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='环境名称')),
                ('body', models.TextField(verbose_name='主体信息')),
                ('base_url', models.CharField(max_length=100, verbose_name='请求地址')),
            ],
            options={
                'db_table': 'Config',
                'verbose_name': '环境信息',
            },
        ),
        migrations.CreateModel(
            name='Debugtalk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(default='# write you code', verbose_name='python代码')),
            ],
            options={
                'db_table': 'Debugtalk',
                'verbose_name': '驱动库',
            },
        ),
        migrations.CreateModel(
            name='HostIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100)),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'HostIP',
                'verbose_name': 'HOST配置',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='项目名称')),
                ('desc', models.CharField(max_length=100, verbose_name='简要介绍')),
                ('responsible', models.CharField(max_length=20, verbose_name='创建人')),
            ],
            options={
                'db_table': 'Project',
                'verbose_name': '项目信息',
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree', models.TextField(default=[], verbose_name='结构主题')),
                ('type', models.IntegerField(default=1, verbose_name='树类型')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project')),
            ],
            options={
                'db_table': 'Relation',
                'verbose_name': '树形结构关系',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='报告名称')),
                ('type', models.IntegerField(choices=[(1, '调试'), (2, '异步'), (3, '定时')], verbose_name='报告类型')),
                ('summary', models.TextField(verbose_name='主体信息')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project')),
            ],
            options={
                'db_table': 'Report',
                'verbose_name': '测试报告',
            },
        ),
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=1024)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project')),
            ],
            options={
                'db_table': 'Variables',
                'verbose_name': '全局变量',
            },
        ),
        migrations.AddField(
            model_name='hostip',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project'),
        ),
        migrations.AddField(
            model_name='debugtalk',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project'),
        ),
        migrations.AddField(
            model_name='config',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project'),
        ),
        migrations.AddField(
            model_name='case',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project'),
        ),
        migrations.AddField(
            model_name='api',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project'),
        ),
    ]
