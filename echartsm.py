"""
Defines custom ECharts bokeh model to render Vega json plots.
"""
from bokeh.core.properties import Any, Dict, Enum, String
from bokeh.models import LayoutDOM

from ..io.resources import bundled_files
from ..util import classproperty


class ECharts(LayoutDOM):
    """
    A Bokeh model that wraps around an ECharts plot and renders it
    inside a Bokeh.
    """

#https://cdn.jsdelivr.net/npm/echarts-countries-js@1.0.4/echarts-countries-js/Afghanistan.js
#https://cdn.jsdelivr.net/npm/echarts-cities-js@1.0.0/echarts-cities-js/AD.json


    __javascript_raw__ = [
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/dist/echarts.js",
        "https://cdn.jsdelivr.net/npm/echarts-gl@2.0.2/dist/echarts-gl.min.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/azul.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/bee-inspired.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/blue.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/caravan.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/carp.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/cool.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/dark.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/dark-blue.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/dark-bold.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/dark-digerati.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/dark-fresh-cut.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/dark-mushroom.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/eduardo.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/forest.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/fresh-cut.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/fruit.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/gray.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/green.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/helianthus.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/infographic.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/inspired.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/jazz.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/london.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/macarons.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/macarons2.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/mint.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/red.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/red-velvet.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/roma.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/royal.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/sakura.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/shine.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/tech-blue.js",
        "https://cdn.jsdelivr.net/npm/echarts@5.1.2/theme/vintage.js"
    ]

    @classproperty
    def __javascript__(cls):
        return bundled_files(cls)

    @classproperty
    def __js_skip__(cls):
        return {
            'echarts': cls.__javascript__[:1]
        }

    __js_require__ = {
        'baseUrl': 'https://www.jsdelivr.com/package/npm/',
        'paths': {
            "echarts":  "echarts@5.1.2/dist/echarts.js",
            "echarts-gl": "echarts-gl@2.0.5/dist/echarts-gl.js",
            "azul": "echarts@5.1.2/theme/azul.js",
            "bee-inspired": "echarts@5.1.2/theme/bee-inspired.js",
            "blue": "echarts@5.1.2/theme/blue.js",
            "caravan": "echarts@5.1.2/theme/caravan.js",
            "carp": "echarts@5.1.2/theme/carp.js",
            "cool": "echarts@5.1.2/theme/cool.js",
            "dark": "echarts@5.1.2/theme/dark.js",
            "dark-blue": "echarts@5.1.2/theme/dark-blue.js",
            "dark-bold": "echarts@5.1.2/theme/dark-bold.js",
            "dark-digerati": "echarts@5.1.2/theme/dark-digerati.js",
            "dark-fresh-cut": "echarts@5.1.2/theme/dark-fresh-cut.js",
            "dark-mushroom": "echarts@5.1.2/theme/dark-mushroom.js",
            "eduardo": "echarts@5.1.2/theme/eduardo.js",
            "forest": "echarts@5.1.2/theme/forest.js",
            "fresh-cut": "echarts@5.1.2/theme/fresh-cut.js",
            "fruit": "echarts@5.1.2/theme/fruit.js",
            "gray": "echarts@5.1.2/theme/gray.js",
            "green": "echarts@5.1.2/theme/green.js",
            "helianthus": "echarts@5.1.2/theme/helianthus.js",
            "infographic": "echarts@5.1.2/theme/infographic.js",
            "inspired": "echarts@5.1.2/theme/inspired.js",
            "jazz": "echarts@5.1.2/theme/jazz.js",
            "london": "echarts@5.1.2/theme/london.js",
            "macarons": "echarts@5.1.2/theme/macarons.js",
            "macarons2": "echarts@5.1.2/theme/macarons2.js",
            "mint": "echarts@5.1.2/theme/mint.js",
            "red": "echarts@5.1.2/theme/red.js",
            "red-velvet": "echarts@5.1.2/theme/red-velvet.js",
            "roma": "echarts@5.1.2/theme/roma.js",
            "royal": "echarts@5.1.2/theme/royal.js",
            "sakura": "echarts@5.1.2/theme/sakura.js",
            "shine": "echarts@5.1.2/theme/shine.js",
            "tech-blue": "echarts@5.1.2/theme/tech-blue.js",
            "vintage": "echarts@5.1.2/theme/vintage.js"
        },
        'exports': {}
    }

    data = Dict(String, Any)

    renderer = Enum("canvas", "svg")

    theme = Enum("default", "light", "dark","azul", "bee-inspired", "blue", "caravan", "carp", "cool", "dark-blue", "dark-bold", "dark-digerati", "dark-fresh-cut", "dark-mushroom", "eduardo", "forest", "fresh-cut", "fruit", "gray", "green", "helianthus", "infographic", "inspired", "jazz", "london", "macarons", "macarons2", "mint", "red", "red-velvet", "roma", "royal", "sakura", "shine", "tech-blue", "vintage")
