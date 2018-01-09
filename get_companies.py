from datapackage import Package

def companies():
    package = Package('http://datahub.io/core/s-and-p-500-companies/datapackage.json')
    resources = package.descriptor['resources']
    resourceList = [resources[x]['name'] for x in range(0, len(resources))]
    data = package.resources[1].read()
    company_list = [data[x][0] for x in range(0, len(data))]
    return company_list
