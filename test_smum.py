
# -*- coding:utf -*-
"""
#Created by Esteban.

Fri 13 Oct 2017 02:05:09 PM CEST

"""
from smum.microsim.table import TableModel

verbose = True
census_file = 'docs/example_ph/data/benchmarks_be_year_bias3_climate.csv'

tm = TableModel(census_file = census_file, verbose = verbose)

tm.add_model('docs/example_ph/data/test_water_be.csv', 'Water')
tm.update_dynamic_model(
    'Water', specific_col = 'ConstructionType', select = 0)
tm.update_dynamic_model(
    'Water', specific_col = 'Age', val = 'mu', compute_average = 0)
tm.update_dynamic_model(
    'Water', specific_col = 'ConstructionYear', val = 'mu')
tm.update_dynamic_model(
    'Water', specific_col = 'HHSize', val = 'mu')
tm.update_dynamic_model(
    'Water', specific_col = 'Income', val = 'mu',
    compute_average = False)

print(tm.models['Water'].loc[2020])
