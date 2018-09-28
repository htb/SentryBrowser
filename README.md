# Sentry browser

## Installation

pip install sentry_browser

## Usage

    sentry help

... then take it from there.

## Configuration

Organization, Project and Auth Token must be specified as input to the script.
It is also possible to set these as environment variables or configure them in the
file `~/.sentryclirc` that is used by `sentry-cli` (another program).

A special not on the log level is that the levels we use for breadcrumb log listing
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
