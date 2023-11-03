import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import piiscan

original_value = """
{
    "name": "John Doe",
    "email": "john@doe.com",
    "address": "123 Front Street, San Francisco, CA",
    "phone": "+1 (415) 123-4567"
}
"""

pii_detected = piiscan.scan(original_value)

annotated = piiscan.annotate(original_value, pii_detected)

print(annotated)
