# Fetch
Data Analyst Assessment

Repository includes
1. README file, which includes answers to assessment
2. SQL/Python scripts
3. Visualizations


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

        >Year over year, based on when users signed up for Fetch, Fetch has grown as follows:
            Year    New Users
            2014       30
            2015       51
            2016       70
            2017      644
            2018     2168
            2019     7093
            2020    16883
            2021    19159
            2022    26807
            2023    15464
            2024    11631


Third: Communicate with stakeholders
    ...