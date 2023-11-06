# piiscan

[![PyPI version](https://badge.fury.io/py/piiscan.svg)](https://badge.fury.io/py/piiscan)

A simple Python library that detects PII in text. Optimized for network traffic and structured data (e.g. JSON Objects, HTTP Requests).

Powered by [`beki/en_spacy_pii_fast`](https://huggingface.co/beki/en_spacy_pii_fast) and [Microsoft Presidio](https://microsoft.github.io/presidio/).

## Installation

This package is published on PyPi, and can be installed using `pip`.

```
pip3 install piiscan
```

## Usage

The module exposes two methods:
- `scan()` returns a `list` of Presidio [`RecognizerResult`](https://microsoft.github.io/presidio/api/analyzer_python/#presidio_analyzer.RecognizerResult) objects.
- `annotate()` returns a human-readable `list` of all fields detected and the corresponding entity type.

### Scanning structured data for PII

```python
import piiscan

original_value = '''
{
    "name": "John Doe",
    "email": "john@doe.com",
    "address": "123 Front Street, San Francisco, CA",
    "phone": "+1 (415) 123-4567"
}
'''

detected_pii = piiscan.scan(original_value)

print(detected_pii)

```

Expected result printed in console:

```
[
    type: EMAIL_ADDRESS, start: 41, end: 53, score: 1.0, 
    type: PERSON, start: 16, end: 24, score: 0.85, 
    type: LOCATION, start: 72, end: 107, score: 0.85, 
    type: URL, start: 46, end: 53, score: 0.5, 
    type: PHONE_NUMBER, start: 127, end: 141, score: 0.4
]
```

### Annotating data to display discovered PII

```python
import piiscan

original_value = '''
{
    "name": "John Doe",
    "email": "john@doe.com",
    "address": "123 Front Street, San Francisco, CA",
    "phone": "+1 (415) 123-4567"
}
'''

detected_pii = piiscan.scan(original_value)

annotated = piiscan.annotate(original_value, detected_pii)

print(annotated)

```

Expected result printed in console (cleaned for readability):

```
{  
    "name": "('John Doe', 'PERSON')",  
    "email": "('john@doe.com', 'EMAIL_ADDRESS'), ('doe.com', 'URL')",   
    "address": "('123 Front Street, San Francisco, CA', 'LOCATION')", 
    "phone": "('+1 (415) 123-4567', 'PHONE_NUMBER')"
}
```

## Credits

The basis for this project is derived from [Pixie Labs' blog post](https://blog.px.dev/detect-pii/) on using NLP to anonymize sensitive PII in structured data, and its corresponding [Hugging Face Space](https://huggingface.co/spaces/beki/pii-anonymizer).

This project uses [Benjamin Kilimnik](https://kilimnik.org/)'s [`en_spacy_pii_fast`](https://huggingface.co/beki/en_spacy_pii_fast) spaCy model for NER. It is trained using a [dataset](https://huggingface.co/datasets/beki/privy) derived from Privy's synthetic payload generator. The entire model is less than 7 MiB!

This library was designed for use in resource-constrained environments, hence the small 7 MiB `en_spacy_pii_fast` model. However, if you would like increased accuracy there are other alternatives described in the [original blog post](https://blog.px.dev/detect-pii/).

This library also makes use of [Microsoft Presidio](https://microsoft.github.io/presidio/) and [spaCy](https://spacy.io/).
