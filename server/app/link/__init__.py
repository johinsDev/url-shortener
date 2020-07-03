from .resource import LinkResource
from .resource_stats import LinkStatsResource
from .validation_schema import CreateLinkValidationSchema


def routes(api):
    api.add_resource(LinkResource, '/links')
    api.add_resource(LinkStatsResource, '/stats')
