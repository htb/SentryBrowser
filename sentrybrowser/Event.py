# -*- coding: utf-8 -*-

from .dateutils import toDate, prettyDate
from .LogEntry import LogEntry


class Event(object):

  def __init__(self, json):
    self.json            = json
    self.id              = json.get('eventID')
    self.message         = json.get('message')
    self.date            = toDate(json.get('dateCreated'))
    self.device_model    = None
    self.os_name         = None
    self.os_version      = None
    self.app_bundleID    = None
    self.app_version     = None
    self.app_build       = None
    self.device_app_hash = None
    self.user_id         = None

    contexts_json = json.get('contexts')
    if contexts_json:
      device_json = contexts_json.get('device')
      if device_json:
        self.device_model = device_json.get('model')
      os_json = contexts_json.get('os')
      if os_json:
        self.os_name = os_json.get('name')
        self.os_version = os_json.get('version')
      app_json = contexts_json.get('app')
      if app_json:
        self.app_bundleID = app_json.get('app_identifier')
        self.app_version = app_json.get('app_version')
        self.app_build = app_json.get('app_build')
        self.device_app_hash = app_json.get('device_app_hash')

    user_json = json.get('user')
    if user_json:
      self.user_id = user_json.get('id')

    # Logs
    self.log_entries = []
    for entry_json in json.get('entries'):
      if entry_json.get('type') == 'breadcrumbs':
        breadcrumbs_json = (entry_json.get('data') or {}).get('values') or {}
        for breadcrumb_json in breadcrumbs_json:
          if breadcrumb_json.get('category') == "LOG":
            log_entry = LogEntry(breadcrumb_json)
            if log_entry: self.log_entries.append(log_entry)


  def print_line(self):
    print "[%32s] %19s | %s" % (self.id, prettyDate(self.date), self.message)

  def print_info(self):
    print "ID       : %s" % self.id
    print "Date     : %s" % prettyDate(self.date)
    print "Message  : %s" % self.message
    print "device   : %s" % self.device_model
    print "os       : %s %s" % (self.os_name, self.os_version)
    print "BundleID : %s" % self.app_bundleID
    print "Version  : %s (%s)" % (self.app_version, self.app_build)
    print "UserID   : %s" % (self.user_id or "(missing)")
    print "Hash     : %s" % (self.device_app_hash or "(missing)")

  def print_log(self, loglevel = None):
    for entry in self.log_entries:
      entry.print_line(loglevel)
