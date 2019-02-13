from oldp.apps.nlp.ner.strategies.dates import DatesExtractionStrategy
from oldp.apps.nlp.tests.ner.strategies.base import BaseTestCase


class DatesExtractionStrategyTestCase(BaseTestCase.Strategy):
    strategy = DatesExtractionStrategy()
    lang = 'de'
    text = 'Mit der Verordnung (EU) 2015/123 des Rates vom 29. Januar 2015 zur Änderung der Verordnung Nr. ' \
           '208/2014 (ABl. 2015, L 99, S. 1) wurde diese entsprechend dem Beschluss am 1.3.2015 2015/123 geändert.'
    matches = ['29. Januar 2015', '1.3.2015']
    entities = ['2015-01-29', '2015-03-01']

    def test_regexp(self):
        self.assert_equal_regexp_matches(self.strategy.regex_obj(), self.text,
                                         self.matches)

    def test_extract_and_normalize_dates(self):
        ents = self.extract_entities(self.strategy, self.text, self.lang)
        self.assert_equal_entity_values(ents, self.entities)
