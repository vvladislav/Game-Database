# -*- coding: utf-8 -*-
"""
Created on Apr 2018

@author: Труханов А.И.
"""

def base():
    """
    База данных
    Возвращает список списков
    Поля = ["Название игры", "Жанр", "Платформа", "Год выпуска", "Цена",
            "Разработчик", "Издатель"]
    Автор Труханов А.И.
    """
    W1 = ["Warcraft", "Стратегия", "ПК", 1994, 499,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    W2 = ["Warcraft 2", "Стратегия", "ПК", 1995, 499,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    W3 = ["Warcraft 3", "Стратегия", "ПК", 2002, 499,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    WOW = ["World of Warcraft", "ММОРПГ", "ПК", 2004, 549,
           "Blizzard Entertainment", "Blizzard Entertainment"]
    D1 = ["Diablo", "РПГ", "ПК", 1996, 499,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    D2 = ["Diablo 2", "РПГ", "ПК", 2000, 499,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    D3 = ["Diablo 3", "РПГ", "ПК", 2012, 999,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    SC1 = ["Star Craft", "Стратегия", "ПК", 1998, 599,
           "Blizzard Entertainment", "Blizzard Entertainment"]
    SC2 = ["Star Craft 2", "Стратегия", "ПК", 2010, 1699,
           "Blizzard Entertainment", "Blizzard Entertainment"]
    HS = ["Hearthstone", "ККИ", "ПК", 2014, 0,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    HOTS = ["Heroes of the Storm", "МОБА", "ПК", 2015, 0,
            "Blizzard Entertainment", "Blizzard Entertainment"]
    OW = ["Overwatch", "Шутер", "ПК", 2016, 1999,
          "Blizzard Entertainment", "Blizzard Entertainment"]
    return [W1, W2, W3, WOW, D1, D2, D3, SC1, SC2, HS, HOTS, OW]
