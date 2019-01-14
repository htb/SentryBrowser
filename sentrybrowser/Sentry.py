# -*- coding: utf-8 -*-

from .Issue import Issue
from .Event import Event
import requests, sys


class Sentry(object):

  url_api           = 'https://sentry.io/api/0'
  url_format_issues = '%s/projects/%s/%s/issues/'
  url_format_events = '%s/issues/%s/events/'
  url_format_event  = '%s/projects/%s/%s/events/%s/'

  def __init__(self, organization, project, auth_token):
    self.organization = organization
    self.project = project
    self._auth_token =  auth_token
    self._headers ={
      'user-agent'    : 'python',
      'Authorization' : 'Bearer %s' % self._auth_token
    }

  def _check_fatal_error(self, r):
    if r.status_code != 200:
      j = r.json()
      if j:
        d = j.get('detail') or '(missing details)'
        sys.stderr.write('ERROR code %d: %s\n' % (r.status_code, d))
      else:
        sys.stderr.write('ERROR code %d\n' % r.status_code)
      sys.exit(1)  # Error

  def _get_issues_json(self):
    url = Sentry.url_format_issues % (Sentry.url_api, self.organization, self.project)
    r = requests.get(url, headers=self._headers)
    self._check_fatal_error(r)
    return r.json()

  def _get_event_json(self, eventID):
    url = Sentry.url_format_event % (Sentry.url_api, self.organization, self.project, eventID)
    r = requests.get(url, headers=self._headers)
    self._check_fatal_error(r)
    return r.json()

  def _get_events_json(self, issueID):
    url = Sentry.url_format_events % (Sentry.url_api, issueID)
    r = requests.get(url, headers=self._headers)
    self._check_fatal_error(r)
    return r.json()

  def get_issues(self):
    issues = []
    jj = self._get_issues_json()
    for j in jj or []:
      issue = Issue(j)
      if issue: issues.append(issue)
    return issues

  def get_events(self, issueID):
    events = []
    jj = self._get_events_json(issueID)
    for j in jj or []:
      event = Event(j)
      if event: events.append(event)
    return events

  def get_event(self, eventID):
    jj = self._get_event_json(eventID)
    return Event(jj) if jj else None


  def print_info(self):
    print "Organization : %s" % (self.organization or "(not set)")
    print "Project      : %s" % (self.project      or "(not set)")
    print "Auth token   : %s" % (self._auth_token  or "(not set)")
    print "Log level    : %s" % (self.loglevel     or "(not set)")
