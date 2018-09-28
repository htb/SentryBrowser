# -*- coding: utf-8 -*-

from .dateutils import toDate, prettyDate


class LogEntry(object):

  _log_format = "%-19s | %-15s | %-11s | %s"
  _error_format = "%2s ==> Error: %s"

  def __init__(self, json):
    self.json = json
    self.category  = json.get('category')
    self.date      = toDate(json.get('timestamp'))
    self.message   = json.get('message')
    self.logger    = None
    self.level     = None
    self.file      = None
    self.function  = None
    self.line      = None
    self.column    = None
    self.error     = None

    data_json = json.get('data')
    if data_json:
      self.logger   = data_json.get('logger')
      self.level    = data_json.get('level')
      self.file     = data_json.get('file')
      self.function = data_json.get('function')
      self.line     = data_json.get('line')
      self.column   = data_json.get('column')
      self.error    = data_json.get('error')


  def print_line(self, level = None):
    if not level or compareLevelStrings(self.level, level) >= 0:
      print LogEntry._log_format % (prettyDate(self.date), self.logger, self.level, self.message)
      if self.error:
        print LogEntry._error_format % ("", self.error)


#region Level functions

def _levelNumber(text):
  levels = ["trace", "debug", "verbose", "info", "status", "warning", "error", "critical", "code"]
  try:
    return levels.index(text.lower())
  except:
    return -1

def compareLevelStrings(a, b):
  aVal = _levelNumber(a)
  bVal = _levelNumber(b)
  if aVal == bVal: return 0
  if aVal < bVal: return -1
  return 1

#endregion Level functions
