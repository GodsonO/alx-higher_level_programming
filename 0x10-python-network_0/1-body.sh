#!/bin/bash
# Get the response body for a given URL for 200 status code responses.
curl -sfL "$1" -X GET
