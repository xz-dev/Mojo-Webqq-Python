import sys
from . import data_handle

__all__ = ['data_handle', ]

if '__main__' in sys.modules:
    sys.modules['__mp_main__'] = sys.modules['__main__']
