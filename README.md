# Fish_Prj
В папке data/ собраны данные, необходимые для анализа и обучения эвристической модели:
    *sity.csv - это справочник Российских городов с координатами (широта и долгота)
    *moon_phases_UTC_1800-2050.csv - это справочник лунных фаз (изменение состояния фазы луны в зависимости от географического положения почти не изменяется, так что это можно посчитать за допустимую погрешность и взять календарь на много лет вперед)
    *raw/weather/ - сырые json полученные с Open Weather

Источники данных:
    Города - https://raw.githubusercontent.com/hflabs/city/master/city.csv
    Фазы луны - https://raw.githubusercontent.com/isaacbernat/moon-data/refs/heads/main/moon_phases_UTC_1800-2050.csv