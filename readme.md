# Django Restaurant App

### Description
This Restaurant App as part of my Django learning experience. Restaurant App features a Landing page which showcases 
a Menu which dynamically displays all the meals the restaurant prepares. Each meal has dynamically created separate page
which lists a description of the ingredients used.

### Technologies
Primary focus was using Django to create the project structure. Reason for using Django was the native users feature,
which allows the app to register cooks, which can then add recipes they know how to make and display said recipes as
dishes in the Restaurant menu.

As a database I used the Django native SQLite3, in order to store information about users and dishes.

For the front-end, I made HTML templates for the Index page and Menu Item page. The index page is the main page where
all dishes are displayed dynamically using Jinja. Each dish then has a link which leads to a separate Menu Item page,
which showcases each dish separately, and displays information about ingredients. A good idea would be to store images
of dishes to fill in the blank space on Menu Item page, and I might do it in the future. Styling is done with Bootstrap.