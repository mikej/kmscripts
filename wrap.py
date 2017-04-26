#!/usr/bin/env python

import sys
import textwrap

wrapper = textwrap.TextWrapper(width = 72, replace_whitespace = False)

text = sys.stdin.readlines()
wrapped_lines = [wrapper.fill(line) for line in text]

# sys.stdout.write("\n".join(wrapped)

print "\n".join(wrapped_lines)
