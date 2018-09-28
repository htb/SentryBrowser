# -*- coding: utf-8 -*-

from .dateutils import toDate, prettyDate


class Issue(object):

  def __init__(self, json):
    self.json          = json
    self.id            = json.get('id')
    self.title         = json.get('title')
    self.level         = json.get('level')
    self.first_seen    = toDate(json.get('firstSeen'))
    self.last_seen     = toDate(json.get('lastSeen'))
    self.event_count   = int(json.get('count') or "0")
    self.user_count    = int(json.get('userCount') or "0")
    self.link          = json.get('permalink')


  def print_line(self):
    print "[%10s] %19s | %4d e | %4d u | %s" %\
          (self.id, prettyDate(self.last_seen), self.event_count, self.user_count, self.title)

  def print_info(self):
    print "ID         : %s" % self.id
    print "Title      : %s" % self.title
    print "Level      : %s" % self.level
    print "#events    : %s" % self.event_count
    print "#users     : %s" % self.user_count
    print "First seen : %s" % prettyDate(self.first_seen)
    print "Last seen  : %s" % prettyDate(self.last_seen)
    print "Link       : %s" % self.link
