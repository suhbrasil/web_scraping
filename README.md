# web_scraping
Web scraping on Gupy page

The gupy page uses continuous scrolling instead of pagination, so I used the webdriver to open all the elements in the list on the "front" of the site, then I selected a name from the div's class that encompassed the position information, company name and city ​​of the vacancy, I collected this information and saved it in a list. As the main page of the gupy website does not start with a list of vacancies, to carry out a larger search, I created a list with vacancy names and placed a variable in the website url to go through each item on the list and increase the number of vacancies researched.
