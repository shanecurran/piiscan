import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import piiscan

piiscan.scan("Hello world! My name is John Doe and my email is john@doe.com.")
