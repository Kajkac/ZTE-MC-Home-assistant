#!/bin/bash

current_version=$1

# Perform version bump logic here. This example increments the patch version.
IFS='.' read -ra version_parts <<< "$current_version"
major="${version_parts[0]}"
minor="${version_parts[1]}"
patch="${version_parts[2]}"
new_version="$major.$minor.$patch"

echo "$new_version" > VERSION
echo "$new_version"
