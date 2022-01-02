import sys

if sys.version_info < (3, 7):
    from ._marker import Marker
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(__name__, [], ["._marker.Marker"])
