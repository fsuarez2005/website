#!/usr/bin/env zsh

# start lighttpd for this project

LIGHTTPDEXE="/opt/homebrew/bin/lighttpd"

CONF="etc/lighttpd/lighttpd.conf"

echo "Running $LIGHTTPDEXE using $CONF ..."
"$LIGHTTPDEXE" -D -f "$CONF"

