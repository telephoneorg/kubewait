"""
kubewait.cli
~~~~~~~~~~~~~~

CLI App for KubeWait.

:copyright: (c) 2016 by Joe Black.
:license: Apache2.
"""

import os
import sys

from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
from cement.ext.ext_logging import LoggingLogHandler

from pyrkube import KubeAPIClient, KubeApps


class KubeWaitLogHandler(LoggingLogHandler):
    class Meta(LoggingLogHandler.Meta):
        label = 'kwlogging'
        console_format = (
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        debug_format = console_format

    def debug(self, msg, *args, **kwargs):
        self.backend.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.backend.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.backend.warning(msg, *args, **kwargs)

    warn = warning

    def error(self, msg, *args, **kwargs):
        self.backend.error(msg, *args, **kwargs)

    def fatal(self, msg, *args, **kwargs):
        self.backend.fatal(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        self.backend.exception(msg, *args, **kwargs)


class KubeWaitController(CementBaseController):
    class Meta:
        label = 'base'
        arguments = [
            (['requirements'],
             dict(help='kubernetes apps to wait on',
                  action='store',
                  nargs='+'))
        ]

    @expose(hide=True)
    def default(self):
        self.app.log.info('Starting kubewait ...')
        self.app.log.debug('Got arguments: %s', self.app.pargs)

        config = self.app.config.get_section_dict('kubewait')
        self.app.log.debug('Using configuration: %s', config)

        api = KubeAPIClient(config['environment'],
                            config['namespace'],
                            config['domain'])
        self.app.log.info('Got kubernetes API client: %s', api)

        kapps = KubeApps(api,
                         self.app.pargs.requirements,
                         self.app.log.backend.name,
                         config['sleep_interval'])

        self.app.log.info('Got KubeApps instance: %s', kapps)

        kapps.wait()


class KubeWaitApp(CementApp):
    class Meta:
        label = 'kubewait'
        description = 'Pauses container init until kube services are ready.'
        base_controller = KubeWaitController
        log_handler = KubeWaitLogHandler
        config_defaults = {
            'kubewait': dict(
                environment=os.getenv('ENVIRONMENT', 'production'),
                namespace=os.getenv('NAMESPACE', 'default'),
                domain=os.getenv('DOMAIN', 'cluster.local'),
                sleep_interval=int(os.getenv('SLEEP_INTERVAL', 5))
            ),
            'log.kwlogging': dict(
                level=os.getenv('LOG_LEVEL', 'INFO')
            )
        }


def main(args=None):
    args = args or sys.argv[1:]
    with KubeWaitApp(argv=args) as app:
        app.run()


if __name__ == '__main__':
    main()
