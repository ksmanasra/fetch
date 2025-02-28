# Fetch
Data Analyst Assessment

Repository includes
1. README file, which includes answers to assessment
2. SQL/Python scripts
3. Slack Message


First: Explore the Data
1. Are there any data quality issues present?
    >Yes. Breakdown by dataset:

        Users: It is odd to have a timestamp on the Birth Date, would make more sense for just the date.

        Transactions: There are duplicate records for every receipt ID

        Products: ~1/4th of Manufacturers+Brands are blank, and ~4000 items have missing barcodes (highlighting this as it would be the unique identifier to each product).

2. Are there any fields that are challenging to understand?

    >Yes. Within the Products file, Category_1, Category_2, Category_3, Category_4 can be more specific and "brand" would be better suited if it were called "product_name" or the like. Within the Transactions file, "quantity" and "sale" are vague, "total quantity" and "total sale" would be more fitting.


Second: provide SQL queries (doing this using python+pandas)
1. Closed-ended questions:

    1. What are the top 5 brands by receipts scanned among users 21 and over?
        >Coca-Cola (288), Annie's (264), Dove (256), Barefoot (253), Oribe (231)
    2. What are the top 5 brands by sales among users that have had their account for at least six months?
        >Coca-Cola ($845.62), Annie's ($776.88), Dove ($756.48), Barefoot ($744.51), Oribe ($679.77)
    3. What is the percentage of sales in the Health & Wellness category by generation?
        >Centennial (0%), Silent (0%), Boomer (28.13%), Gen-X (31.60%), Millienial (40.27%), Gen-Z (0%)

        >[Reference to Year Ranges of Generation Groups](https://libguides.usc.edu/busdem/age)

2. Open-ended questions: for these, make assumptions and clearly state them when answering the question.

    1. Who are Fetch’s power users?
        >Defining "power users" as users who scanned the most receipts, it is a more accurate definition for Fetch versus seeing who bought the most items or who has spent them most. We will go with the theme of the previous questions and list the top 5 users.

        >The following output are the top 5 "power users" (there are no names, so we will categorize by the given ID):

            USER_ID                     SCANNED
            62925c1be942f00613f7365e    10
            64e62de5ca929250373e6cf5    10
            64063c8880552327897186a5     9
            604278958fe03212b47e657b     7
            609af341659cf474018831fb     7
    2. Which is the leading brand in the Dips & Salsa category?
        > We can define "leading brand" as simply which ever brand sells the most. So we can check through the quantity of each brand sold throughout the dataset.

        >After analysis, we find that Tostitos was the top ranking Dips & Salsa brand, with a total quantity of 20 items.
    3. At what percent has Fetch grown year over year?
        >Growth can either be defined by user growth over each year, or the amount of receipts scanned year over year. Since Fetch gathers data it needs from scanned receipts, it would be more significant to use the total amount of receipts scanned each year to understand Fetch's growth. Although we run into an issue, all scan dates are within 2024 in the provided data. We can revert back to analyze Fetch's growth through how many users made accounts each year.

        >Year over year, based on new users, Fetch has grown as follows:

            Year     New Users   Percent Growth
            2014         30               -
            2015         51          70.00%
            2016         70          37.25%
            2017        644          82.00%
            2018       2168         236.65%
            2019       7093         227.17%
            2020      16883         138.02%
            2021      19159          13.48%
            2022      26807          39.92%
            2023      15464         -42.31%
            2024      11631         -24.79%

Third: Communicate with stakeholders (Slack)
    
Hello Fellow Fetchers, the analytics team wanted to share an update with you all about some findings we had after an investigation into our data.

Data Quality
1. We have identified key data points, including unique identifiers that were missing which affected our ability to properly perform analysis. A more complete version of the data would give us more accurate insights. An example of this would be the data we store on products, where some barcodes (the unique identifier) are missing.
2. We have also found that there were duplicate records for every scanned receipt that was within our data warehouse. There is a work around for removing duplicate records, however the root cause of the issue needs to be investigated.
3. We seem to have scanned receipts from the year 2024, even when we have users that have signed up well before that year. We can only provide consumer insights limited to one year. To add, with data from previous years, we would be able to give a better understanding of Fetch's growth year over year.

Interesting Trend Regarding Age Demographics
- According to the data, we find that almost all of Fetch's users are within the Boomer (1946 - 1964), Gen-X (1965 - 1979), and Millenial (1980 - 1994) generations. 
- Although, we have virtually no users who are from the "Gen-Z" generation (born 1995-2012) according to the user database. 
- Within that generation are those who are more tech-savvy, so they can use the app with ease. To add, many are already working and spending on products in the market.
- Is there an outreach issue with the younger generation? This would be a great opportunity to discuss how Fetch can tap into a new age demographic. 

Next Steps
1. Clarification on certain data models: Is the data we hold supposed to behave the way they do? How can we better define some of the data models that we have?
2. Data Engineering: Can we determine the root cause of the duplication issue when a user scans a receipt? Also, an explanation to how some datetimes are configured would be appreciated.
3. Market reach: What is the explanation to why there are no Gen-Z users? What can we do to broaden our user base to younger people? Does Fetch have appeal to younger people?