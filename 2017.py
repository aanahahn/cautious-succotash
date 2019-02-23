"""
If payment has not been received within 45 days of the close of a deal, the vendor sends a reminder to the customer.  By region, what is the current (where "today" is December 11, 2018) total value of contracts to be collected that are more than 45 days past close?  More than 90 days?  More than 135 days?  How does this compare to contracts closed in 2017?

Contracts in 2017 by region:
APAC 87399.0
Africa 23178.0
EMEA 166514.0
Latin America 21355.0
North America 151625.0
"""

import pandas as pd
import numpy as np

import datetime
from datetime import datetime, timedelta


contracts = pd.DataFrame(pd.read_csv('contracts.csv'))
accounts = pd.DataFrame(pd.read_csv('accounts.csv'))


contracts['closingDate'] = pd.to_datetime(contracts['closingDate'])
contracts['paymentDate'] = pd.to_datetime(contracts['paymentDate'])



regionGrouped = accounts.groupby(by = 'region')
# print(regionGrouped.size())
# region
# APAC              596
# Africa            190
# EMEA             1031
# Latin America     202
# North America     981
# dtype: int64


group_APAC = regionGrouped.get_group("APAC")
# # # print(group_APAC.head())
   # # # accountID region partnerInvolved
# # # 5     3oy2wf   APAC             Yes
# # # 8     0w3ynj   APAC              No
# # # 11    kt2n1f   APAC              No
# # # 15    ta2z0d   APAC              No
# # # 19    g8rycf   APAC              No

group_Africa = regionGrouped.get_group("Africa")
group_EMEA = regionGrouped.get_group("EMEA")
group_LatinAmerica = regionGrouped.get_group("Latin America")
group_NorthAmerica = regionGrouped.get_group("North America")

lst = group_APAC['accountID']
temporary = pd.DataFrame()
val_Size = 0

year_group = contracts[(pd.to_datetime(contracts['closingDate'])>= pd.to_datetime('2017-01-01')) & (pd.to_datetime(contracts['closingDate'])<= pd.to_datetime('2017-12-31'))]

year_group_diff = (pd.to_datetime(year_group['paymentDate']) - pd.to_datetime(year_group['closingDate'])).dt.days

"""
print(year_group_diff.describe())
count    1433.000000
mean       93.782973
std        19.110154
min        41.000000
25%        80.000000
50%        94.000000
75%       107.000000
max       167.000000
dtype: float64
"""



for an_item in lst:
	contracts_index = year_group['contractID'].str.contains('DKU-'+an_item)
	found_indices = year_group[contracts_index]
	temporary = temporary.append(found_indices)

temporary.paymentDate = temporary.paymentDate.replace('', np.nan)
temp_blankDate = temporary[temporary.paymentDate.isnull()]

val_Size = temporary.contractSize * temporary.contractLength
total_Value = sum(val_Size)
print('APAC', total_Value)


###############################################################

lst = group_Africa['accountID']
temporary = pd.DataFrame()
val_Size = 0


for an_item in lst:
	contracts_index = year_group['contractID'].str.contains('DKU-'+an_item)
	found_indices = year_group[contracts_index]
	temporary = temporary.append(found_indices)

temporary.paymentDate = temporary.paymentDate.replace('', np.nan)
temp_blankDate = temporary[temporary.paymentDate.isnull()]

val_Size = temporary.contractSize * temporary.contractLength
total_Value = sum(val_Size)
print('Africa', total_Value)


###############################################################
lst = group_EMEA['accountID']
temporary = pd.DataFrame()
val_Size = 0

for an_item in lst:
	contracts_index = year_group['contractID'].str.contains('DKU-'+an_item)
	found_indices = year_group[contracts_index]
	temporary = temporary.append(found_indices)

temporary.paymentDate = temporary.paymentDate.replace('', np.nan)
temp_blankDate = temporary[temporary.paymentDate.isnull()]

val_Size = temporary.contractSize * temporary.contractLength
total_Value = sum(val_Size)
print('EMEA', total_Value)

###############################################################

lst = group_LatinAmerica['accountID']
temporary = pd.DataFrame()
val_Size = 0

for an_item in lst:
	contracts_index = year_group['contractID'].str.contains('DKU-'+an_item)
	found_indices = year_group[contracts_index]
	temporary = temporary.append(found_indices)

temporary.paymentDate = temporary.paymentDate.replace('', np.nan)
temp_blankDate = temporary[temporary.paymentDate.isnull()]

val_Size = temporary.contractSize * temporary.contractLength
total_Value = sum(val_Size)
print('Latin America', total_Value)


###############################################################

lst = group_NorthAmerica['accountID']
temporary = pd.DataFrame()

val_Size = 0

for an_item in lst:
	contracts_index = year_group['contractID'].str.contains('DKU-'+an_item)
	found_indices = year_group[contracts_index]
	temporary = temporary.append(found_indices)

temporary.paymentDate = temporary.paymentDate.replace('', np.nan)
temp_blankDate = temporary[temporary.paymentDate.isnull()]

val_Size = temporary.contractSize * temporary.contractLength
total_Value = sum(val_Size)
print('North America', total_Value)
