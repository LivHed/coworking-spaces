# The Coworking Swede 
This is my Milestone Project 3: Data Centric Development - Code Institute.

This is a page for people that wants to find and use a coworking space located in swedish cities, and also be able to add, edit and delete coworking spaces.
The idea of this web page is that the database will grow over time, when users add more coworking spaces. My aim is that the co-creation of the page will provide a sense of community; A page for coworkers, by coworkers.
In this app I have used the programming language Python along with the Python micro web framework Flask, and the document-based database MongoDB.
[Check it out here!]()


## UX

### Design process
After doing research looking at websites with coworking spaces I found that there was no pages dedicated only to Swedish coworking spaces, which is a gap I wanted to fill. The intention of the pages I found where to search for these spaces globally. I wanted to narrow this search down to only swedish spaces for myself and my fellow swedish coworkers. My goals with the design was set to:

* To make the design suitable for people who wants to find coworking spaces in an easy way. I wanted to do this with a stylistic and easily understandable design with light and discrete colors and with buttons showing clear directions.
* To make a webpage with several pages, each with it´s clear purpose, and this with a user friendly and easy layout to quick be able to understand what you can do and how.
* The fonts that I chose to use for this website are Railway (sans serif) because it presents the content in a stylistic and easy-to-read way.

### Wireframes
The wireframes are created with Balsamiq. They where made as a part of the design process and are saved as a pdf document and kept in the separate folder; wireframes. One is designed for desktop view and the other for mobile view. Check them out here! (link to it here!)

### User stories
* As an employee at a company, that works remotely from home, I would like to change my workspace from time to time. I want to be able to search for coworking spaces in the city where I live and to be able to edit and add information about them when I have tried them.
* As an entrepreneur working with a small startup without an office space yet, me and my colleagues want to find a coworking space to work from when needed for meetings or as a temporary office space shared with others.
* As a self-employed and freelancer working remotely I´m interested in the coworking scene in Sweden as I travel a lot to meet with clients and work from wherever I´m positioned at the moment. I have a lot of contacts and insight in this area and I want to be able to add workspaces on this webpage to share my knowledge with others, and also edit and/or delete information if updates I´m aware of have been made for these places or if a place have become inactive or shut down.
* As an employee I have asked for permission from my boss to work remotely for a week to try it out, to see if it could be a new way of working that suits both me and the company. I want to search for a coworking space in a city in another part of Sweden to spend this week there.

### Features
#### Existing Features
* The presentation text is placed under the name of the page and provides a short introduction to the intention of the page, which give the users a direct way of reading about the page the first thing they do when they land on the page.
* The dropdown menu with the cities in it is placed underneath the introduction text as a natural next step to follow after reading about it and follow the directions given in the text.
* The functions of the radio buttons when clicked on them is that they return results with either accommodations or restaurants in the chosen city, depending on which button you click, and shows icon markers of the found places. The results are displayed in a discrete way with no background color to keep the simple design of the whole page.
* The Result list is shown in a responsive way, 20 results at a time. Up to 60 results can be shown for either restaurants or accommodations in each city, if found within the radius I have specified.
* The More results button shows 20 more results when pressing it.
* The manual zoom function of the map is kept for the users to be able to zoom in even more themselves to see a close-up of where the places are located.
* The background color is supposed to give the users a feeling of the page´s authenticity when it comes to environmental sustainable thinking, and relate to the title of the page with its green insinuation.
* The name of the webpage is placed in the navbar in a center position, like a brand or logo, meant to be discrete with the transparent background of the navbar.

#### Features Left to Implement
* In the future I want to add more ..
* I want to add ..
* If I have had more time in the project I would have focused on and worked more with the UI.
* If I have had more time I would also have added a footer that was sticked to the bottom of the page.
* I want to add info windows to show the name and adress of the place in a small window when clicking on the iconmarkers, and also those details to be shown in the result list beside the names.
* In the future I also want to add an option to perform a textSearch in the cities, to narrow down the search to be more related to "green travels" with specific words related to sustainability, like "organic" or "sustainable".

## Technologies Used
#### Languages
* [HTML5](https://www.w3schools.com/html/html5_intro.asp), [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) and [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) 
* [Python](https://www.python.org/download/releases/3.0/)

#### Libraries
* [Google Fonts](https://fonts.google.com/) is used to style the fonts of the website.
* [Bootstrap](https://www.bootstrapcdn.com/) for the content to be responsive and a simple structure of the web page.
* [JQuery](https://jquery.com/) to simplify DOM manipulation, and for the Bootsrap components that requires the use of JavaScript to function.
* [Popper.js](https://popper.js.org/) also for the Bootsrap components that requires the use of JavaScript to function.
* [Font Awesome](https://fontawesome.com/) for the icons. 
* [PyMongo](https://api.mongodb.com/python/current/) to be able to work with MongoDB from Python.
* [Flask](https://flask.palletsprojects.com/en/1.0.x/) to be able to build and render pages. 
* [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) to get and display data from the backend with template inheritance and loops in html.

#### Tools
* [AWS Cloud9 IDE](https://aws.amazon.com/cloud9/) for the development of this site: writing, debugging and running my code. GIT was then used to push files to Github.
* [GitHub](https://github.com/) to store and share the project remotely.
* [MongoDB Atlas](https://www.mongodb.com/cloud) is the database I have used for this project.
* [Balsamiq](https://balsamiq.com/) to create my wireframes as a part of the design process, with a simple yet goodlooking result.
* [Responsinator](http://www.responsinator.com/) was used to check the responsiveness of the page.

## Testing
Here I present how my website meet the needs of the users that will visit the site, which I presented in the section UX: User stories:

* As an employee at a company, that works remotely from home, I would like to change my workspace from time to time. I want to be able to search for coworking spaces in the city where I live and to be able to edit and add information about them when I have tried them. -->
* As an entrepreneur working with a small startup without an office space yet, me and my colleagues want to find a coworking space to work from when needed for meetings or as a temporary office space shared with others. -->
* As a self-employed and freelancer working remotely I´m interested in the coworking scene in Sweden as I travel a lot to meet with clients and work from wherever I´m positioned at the moment. I have a lot of contacts and insight in this area and I want to be able to add workspaces on this webpage to share my knowledge with others, and also edit and/or delete information if updates I´m aware of have been made for these places or if a place have become inactive or shut down. -->
* As an employee I have asked for permission from my boss to work remotely for a week to try it out, to see if it could be a new way of working that suits both me and the company. I want to search for a coworking space in a city in another part of Sweden to spend this week there.-->

(remove these, look at for insp)
* As an environmentally conscious traveller I want to have a look at cities with a sustainable focus before I travel there, to get inspired and remember to keep the focus of those things I find most important in the society. --> The information about the list of the sustainable cities and how to find them in the map are easily seen in the introduction right underneath the heading, and are therefore easy to understand how to find by choosing a city in the dropdown menu, and to see on the map with icons and listed in the result list below it. It´s also possible to read more about this list on the company's website that is linked to in the text.
* As an environmentally conscious traveller on the road right now I would like to know where to eat and stay for the night while exploring the sustainable city I´m currently in. --> This information can easily be found on a smartphone on the go, since the webpage has a mobile-first design with a simple and easy understandable layout.
* As a traveller with many different kinds of interests I would like to check this page out, out of pure curiosity, to see what kinds of cities the environmentally conscious travellers would want to visit, and maybe travel there myself to see what these cities are like. --> This research can be done from home or on the go, beforehand or during the stay in the city, like described above.

### Validation of code
- I used [this website](https://validator.w3.org/#validate_by_input) to validate my HTML by direct input.
- I used [this website](https://jigsaw.w3.org/css-validator/validator.html.en#validate_by_input) to validate my CSS by direct input.
- I used JS Hint to check my Javascript code for errors and potential problems.

### The responsiveness of the whole website
- The webpage is fully responsive for these devices: Galaxy S5, Pixel 2, Pixel 2XL, IPhone 5 SE, Iphone 6/7/8, IPhone 6/7/8 Plus, Iphone X, tested in Chrome Developer Tools and Responsinator.

### The responsive parts of the website

- The webpage is responsive since I´m using Bootstrap 4 and it works good on smaller devices too. The dropdown menu, the radio buttons and the map is placed inside of responsive columns and the resultlist is placed inside of a responsive table.
- The title of the page is inside of a navbar, which is responsive by default.
- The More results button responds to get more results when it´s clicked, until the limit is reached.
- The resultlist is cleared when a new city is chosen, and when clicking the other radio button.
- The Google maps Javascript API and Places library is responsive in itself and is set to respond to the interactions of the user.

### Testing process scenarios
Dropdown menu with cities
1. Click on the dropdown menu.
2. Choose a city to see that it´s zoomed in on as intended.
3. Try this with all of the cities one by one, and verify that the function is working for all of them.

Radio buttons
1. Click on the accommodations radio button for every selected city and verify that the results of accommodations are showing on the map with the proper marker icons.
2. Click on the restaurants radio button for every selected city and verify that the results of restaurants are showing on the map with the proper marker icons.

More results button
1. When the first 20 results are showing in the Results list, click on More results button and verify that 20 new results are showing in the list.
2. Click the button again and verify that 20 more results are showing.
3. Verify that the button is unable to click again when 60 results have been shown and the button have been clicked two times.

### Bugs I came across while creating the site and while testing it

* When clicking on..  the results are not shown..
* 
* 

## Deployment

### Local Deployment
For local deployment you must have an IDE, like [Visual Studio Code](https://code.visualstudio.com/) and the following to be installed locally on your machine: [git](https://git-scm.com/), [PIP](https://pip.pypa.io/en/stable/installing/), [Python 3](https://www.python.org/downloads/), [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/) and a [MongoDB Atlas account](https://docs.atlas.mongodb.com/).
* After creating your own folder and are in it, type this in to the terminal `git clone https://github.com/LivHed/coworking-spaces.git`
* Then run this command `pip install --upgrade pip`
* To be followed by this command `pip install -r requirements.txt` to install the required modules. 
* You can run the app with the command `python -m flask run`

### Heroku Deployment
This website is deployed on Heroku, following these steps:

* First, create a `requirements.txt` file using the `pip freeze > requirements.txt` command in the terminal. 
* Then,create a Procfile with the command `echo web: python app.py > Procfile` in the terminal. 
* Then type the `git add` and `git commit` commands for these new files and then `git push` to GitHub.
* Then go to the Heroku website and go to Dashboard and click on the New button, and then click on Create new app. Name it and set the region to Europe.
* In the new Heroku app, Click on Deploy. In the section Deployment method, click on Github.
* Choose the correct GitHub repository to link it to the Heroku app.
* In the section Automatic Deploys, click on Enable automatic deploys, from master branch.
* Now go to Settings and click on Reveal config vars, and set them to: 
```
IP : 0.0.0.0
PORT: 5000
MONGO_URI: mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
SECRET_KEY: <your_secret_key>
```
* You will get the MONGO_URI in your created database on the Mongo Db Atlas page. Keep that string and the secret key as environment variables so only you can access them.
* Click on the button Open app in the top right corner and you can now view your deployed app.

## Credits

## Content
* The content on the website was written by me, after doing research in other coworking space pages and after reading about the concept.
* The content that are showing in the results are gathered from the coworking spaces own web pages, and I´m making sure me and other people are linking to these coworking spaces own homepages so that people can read further about them and give them more traffic and people that are using their spaces.

## Media
* 

## Acknowledgements
* For the results showing of the coworking spaces I copied the Album example code from this page https://getbootstrap.com/docs/4.0/examples/album/ and then modified the layout for my needs.
