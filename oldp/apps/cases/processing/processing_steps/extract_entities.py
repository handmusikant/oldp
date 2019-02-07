import logging

from oldp.apps.cases.models import Case
from oldp.apps.cases.processing.processing_steps import CaseProcessingStep
from oldp.apps.nlp.models import Entity
from oldp.apps.processing.processing_steps.extract_entities import EntityProcessor

logger = logging.getLogger(__name__)


class ProcessingStep(CaseProcessingStep, EntityProcessor):
    description = 'Extract entities'
    entity_types = [Entity.MONEY, Entity.LOCATION, Entity.PERSON, Entity.ORGANIZATION, Entity.LEGAL_STAKEHOLDER,
                    Entity.LEGAL_ACTION, Entity.LEGAL_MATTER_IN_DISPUTE, Entity.LEGAL_AMOUNT_IN_DISPUTE,
                    Entity.LEGAL_RULING_TYPE]

    def process(self, case: Case) -> Case:
        self.extract_and_load(case.content, case, lang='de')
        return case
