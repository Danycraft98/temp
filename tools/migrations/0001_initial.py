# Generated by Django 3.1.7 on 2021-05-07 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='카테고리 ID')),
                ('name', models.CharField(max_length=100, verbose_name='카테고리')),
                ('date_entered', models.DateTimeField(auto_now=True, verbose_name='등록일')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='static/uploads/', verbose_name='file')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('entered_date', models.DateTimeField(auto_now_add=True)),
                ('ca_id_extra', models.CharField(max_length=10, verbose_name='카테고리 ID')),
                ('it_id_extra', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('it_name', models.CharField(max_length=50, verbose_name='이름')),
                ('it_img_json', models.CharField(max_length=500, verbose_name='이미지 JSON')),
                ('it_origin', models.CharField(max_length=5, verbose_name='origin')),
                ('it_url', models.URLField(max_length=150, verbose_name='URL')),
                ('it_price', models.FloatField(verbose_name='Price')),
                ('it_whole_price', models.FloatField(verbose_name='Whole Price')),
            ],
        ),
        migrations.CreateModel(
            name='TourInfo',
            fields=[
                ('entered_date', models.DateTimeField(auto_now_add=True)),
                ('contentid', models.IntegerField(primary_key=True, serialize=False, verbose_name='컨텐트 ID')),
                ('contenttypeid', models.IntegerField(verbose_name='컨텐트 타입 ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('cat1', models.CharField(max_length=3, verbose_name='대분류 카테고리')),
                ('cat2', models.CharField(max_length=5, verbose_name='중분류 카테고리')),
                ('cat3', models.CharField(max_length=10, verbose_name='소분류 카테고리')),
                ('createdtime', models.IntegerField(verbose_name='Created Time')),
                ('modifiedtime', models.IntegerField(verbose_name='Modified Time')),
                ('eventstartdate', models.IntegerField(verbose_name='시작 날짜')),
                ('eventenddate', models.IntegerField(verbose_name='끝 날짜')),
                ('firstimage', models.URLField(max_length=150, verbose_name='First Image')),
                ('firstimage2', models.URLField(max_length=150, verbose_name='Second Image')),
                ('readcount', models.IntegerField(verbose_name='조회수')),
                ('tel', models.CharField(max_length=15, verbose_name='전화번호')),
                ('addr1', models.CharField(max_length=100, verbose_name='주소')),
                ('areacode', models.IntegerField(verbose_name='Area Code')),
                ('sigungucode', models.IntegerField(verbose_name='시군구 코드')),
                ('mapx', models.FloatField(verbose_name='X Coordinate')),
                ('mapy', models.FloatField(verbose_name='Y Coordinate')),
                ('mlevel', models.IntegerField(verbose_name='M Level')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ss_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='스마트스토어 샵ID')),
                ('mall_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='MALL ID')),
                ('url', models.URLField(max_length=150, verbose_name='URL')),
                ('notes', models.TextField(blank=True, max_length=150, null=True, verbose_name='비고')),
                ('quantity', models.IntegerField(default=0, verbose_name='상품 갯수')),
                ('date_entered', models.DateTimeField(auto_now=True, verbose_name='등록일')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='반영일')),
                ('edit', models.BooleanField(default=False, verbose_name='반영여부')),
                ('delete', models.BooleanField(default=False, verbose_name='삭제여부')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='tools.category', verbose_name='카테고리')),
            ],
        ),
    ]
