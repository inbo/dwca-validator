# -*- coding: utf-8 -*-
"""
@author: stijn_vanhoey
"""


import json
import yaml
import requests

from pywhip import whip_dwca, whip_csv


# -------
# EXAMPLE
# -------

with open("example_dwc_occurrence.yaml") as schema_file:
    specifications = yaml.load(schema_file)

example = whip_csv("example_dwc_occurrence_draft.tsv",
                   specifications, delimiter='\t')

with open("report_example.html", "w") as index_page:
    index_page.write(example.get_report('html'))

with open('report_example.json', 'w') as json_report:
    json.dump(example.get_report(), json_report, indent=4,
              sort_keys=True, ensure_ascii=False)

# -------
# SALTABEL
# -------

# saltabel_yaml = 'https://raw.githubusercontent.com/inbo/data-publication/' \
#                 'master/datasets/saltabel-occurrences/specification/' \
#                 'dwc_occurrence.yaml'
#
# # read from URL
# response = requests.get(saltabel_yaml)
# saltabel_schema = response.text
# saltabel_specifications = yaml.load(saltabel_schema)
#
# saltabel = whip_dwca('draft/dwca-saltabel-occurrences-v5.2.zip',
#                      saltabel_specifications, 50)
#
# with open("report_saltabel.html", "w") as index_page:
#     index_page.write(saltabel.get_report('html'))
#
# with open('report_saltabel.json', 'w') as outfile:
#     json.dump(saltabel.get_report(), outfile, indent=4,
#               sort_keys=True, ensure_ascii=False)

# -------
# NATUURPUNT
# -------

# PLANT EXOTEN

# natuurpunt_yaml = 'https://raw.githubusercontent.com/inbo/' \
#                   'data-publication-natuurpunt/master/datasets/' \
#                   'planten-exoten-natuurpunt-occurrences/specification/' \
#                   'dwc-occurrence.yaml' \
#                   '?token=AAuErr-v15hsoXp304MZ_fafcKJQn3gdks5bepc5wA%3D%3D'
#
# # read from URL
# response = requests.get(natuurpunt_yaml)
# natuurpunt_schema = response.text
#
# natuurpunt = Whip(natuurpunt_schema)
# #natuurpunt.whip_dwca('dwca-planten-exoten-natuurpunt-occurrences-v1.1.zip')
#
# natuurpunt.whip_csv('dwca-planten-exoten-natuurpunt-occurrences-v1.1/test.tsv',
#                       delimiter='\t')
#
# print(natuurpunt.errors)
# print(natuurpunt.list_error_types())


# DIER EXOTEN - according to guidelines...

# natuurpunt_dieren = 'https://raw.githubusercontent.com/inbo/' \
#                     'data-publication-natuurpunt/master/datasets/' \
#                     'dieren-exoten-natuurpunt-occurrences/specification/' \
#                     'dwc-occurrence.yaml?' \
#                     'token=AAuErtLue61UnIz5kbsrDI_RDSvJ3HBrks5beuA-wA%3D%3D'
#
# response = requests.get(natuurpunt_dieren)
# natuurpunt_schema = response.text
#
# natuurpunt = Whip(natuurpunt_schema)
# natuurpunt.whip_dwca('dwca-dieren-exoten-natuurpunt-occurrences-v1.1.zip')
#
# #natuurpunt.screen_dwc('dwca-planten-exoten-natuurpunt-occurrences-v1.1/test.tsv',
# #                      delimiter='\t')
#
# print(natuurpunt.errors)
# print(natuurpunt.list_error_types())
