# -*- coding: utf-8 -*-


__version__ = "0.0.3"
__author__  = "Hans Terje Bakke"

from .dateutils import toDate, prettyDate

__all__ = [
  'toDate', 'prettyDate'
 ]


#region Encoding of stdin/stdout

import sys, codecs

# Fix stdin and stdout encoding issues
_encoding_stdin  = sys.stdin.encoding or "UTF-8"
_encoding_stdout = sys.stdout.encoding or _encoding_stdin
#sys.stdin = codecs.getreader(_encoding_stdin)(sys.stdin)
sys.stdout = codecs.getwriter(_encoding_stdout)(sys.stdout)

#endregion Encoding of stdin/stdout
