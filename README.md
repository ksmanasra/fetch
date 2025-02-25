# fetch
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

Second: provide SQL queries
1. Closed-ended questions:

    1. What are the top 5 brands by receipts scanned among users 21 and over?
    2. What are the top 5 brands by sales among users that have had their account for at least six months?
    3. What is the percentage of sales in the Health & Wellness category by generation?

2. Open-ended questions: for these, make assumptions and clearly state them when answering the question.

    1. Who are Fetch’s power users?
    2. Which is the leading brand in the Dips & Salsa category?
    3. At what percent has Fetch grown year over year?

Third: communicate with stakeholders
    ...