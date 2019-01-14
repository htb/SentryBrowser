# Sentry browser

This is simple script for browsing some information from a Sentyry server.

(See http://sentry.io for information about Sentry.)

## Installation

    pip install sentry_browser

## Usage

    sentry help

... then take it from there.

## Configuration

Organization, Project and Auth Token must be specified as input to the script.
It is also possible to set these as environment variables or configure them in the
file `~/.sentryclirc` that is used by `sentry-cli` (another program).

A special note on the log level is that the levels we use for breadcrumb log listing
does not necessarily conform to sentry log level names. We just use this as default.

### Config file (~/.sentryclirc)

    [auth]
    token = mytoken
    [defaults]
    org = myorg
    project = myproject
    [log]
    level = debug

### Environment variables

    SENTRY_ORG
    SENTRY_PROJECT
    SENTRY_AUTH_TOKEN 
    SENTRY_LOG_LEVEL
    
Environment variables have presedence over config file entries.

## Getting an auth token with sentry-cli

sentry-cli is not necessary to use this script, but it can be used to obtain
an authorization token. To get an auth token, call

    sentry-cli login

Documentation and installation instructions for sentry-cli:

https://github.com/getsentry/sentry-cli 


## `sentry log <entryID`

This lists logs collected as 'breadcrumbs' in Sentry.
The format of these logs are particular to one of my projects.
You can use the same for your project if you submit special breadcrumbs
with category `LOG` and the following special information in addition
to the standard fields:

    "category": "LOG",
    "data": {
        "logger"   : "myLoggerName",
        "level"    : "myLoglevel",
        "file"     : "myOptionalFilename",
        "function" : "myOptionalFunction()",
        "line"     : "myOptionalLineNumber",
        "column"   : "myOptionalColumnNumber"
    }
