# cautious-succotash
Data analysis example using Pandas and Python

The use case in this fictional example is a B2B vendor with two data sources:
A customer accounts (file attached) data source that has a row for each customer of the vendor, and columns for:
  the unique ID assigned to each customer,
  the region in which the customer operates, and
  whether a vendor partner was involved in bringing the customer in

A contracts (file attached) data source that has a row for each deal closed by the vendor, and columns for:
  the date on which each deal was closed,
  the size of each deal (in thousands ARR),
  the length of each deal (in years),
  the unique ID assigned to each deal, and
  the date on which payment was received

If payment has not been received within 45 days of the close of a deal, the vendor sends a reminder to the customer.  By region, what is the current (where "today" is December 11, 2018) total value of contracts to be collected that are more than 45 days past close?  More than 90 days?  More than 135 days?  How does this compare to contracts closed in 2017?

Identify the customers who have churned.  Is there a relationship between churn and whether a partner was involved in bringing the customer to the vendor, or the region in which the customer operates, or the size or length of the contracts the customer has signed with the vendor? 
