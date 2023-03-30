#!/bin/bash
# send a request to URL with curl, displays size of the body of the response
curl  "$1" | wc
