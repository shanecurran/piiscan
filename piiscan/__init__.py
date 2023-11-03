from piiscan.spacy_recognizer import CustomSpacyRecognizer
from presidio_analyzer.nlp_engine import NlpEngineProvider
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry

# Helper methods
def analyzer_engine():
    """Return AnalyzerEngine."""

    spacy_recognizer = CustomSpacyRecognizer()
    configuration = {
        "nlp_engine_name": "spacy",
        "models": [{"lang_code": "en", "model_name": "en_spacy_pii_fast"}],
    }

    # Create NLP engine based on configuration
    provider = NlpEngineProvider(nlp_configuration=configuration)
    nlp_engine = provider.create_engine()

    registry = RecognizerRegistry()
    # add rule-based recognizers
    registry.load_predefined_recognizers(nlp_engine=nlp_engine)
    registry.add_recognizer(spacy_recognizer)
    # remove the nlp engine we passed, to use custom label mappings
    registry.remove_recognizer("SpacyRecognizer")

    analyzer = AnalyzerEngine(
        nlp_engine=nlp_engine, registry=registry, supported_languages=["en"]
    )

    return analyzer


def scan(text, language="en", score_threshold=0.35):
    return analyzer_engine().analyze(text, language, score_threshold)
