# -*- coding: utf-8 -*-

name = 'sentrybrowser'

__all__ = ['toDate', 'prettyDate']

import datetime, dateutil.parser


def toDate(text):
  if not text: return None
  try:
    return dateutil.parser.parse(text)
  except:
    return None


def prettyDate(date):
  if not type(date) is datetime.datetime: return None
  try:
    return date.strftime('%Y-%m-%d %H:%M:%S')
  except:
    return None
