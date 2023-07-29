# Paleo Database

Paleo Database is a database website for displaying my personal collection oof fossils in the form of an onlinemuseum. Users are also able create an account to interract with each upload with comments. The comment section is designed to be a place where other users can provide the most up to date information about each specemin so that identifications are most up to date. Users that provide the updated information will be credited for any useful information. As a site admin i am able to upload remove and edit existing content including comments and specimen uploads

## How to use the app
- Users are able to login and log out through links on the navbar. if the user does not have an account registered with the all, then they will need to create on through the sign up option. 
- toreturn to the home page, there is the home logo in the top left of the sceen which is displayed across all pages and will return to the display of all submitted specimens. 
- to view individual uploads, click on the cards containing easch specimen. this will take the user to the specimen display page, where additional information will be displayed on the specimen and the comment section is able to be viewed.
### comment section
- comments are submitted through the form on the comment section. The comment section is located by clicking on a specimen to load the specimen display.
- comments will be submitted to the admin pannel, waiting to be approved by app admins.
- After the comment is submitted, the comments will appear underneath the specimen details section in time order, newest a the top. 


## bug fixes and errors in code.

### currenetly active bugs
- when trying to load the submitted photos from cloudinary onto the web page the photos would not render. When rendering the images using a cloudinary tag for example {% cloudinary 'image_url' %} i was able to get them displayed on individually on the page, but was unable to display it when iterating through each database submission. I submited the code to various online forums aswell as recieving help in person from another developer. Despite this, I was unable to get the photos working as they should and had to move on due to project submission time limit.
- loading in comment section caused my specemin_details page to break/ the error message being TemplateDoesNotExist at /latin-name/ despite working before the comment section was added. I have added and removed the comment section code twice aswell as referring to multiple different forums for help. i have been unable to fix this code due to time constraints. 

### fixed bugs
- when loading in the static files, I was unable to load the css, however after changing the filepaths i was able to ge the css file loaded in. 
- removed space in url that lead to my home page being unable to load in.
- various spelling errors and syntax errors.

## How i will progress with the app in the future
- Despite being unable to fully complete what my aim was in this project, it has been massively fulfilling and has taught me a lot. i will continue to work on this project ot hopefully fix the current errors so that i can progress and improve the project. 
- During the making of this project my vision of the project has changed massively. it was initiially going to be a place where people could upload their own findings to a public fossil database. through making this app, i was able to realise that without giving admin access to a large amount of people this would not be the best way to go forward. Through speaking to museums, this project has moved to a more private display for individuals or organisations such as a museum or private collecter. Each individual that uses this website template therfore has the opportunity to display their collection to the public, where some people may not be nececcarilty be able to visit the museum in person they would be able to do so online and view the specimen up close. the website can also be kept private and be used as a categorisation website to easily organise and track all specimens within the collection rather than keeping records of each item on paper. 
- I would like to implement a feature to filter the collection by specific features eg. by location or by species of fossil in order to find and compare specific specimens more easily.
- the point previously could also be implemented through the use of the user being able to create folders to store different items in, such as storing all items from a specific location in a seperate html file. 

## credits 
- project was created while using the code institute django walkthrough project. I used code institutse code to model my own models, functions nad overall structure around. 

## testing
### html 
- ran html through w3c validator
### css
- ran css through w3c validator


