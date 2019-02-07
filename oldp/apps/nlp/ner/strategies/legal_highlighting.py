import re

from oldp.apps.nlp.ner.strategies.base import RegexStrategy
from oldp.apps.nlp.ner.strategies.money import GermanEuroExtractionStrategy, normalize_money_amount


class GermanStakeholderExtractionStrategy(RegexStrategy):

    def regex_obj(self):
        return re.compile(r'(?:\b)(?P<stakeholder>Kläger(in|s)?|Beklagte[rn]?)(?:\b)')


class GermanActionExtractionStrategy(RegexStrategy):

    def regex_obj(self):
        return re.compile(r'(?:\b)(?P<action>tun|unterlassen|dulden)(?:\b)', re.IGNORECASE)


class GermanMatterInDisputeExtractionStrategy(RegexStrategy):

    def regex_obj(self):
        return re.compile(r'(?:\b)(?P<matter_in_dispute>Streitgegenst[aä]nde?)(?:\b)')


class GermanAmountInDisputeExtractionStrategy(RegexStrategy):
    AMOUNT_IN_DISPUTE = r'Streitwert'
    MONEY = GermanEuroExtractionStrategy.MONEY_AMOUNT
    CURRENCY = GermanEuroExtractionStrategy.EUROS
    MONEY_GROUP = 'amount'

    def regex_obj(self):
        return re.compile(
            r'(?:\b)(?P<amount_in_dispute>{amount_in_dispute})(?:.*)(?P<{money_group}>{money_value})(?: ?{currency})'
                .format(amount_in_dispute=self.AMOUNT_IN_DISPUTE,
                        money_group=self.MONEY_GROUP,
                        money_value=self.MONEY,
                        currency=self.CURRENCY)
        )

    def normalize(self, groups: dict, full_match: str):
        """Returns the amount in euros as Decimal."""
        return normalize_money_amount(groups[self.MONEY_GROUP])


class GermanRulingTypeExtractionStrategy(RegexStrategy):

    def regex_obj(self):
        return re.compile(r'(?:\b)(?P<ruling_type>Urteil|Gerichtsbescheid|Beschluss)(?:\b)')
