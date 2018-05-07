import logging

from django.core.management import BaseCommand
from django.db import models

from oldp.apps.laws.models import LawBook

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Set latest revision of law books'

    def __init__(self):
        super(Command, self).__init__()

    def add_arguments(self, parser):
        # parser.add_argument('type', type=str, help='Content type (case, law, ...)')
        # parser.add_argument('--limit', type=int, default=20)
        parser.add_argument('--empty', action='store_true', default=False, help='Delete existing revisions')
        pass

    def handle(self, *args, **options):
        # Disable latest for all revisions
        LawBook.objects.all().update(latest=False)

        # Fetch latest revision date and update corresponding books
        latest_revisions = LawBook.objects.values('code').annotate(revision_date=models.Max('revision_date')).order_by('code')

        for rev in latest_revisions:
            LawBook.objects.filter(code=rev['code'], revision_date=rev['revision_date']).update(latest=True)
            logger.debug('Set latest for: %s' % rev)

