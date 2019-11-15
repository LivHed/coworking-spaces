# The Coworking Swede 
This is my Milestone Project 3: Data Centric Development - Code Institute.

This is a page for people that wants to find and use a coworking space located in swedish cities, and also be able to add, edit and delete coworking spaces.
The idea of this web page is that the database will grow over time, when users add more coworking spaces. My aim is that the co-creation of the page will provide a sense of community; A page for coworkers, by coworkers.
In this app I have used the programming language Python along with the Python micro web framework Flask, and the document-based database MongoDB.
[Check it out here!](https://coworking-swede.herokuapp.com/)

## UX

### Design process
After doing research looking at websites with coworking spaces I found that there was no pages dedicated only to Swedish coworking spaces, which is a gap I wanted to fill. In the pages I found you could search for these kind of spaces globally. I wanted to narrow this search down to spaces placed in swedish cities, for myself and my fellow swedish coworkers. My goals with the design was set to:

* To make the design suitable for people who wants to find coworking spaces in an easy way. I wanted to do this with a stylistic and easily understandable design with light and discrete colors and buttons with clear directions.
* To make a web application with several pages, each with it´s clear purpose, and this with a user friendly and easy layout to quick be able to understand what you can do and how.
* The fonts that I chose to use for this website are Railway (sans serif) because it presents the content in a stylistic and easy-to-read way.
* I chose to use 10 of the biggest cities in Sweden to choose from in the search of coworking spaces, since there will be coworking spaces in these cities to choose from for the user to add.

Since this page is supposed to handle the CRUD functionality (Create, Read, Update and Delete) I planned for this web page to give a sense of "Let´s do it together", and I´m specifying the guidelines in the About page. 

### Wireframes
The wireframes are created with Balsamiq. They where made as a part of the design process and are saved as a pdf document and kept in the separate folder; wireframes. All of the pages are showed as I planned them and one example of mobile view can be found on the last page in the document. [Check them out here!](https://github.com/LivHed/coworking-spaces/blob/master/wireframes/BalsamiqMockupMilestone3finnish.pdf)

### User stories
* As an employee at a company, that works remotely from home, I would like to change my workspace from time to time. I want to be able to search for coworking spaces in the city where I live and to be able to edit and add information about them when I have tried them.
* As an entrepreneur working with a small startup without an office space yet, me and my colleagues wants to find a coworking space to work from when needed for meetings or as a temporary office space shared with others.
* As a self-employed and freelancer working remotely I´m interested in the coworking scene in Sweden as I travel a lot to meet with clients and work from wherever I´m positioned at the moment. I have a lot of contacts and insight in this area and I want to be able to add workspaces on this webpage to share my knowledge with others, and also edit and/or delete information if updates I´m aware of have been made for these spaces or if one have become inactive or shut down.
* As an employee I have asked for permission from my boss to work remotely for a week to try it out, to see if it could be a new way of working that suits both me and the company. I want to search for a coworking space in a city in another part of Sweden to spend this week there.

## Features
#### Existing Features
* The presentation text is placed under the name of the page and provides 
* The select menu with the cities and the search button is placed underneath the name of the page and the sentence with what you can do on this landing page, as a natural next step of action to follow.
* The Coworking spaces and the details about them are shown in album cards, in a responsive way. The user can click on the link to view the coworking space´s own webpage. 
* The fields in the forms are required (except for the insert image field), so the user won´t be able to submit the forms until all fields are filled in. This will show nicely in the cards, with all fields complete inside of them. 
* The name of the webpage is placed in the navbar in the left corner as good common pratcice. The navbar collapse to a burger icon on smaller devices.

#### Features Left to Implement
* In the future I want to add authentication with Sign up / Log in forms, so that the edit/add/delete functionality for the information of the coworking spaces is only for logged in members.
* I want to add a timepicker to the Add and Edit forms to choose opening and closing times for the coworking spaces, from dropdowns. This for a more simple and user-friendly way to add this than what I currently have.
* If I have had more time in the project I would have focused on and worked more with the UI.
* If I have had more time I would also have wanted to aded a footer sticked to the bottom of the page.
* In the future I would want for users to add cities, at the moment only I can add cities from the database. 
* I also want to add pagination to show only 3 or 6 cards per page. 
* Since this project did not require authentication, nothing happends when you click on the Send button in the Contact form, this is something I´ll fix later when there is time.

## Technologies Used
#### Languages
* [HTML](https://www.w3schools.com/html/html5_intro.asp), [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) and [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) 
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

## Information Architecture
* In the database MongoDB I created two collections:
```
cities
coworkingspaces
```
An example of the structure and the key-value pairs from the cities collection:
```
city_name: "Stockholm"  
```
An example of the structure and the key-value pairs from the coworkingspaces collection:
```
city_name: "Stockholm"
coworking_name: "Impact Hub Stockholm"
coworking_description: "Impact Hub is the world’s largest network of social entrepreneurs, and..."
coworking_address: "Luntmakargatan 25, 111 37 Stockholm"
opening_hours: "Mon-Fri 9:00 am - 5:00 pm"
website_url: "https://stockholm.impacthub.net/"
image_url: "https://coworker.imgix.net/photos/sweden/stockholm/impact-hub-stockhol..."
``` 

## Testing
Here I present how my website meet the needs of the users that will visit the site, which I presented in the section UX: User stories:

* As an employee at a company, that works remotely from home, I would like to change my workspace from time to time. I want to be able to search for coworking spaces in the city where I live and to be able to edit and add information about them when I have tried them. --> This is possible to do from the landing page, where it´s clear what to do. The first thing you see is the text that tells you that you can find a coworking space on this page, clearly with using the select menu of cities and a search button.
* As an entrepreneur working with a small startup without an office space yet, me and my colleagues want to find a coworking space to work from when needed for meetings or as a temporary office space shared with others. --> THis need can be met as in the example above, with the search function for the cities that are presented in the dropdown menu. 
* As a self-employed and freelancer working remotely I´m interested in the coworking scene in Sweden as I travel a lot to meet with clients and work from wherever I´m positioned at the moment. I have a lot of contacts and insight in this area and I want to be able to add workspaces on this webpage to share my knowledge with others, and also edit and/or delete information if updates I´m aware of have been made for these places or if a place have become inactive or shut down. -->
* As an employee I have asked for permission from my boss to work remotely for a week to try it out, to see if it could be a new way of working that suits both me and the company. I want to search for a coworking space in a city in another part of Sweden to spend this week there.-->

### Validation of code
- I used [this website](https://validator.w3.org/#validate_by_input) to validate my HTML by direct input.
- I used [this website](https://jigsaw.w3.org/css-validator/validator.html.en#validate_by_input) to validate my CSS by direct input.
- I used JS Hint to check my Javascript code for errors and potential problems.

### The responsiveness of the whole website
- The webpage is fully responsive for these devices: Galaxy S5, Pixel 2, Pixel 2XL, IPhone 5 SE, Iphone 6/7/8, IPhone 6/7/8 Plus, Iphone X, tested in Chrome Developer Tools and Responsinator.

### The responsive parts of the website

- The webpage is responsive since I´m using Bootstrap 4 and it works good on smaller devices too. Yhe navbar collapse on smaller views with a standard navbar icon for smaller devices.
- The title of the page inside of the navbar in the top left corner takes the user back to the landing page when it´s clicked on. 
- 
-

### Testing process scenarios

#### Manual testing
-Choose a City- select menu and -Search- button
1. Click on the dropdown menu.
2. Choose a city.
3. Click on the search button.
4. Try this with all of the cities one by one, and verify that results with cards are showing if the chosen city matches the city on the card.
5. Verify that the text "No coworking spaces found" is showing, if no coworking spaces exist in the database from the chosen city.

Edit a coworking space
1. Click on the Edit button on a card containing information about a coworking space. 
2. Verify that you are redirected to the Edit Coworking space page.
3. Verify that it´s possible to choose one of the cities from the select menu.
3. Change the pre-filled fields if you want.
4. Check that all of the fields are required, leave one by one empty and click on the update button, and verify that it´s not possible to click on the Update button if the fields are not filled in.
5. Try to leave the image link field empty and verify that this is the only field you can leave empty and still be able to click on the Update button to be redirected to the landing page and see the updated card with a default image displayed. 

Delete a coworking space
1. On the Edit page, click on the Delete button
2. verify that the modal is showing and that you will be given one more chance to be sure that you want to delete this coworking space. 
3. Click on the No, go back button and verify that you are back on the Edit page.
4. If you choose to click on the Yes, I´m sure button, verify that the coworking space have been deleted when you get redirected to the landing page. 

Add a coworking space
1. Click in the navbar on Add a coworking space.
2. Verify that it´s possible to choose one of the cities from the select menu.
2. Fill the fields with your information about a coworking space you have in mind. 
3. Check that all of the fields are required, leave one by one empty and click on the Add button, and verify that it´s not possible to add a new coworking space if the fields are not filled in.
4. Try to submit the coworking space without a link to an image.
5. Verify that this is the only field you can leave empty and still be able to click on the Add button to redirect you to the landing page and that you can see a default image displayed in the card with the new coworking space you just created.

Contact form
1. Click on the Contact page in the navbar.
2. Fill in the fields, verify that they are required by leaving one out, and see that a text shows that says that you have to fill in that field.
3. Click on the Submit button and verify that the form is not submitted, you are still on the page. (This is because this project did not require authentication, and is therefore something I´ll add later when there is time.)

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
* You can run the app with the command `python3 app.py`

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
* I´m using this image as the default image to show in the cards when the user´s not adding an image url to the forms, from pexels.com, [see it here](https://images.pexels.com/photos/7097/people-coffee-tea-meeting.jpg)


## Acknowledgements
* For the results showing of the coworking spaces I copied the Album example code from this page https://getbootstrap.com/docs/4.0/examples/album/ and then modified the layout for my needs.
