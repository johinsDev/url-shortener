from .resource import LinkResource


def routes(api):
    api.add_resource(LinkResource, '/link')
