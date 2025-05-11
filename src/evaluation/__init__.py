# FILE: /Eval-VLM-Image-Desc/src/evaluation/__init__.py

from .clipscore import Clipscore
from .vqascore import VQAscore

__all__ = ['Clipscore', 'VQAscore']