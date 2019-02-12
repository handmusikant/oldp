from oldp.apps.nlp.models import Entity, NLPContent
from oldp.apps.nlp.ner.base import HtmlEntityExtractor


class EntityProcessor:  # TODO Can this be all done in ProcessingStep?
    entity_types = []

    def __init__(self):
        super(EntityProcessor, self).__init__()

    def extract_and_load(self,
                         text: str,
                         owner: NLPContent,
                         lang='de'):
        if len(self.entity_types) == 0:
            raise ValueError('No entity types given! Set them via public property entity_types.')

        # Remove existing entities
        owner.nlp_entities.all().delete()

        extractor = HtmlEntityExtractor(lang=lang)
        extractor.prepare(text)

        # Extract for each type
        for entity_type in self.entity_types:
            entities = extractor.extract(entity_type)
            for (value, start, end) in entities:

                # Prepare value
                value_str = str(value).strip()

                # Only add non-empty entities
                if value_str != '':
                    entity = Entity(type=entity_type,
                                    value=value_str,
                                    pos_start=start,
                                    pos_end=end)

                    # Handle binary values
                    if entity_type == Entity.MONEY:
                        currency, dec = value
                        entity.value_float = dec

                    entity.save()
                    owner.nlp_entities.add(entity)
