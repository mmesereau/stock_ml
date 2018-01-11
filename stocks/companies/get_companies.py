from datapackage import Package

def companies():
    package = Package('http://datahub.io/core/s-and-p-500-companies/datapackage.json')
    resources = package.descriptor['resources']
    resourceList = [resources[x]['name'] for x in range(0, len(resources))]
    data = package.resources[1].read()
    return data
