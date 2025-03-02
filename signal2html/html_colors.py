# -*- coding: utf-8 -*-

"""Colors extracted from Signal source

License: See LICENSE file.

"""

import random

CRIMSON = "#CC163D"
CRIMSON_TINT = "#EDA6AE"
CRIMSON_SHADE = "#8A0F29"
VERMILLION = "#C73800"
VERMILLION_TINT = "#EBA78E"
VERMILLION_SHADE = "#872600"
BURLAP = "#746C53"
BURLAP_TINT = "#C4B997"
BURLAP_SHADE = "#58513C"
FOREST = "#3B7845"
FOREST_TINT = "#8FCC9A"
FOREST_SHADE = "#2B5934"
WINTERGREEN = "#1C8260"
WINTERGREEN_TINT = "#9BCFBD"
WINTERGREEN_SHADE = "#36544A"
TEAL = "#067589"
TEAL_TINT = "#A5CAD5"
TEAL_SHADE = "#055968"
BLUE = "#336BA3"
BLUE_TINT = "#ADC8E1"
BLUE_SHADE = "#285480"
INDIGO = "#5951C8"
INDIGO_TINT = "#C2C1E7"
INDIGO_SHADE = "#4840A0"
VIOLET = "#862CAF"
VIOLET_TINT = "#CDADDC"
VIOLET_SHADE = "#6B248A"
PLUMB = "#A23474"
PLUMB_TINT = "#DCB2CA"
PLUMB_SHADE = "#881B5B"
TAUPE = "#895D66"
TAUPE_TINT = "#CFB5BB"
TAUPE_SHADE = "#6A4E54"
STEEL = "#6B6B78"
STEEL_TINT = "#BEBEC6"
STEEL_SHADE = "#5A5A63"
ULTRAMARINE = "@COLOR/CORE_ULTRAMARINE"
ULTRAMARINE_TINT = "#B0C8F9"
ULTRAMARINE_SHADE = "#1851B4"
GROUP = "@COLOR/CORE_ULTRAMARINE"
GROUP_TINT = "#B0C8F9"
GROUP_SHADE = "#1851B4"

COLORMAP = {
    "red": CRIMSON,
    "deep_orange": CRIMSON,
    "orange": VERMILLION,
    "amber": VERMILLION,
    "brown": BURLAP,
    "yellow": BURLAP,
    "pink": PLUMB,
    "purple": VIOLET,
    "deep_purple": VIOLET,
    "indigo": INDIGO,
    "blue": BLUE,
    "light_blue": BLUE,
    "cyan": TEAL,
    "teal": TEAL,
    "green": FOREST,
    "light_green": WINTERGREEN,
    "lime": WINTERGREEN,
    "blue_grey": TAUPE,
    "grey": STEEL,
    "ultramarine": ULTRAMARINE,
    "group_color": GROUP,
}


def get_random_color():
    return random.choice(list(COLORMAP.keys()))
