from django.db import models

from oldp.apps.lib.markers import BaseMarker


class Entity(models.Model, BaseMarker):
    MONEY = "MONEY"
    EURO = "EURO"
    DATE = "DATE"
    PERSON = "PERSON"
    LOCATION = "LOCATION"
    ORGANIZATION = "ORGANIZATION"
    PERCENT = "PERCENT"
    LEGAL_STAKEHOLDER = "L_STKHOLDER"
    LEGAL_ACTION = "L_ACTION"
    LEGAL_MATTER_IN_DISPUTE = "L_MATTER_I_D"
    LEGAL_AMOUNT_IN_DISPUTE = "L_AMOUNT_I_D"
    LEGAL_RULING_TYPE = "L_RULING"

    TYPES = (
        (MONEY, "Monetary values with currency."),
        (EURO, "Euro amounts."),
        (DATE, "Calendar dates."),
        (PERSON, "Name of a person or family."),
        (LOCATION, "Name of geographical or political locations."),
        (ORGANIZATION, "Any organizational entity."),
        (PERCENT, "Percentage amounts."),
        (LEGAL_STAKEHOLDER, ""),
        (LEGAL_ACTION, ""),
        (LEGAL_MATTER_IN_DISPUTE, ""),
        (LEGAL_AMOUNT_IN_DISPUTE, ""),
        (LEGAL_RULING_TYPE, ""),
    )
    type = models.CharField(
        help_text='Entity type',
        max_length=12,
        choices=TYPES,
        )
    value = models.TextField(
        help_text='Content that represents the entity'
    )
    value_float = models.FloatField(
        help_text='Content as number that represents the entity (for e.g. money)',
        default=0,
    )
    pos_start = models.IntegerField(
        help_text='Start position of entity in content',
        null=True
    )
    pos_end = models.IntegerField(
        null=True,
        help_text='End position of entity in content',
    )

    def get_start_position(self) -> int:
        return self.pos_start

    def get_end_position(self) -> int:
        return self.pos_end

    def get_marker_open_format(self) -> str:
        return '<span class="entity entity-{type} entity-off" id="entity{id}" data-value="{value}">'

    def get_marker_close_format(self) -> str:
        return '</span>'

    def __str__(self):
        return self.value

    def __repr__(self):
        return '<Entity({}: {}; {}-{})>'.format(self.type, self.value, self.pos_start, self.pos_end)


class NLPContent(models.Model):
    nlp_entities = models.ManyToManyField(Entity, blank=True)

    class Meta:
        abstract = True

    @staticmethod
    def get_entity_types():
        return [Entity.ORGANIZATION, Entity.DATE, Entity.MONEY, Entity.PERSON, Entity.LOCATION,
                Entity.LEGAL_STAKEHOLDER, Entity.LEGAL_ACTION, Entity.LEGAL_MATTER_IN_DISPUTE,
                Entity.LEGAL_AMOUNT_IN_DISPUTE, Entity.LEGAL_RULING_TYPE]
