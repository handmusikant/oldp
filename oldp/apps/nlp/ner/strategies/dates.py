import re
import dateparser

from oldp.apps.nlp.ner.strategies.base import RegexStrategy


class DatesExtractionStrategy(RegexStrategy):

    def regex_obj(self):
        return re.compile(r'\b([0123]?\d\.)?(( (Jan|Feb|Mrz|Mä|Apr|Mai|Jun|Jul|Aug|Sep|Okt|Nov|Dez)[a-z]{0,6}\.? )|([01]?\d\.))([12]\d)?\d{2}\b')

    def normalize(self, groups: dict, full_match: str):
        """Returns the date formatted in ISO."""
        return dateparser.parse(full_match).date().isoformat()
