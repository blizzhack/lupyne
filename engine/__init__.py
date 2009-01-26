"""
Pythonic wrapper around `Lucene <http://lucene.apache.org/java/docs/index.html>`_ search engine.

Provides high-level interfaces to indexes and documents,
abstracting away java lucene primitives.
"""

import warnings
import lucene

if lucene.getVMEnv() is None:
    warnings.warn("lucene.initVM(lucene.CLASSPATH,... ) must be called before using lucene.", RuntimeWarning, stacklevel=2)

from queries import Query
from documents import Document, Field, NestedField, PrefixField
from indexers import Indexer, IndexSearcher