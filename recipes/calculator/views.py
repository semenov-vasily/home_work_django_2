from django.core.paginator import Paginator
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1
    }
}


# Функция домашней страницы
def home(request):
    # Получаем номер страницы блюда (по-умолчанию 1)
    num = int(request.GET.get('page', 1))
    # Используем пагинацию для вывода 1 блюда из словаря DATA на страницу
    paginator = Paginator([{key: value} for key, value in DATA.items()], 2)
    # Формируем данные для отправки в шаблон и вывода на страницу
    page = paginator.get_page(num)
    data = {'title': 'Главная страница',
            'page': page,
            }
    return render(request, 'calculator/home.html', context=data)


# Функция страницы блюда
def recipes(request, dish):
    # Получаем коэффициент для умножения количества каждого ингредиента в блюде (по-умолчанию 1)
    num = int(request.GET.get('servings', 1))
    # Получаем блюдо (словарь ингредиенты:количество) из словаря DATA
    dish_ingredients = DATA[dish]
    # Создаем новый словарь (ингредиенты:количество) данного блюда, чтобы не записывать изменения в словарь DATA
    dish_ingredients = {key:value for key,value in dish_ingredients.items()}
    for key, value in dish_ingredients.items():
        # Умножаем коэффициент на количество каждого ингредиента в блюде (по-умолчанию 1)
        dish_ingredients[key] = round(value * num, 2)
    data = {'title': 'Страница блюда',
            'dish': dish,
            'recipe': dish_ingredients,
            }
    return render(request, 'calculator/index.html', context=data)
