#!/usr/bin/env python

import os
import sys

# Set up the basic HTML structure
html_str = """
<!DOCTYPE html>
<html>
  <head>
    <style>
      body {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
      }
      .flash {
        animation: flash 1s infinite;
      }
      @keyframes flash {
        50% {
          color: transparent;
        }
      }
      .heart {
        font-size: 3em;
        color: red;
      }
    </style>
  </head>
  <body>
    <div>
      <span class="heart">❤</span>
      <span class="flash">Jeg liker DIG Caroline</span>
      <span class="heart">❤</span>
    </div>
  </body>
</html>
"""

# Create the HTML file
html_file = open('index.html', 'w')
html_file.write(html_str)
html_file.close()

print('Website generated successfully!')
