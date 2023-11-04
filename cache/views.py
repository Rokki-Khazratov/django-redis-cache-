from django.shortcuts import render
from django.core.cache import cache
from cache.models import News

def data_tracker(request):
    # Попробуйте получить данные из кеша (Redis)
    cached_data = cache.get( News.objects.get(id=id) )

    if cached_data is None:
        # Если данных нет в кеше, загрузите их из базы данных (PostgreSQL)
        data_from_db = News.objects.all()
        
        # Затем сохраните данные в кеш
        cache.set("my_key", data_from_db, 300)  # 300 секунд кеширования

        return render(request, 'news.html', {'data': data_from_db})
    else:
        return render(request, 'news.html', {'data': cached_data})
