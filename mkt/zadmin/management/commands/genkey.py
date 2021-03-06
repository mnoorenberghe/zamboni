import os
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from lib.crypto import generate_key


class Command(BaseCommand):
    help = 'Generate a randomized encryption encryption key'
    option_list = BaseCommand.option_list + (
        make_option('--dest', action='store',
                    help='Location for key file. Default: %default',
                    default='./encryption.key'),
        make_option('--length', action='store', type=int,
                    help='Key length in bytes. Default: %default',
                    default=128),
    )

    def handle(self, *args, **options):
        if os.path.exists(options['dest']):
            raise CommandError('Key file already exists at %s; remove it '
                               'first or specify a new path with --dest'
                               % options['dest'])
        with open(options['dest'], 'wb') as fp:
            fp.write(generate_key(options['length']))
        os.chmod(options['dest'], 0600)
        print 'Wrote in-app payment key: %s' % options['dest']
