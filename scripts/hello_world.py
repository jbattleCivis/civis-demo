import sys
import os

print("Hello world")
print("Hello " + os.environ['name'])
print("Your script can use the API key " + os.environ['CIVIS_API_KEY'])
