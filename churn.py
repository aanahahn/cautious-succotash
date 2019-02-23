"""
Identify the customers who have churned.  Is there a relationship between churn and whether a partner was involved in bringing the customer to the vendor, or the region in which the customer operates, or the size or length of the contracts the customer has signed with the vendor? 

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

#lst = group_APAC['accountID']
#lst = group_Africa['accountID']
#lst = group_EMEA['accountID']
#lst = group_LatinAmerica['accountID']
lst = group_NorthAmerica['accountID']

result = []
for an_item in lst:
	look = pd.value_counts(contracts['contractID'].str.contains(an_item))
	if look[True] <= 1: result.append(an_item)


temporary = pd.DataFrame()

for another_item in result:
	accounts_index = accounts.accountID.str.contains(another_item)
	found_indices = accounts[accounts_index]
	temporary = temporary.append(found_indices)

print(temporary['partnerInvolved'].value_counts())
# # For APAC:
# # No     121 59% out of 204 total
# # Yes     83 41%

# # For Africa:
# # Yes    34
# # No     28

# # For EMEA:
# # No     278
# # Yes     86

# # For Latin America:
# # No     56
# # Yes    34

# # For North America:
# # No     262
# # Yes     87



temporary = pd.DataFrame()
for another_item in result:
	contracts_index = contracts['contractID'].str.contains('DKU-'+an_item)
	found_indices = contracts[contracts_index]
	temporary = temporary.append(found_indices)

print(temporary.contractSize.describe())
# # For APAC:
# # count    408.000000
# # mean     242.500000
# # std       22.527624
# # min      220.000000
# # 25%      220.000000
# # 50%      242.500000
# # 75%      265.000000
# # max      265.000000
# # Name: contractSize, dtype: float64

# # For Africa:
# # count    186.000000
# # mean     252.666667
# # std       81.682885
# # min      145.000000
# # 25%      145.000000
# # 50%      271.000000
# # 75%      342.000000
# # max      342.000000
# # Name: contractSize, dtype: float64

# # For EMEA:
# # count    728.000000
# # mean     215.000000
# # std       15.010313
# # min      200.000000
# # 25%      200.000000
# # 50%      215.000000
# # 75%      230.000000
# # max      230.000000
# # Name: contractSize, dtype: float64

# # For Latin America:
# # count     90.0
# # mean     165.0
# # std        0.0
# # min      165.0
# # 25%      165.0
# # 50%      165.0
# # 75%      165.0
# # max      165.0
# # Name: contractSize, dtype: float64

# # For North America:
# # count    1047.000000
# # mean      122.333333
# # std        31.387309
# # min        80.000000
# # 25%        80.000000
# # 50%       132.000000
# # 75%       155.000000
# # max       155.000000
# # Name: contractSize, dtype: float64

print(temporary.contractLength.describe())
# # For APAC:
# # count    408.000000
# # mean       2.000000
# # std        1.001228
# # min        1.000000
# # 25%        1.000000
# # 50%        2.000000
# # 75%        3.000000
# # max        3.000000
# # Name: contractLength, dtype: float64
# # contracts appear to be longer. 

# # For Africa:
# # count    186.000000
# # mean       1.666667
# # std        0.945354
# # min        1.000000
# # 25%        1.000000
# # 50%        1.000000
# # 75%        3.000000
# # max        3.000000
# # Name: contractLength, dtype: float64

# # For EMEA:
# # count    728.0
# # mean       3.0
# # std        0.0
# # min        3.0
# # 25%        3.0
# # 50%        3.0
# # 75%        3.0
# # max        3.0
# # Name: contractLength, dtype: float64

# # For Latin America:
# # count    90.0
# # mean      3.0
# # std       0.0
# # min       3.0
# # 25%       3.0
# # 50%       3.0
# # 75%       3.0
# # max       3.0
# # Name: contractLength, dtype: float64

# # For North America:
# # count    1047.000000
# # mean        1.666667
# # std         0.943260
# # min         1.000000
# # 25%         1.000000
# # 50%         1.000000
# # 75%         3.000000
# # max         3.000000
# # Name: contractLength, dtype: float64