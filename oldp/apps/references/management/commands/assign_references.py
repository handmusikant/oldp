import json
import logging

from django.core.management import BaseCommand

from oldp.apps.cases.models import Case
from oldp.apps.laws.models import LawBook, Law
from oldp.apps.references.models import LawReference, CaseReference

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Assign references to corresponding database items (laws and cases)'

    def __init__(self):
        super(Command, self).__init__()

    def add_arguments(self, parser):

        parser.add_argument('--type', type=str, default='')

        parser.add_argument('--verbose', action='store_true', default=False)

        parser.add_argument('--override', action='store_true', default=False, help='Reassign all references')
        # parser.add_argument('--empty', action='store_true', default=False, help='Empty existing index')

        parser.add_argument('--limit', type=int, default=0)

    def handle(self, *args, **options):
        if options['verbose']:
            logger.setLevel(logging.DEBUG)

        if options['type'] == '':
            # Use both reference types
            refs = LawReference.objects
            self.assign_refs(refs, 'law', options['limit'], options['override'])

            refs = CaseReference.objects
            self.assign_refs(refs, 'case', options['limit'], options['override'])

        elif options['type'] == 'law':
            refs = LawReference.objects
            self.assign_refs(refs, 'law', options['limit'], options['override'])

        elif options['type'] == 'case':
            refs = CaseReference.objects
            self.assign_refs(refs, 'case', options['limit'], options['override'])

        else:
            raise ValueError('Unsupported ref type: %s' % options['type'])

    def find_case_target(self, ref_source, ref_target, court_hint=None):
        # TODO court hint: same as book hint but with court

        try:
            # Find case based on ECLI
            case = Case.objects.get(ecli=ref_target['ecli'])
            ref_source.case = case
        except Case.DoesNotExist:
            pass

        return ref_source

    def find_law_target(self, ref_source, ref_target, book_hint=None):
        # TODO Handle book_hint: Book hints should be used for references within a law book
        # e.g. BGB 1 refers to § 2 but without naming the references BGB

        try:
            # Determine book first
            book = LawBook.objects.get(code=ref_target['book'])

            # Find law with exact slug match (TODO make it more fuzzy)
            # print('law query: book=%s, slug=%s' % (book, ref_target['sect']))
            law = Law.objects.get(book=book, slug=ref_target['sect'])

            # print('Law found: %s' % law)
            ref_source.law = law

        except LawBook.DoesNotExist:
            pass

        except Law.DoesNotExist:
            pass

        return ref_source


    def assign_refs(self, refs, ref_type, limit=0, override=False):

        logger.info('Assigning refs for: %s' % ref_type)

        if override:
            refs = refs.all()
        else:
            refs = refs.filter(case__isnull=True, law__isnull=True)

        logger.debug('Refs found: %i' % len(refs))

        if limit > 0:
            logger.info('Limit set to: %i' % limit)
            refs = refs[:limit]

        for ref_source in refs:
            # print('-----------------')
            # print(ref.to)
            # print('marker text: %s' % ref.marker.text)
            # print('referenced by: %s' % ref.marker.referenced_by)

            ref_target = json.loads(ref_source.to)

            if 'type' not in ref_target:
                raise ValueError('Cannot handle ref_target: %s' % ref_target)

            if ref_type == 'law' and ref_target['type'] == 'law':
                # From law to law
                ref_source = self.find_law_target(ref_source, ref_target, ref_source.marker.referenced_by.book)  # TODO book hint

            elif ref_type == 'case' and ref_target['type'] == 'case':
                # From case to case
                ref_source = self.find_case_target(ref_source, ref_target, ref_source.marker.referenced_by.court)

            elif ref_type == 'case' and ref_target['type'] == 'law':
                # Case to law
                ref_source = self.find_law_target(ref_source, ref_target, None)  # TODO book hint

            elif ref_type == 'law' and ref_target['type'] == 'case':
                # Law to case
                # raise NotImplementedError('Law->Case reference matching not implemented')
                ref_source = self.find_case_target(ref_source, ref_target, None)

            else:
                # Should never happend
                raise ValueError('Reference type invalid (requested: %s): %s' % (ref_type, ref_target))

            if ref_source.law is not None or ref_source.case is not None:
                ref_source.save()
                logger.debug('Ref saved: %s' % ref_source)
            else:
                logger.debug('Reference cannot be assigned to database item:')
                logger.debug(' - to: %s' % ref_source.to)
                logger.debug(' - marker text: %s' % ref_source.marker.text)
                logger.debug(' - referred by: %s' % ref_source.marker.referenced_by)
                #
                # print('ref not saved')
                pass
                # raise ValueError('Reference cannot be matched: %s' % ref_target)
                # ref.delete()
