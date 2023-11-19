# Paleo Database

- Paleo Database is a database website for displaying personal collections of fossils in the form of an onlinemuseum. Users are also able create an account to interract with each upload with comments. The comment section is designed to be a place where other users can provide the most up to date information about each specemin so that identifications are most up to date. Users that provide the updated information will be credited for any useful information. As a site admin I am able to upload remove and edit existing content including comments and specimen uploads.

- this app was developed using uthe agile principles. At the beginning of the project, I created the following user stories in  github projects and created the following issues as user story tasks. these user stories atarted in the cambian board with no status and were moved form the 'to do' section, to the 'in progress' section and then 'done' throughout the process of development. 
 1. As a user I can create an account so that i can view my personal collection
 2. As a site user I can add specimen pages so that other users can view and comment of them.
 3. As a site user I can add additional information to images so that i can document specific details
 4. As a user/admin I can write comments so that i can interact with specimens and provide other users with more up to date information
 5. As an admin I can approve or reject comments so that all comments are constructive
 6. As a site user I can view and write comments and like other users comments
 7. As a site user I can see all of the specimens that i have uploaded so that i can select one to view
 8. As a site user I can see the specimens on pages so that i can view further informations 
 9. As a site user/admin I can update specimens so that all information is up to date 


## How to use the app
- Users are able to login and log out through links on the navbar. if the user does not have an account registered with the all, then they will need to create on through the sign up option. 
- To return to the home page, there is the home logo in the top left of the sceen which is displayed across all pages and will return to the display of all submitted specimens. 
- To view individual uploads, click on the cards containing easch specimen. this will take the user to the specimen display page, where additional information will be displayed on the specimen and the comment section is able to be viewed.
### comment section
- comments are submitted through the form on the comment section. The comment section is located by clicking on a specimen to load the specimen display.
- comments will be submitted to the admin pannel, waiting to be approved by app admins.
- After the comment is submitted, the comments will appear underneath the specimen details section in time order, newest a the top. 


## bug fixes and errors in code.

### fixed bugs
- when loading in the static files, I was unable to load the css, however after changing the filepaths I was able to get the css file loaded in. 
- removed space in url that lead to my home page being unable to load in.
- various spelling errors and syntax errors.
- when trying to load the submitted photos from cloudinary onto the web page the photos would not render. When rendering the images using a cloudinary tag for example {% cloudinary 'image_url' %} i was able to get them displayed on individually on the page, but was unable to display it when iterating through each database submission. I submited the code to various online forums as well as recieving help in person from another developer. Despite this, I was unable to get the photos working as they should and had to move on due to project submission time limit.
- loading in comment section caused my specemin_details page to break/ the error message being TemplateDoesNotExist at /latin-name/ despite working before the comment section was added. I have added and removed the comment section code twice aswell as referring to multiple different forums for help. i have been unable to fix this code due to time constraints. 


## How i will progress with the app in the future
- I would like to implement a feature to filter the collection by specific features eg. by location or by species of fossil in order to find and compare specific specimens more easily.
- the point previously could also be implemented through the use of the user being able to create folders to store different items in, such as storing all items from a specific location in a seperate html file. 

## credits 
- project was created while using the code institute django walkthrough project. I used code institutse code to model my own models, functions nad overall structure around. 

## testing
### Testing method
The method i have used for testing is string testing. this is a standard method for integrating the various modules of an application and then testing their behaviour as a combined, or integrated, unit. This is an industry standard method for testing software applications as it provides a library of tests that can be used for proving that bugs have been fixed and insuring that other bugs have not been introduced via regression testing.
### html 
- ran html through w3c validator
### css
- ran css through w3c validator
### string testing against requirements
#### -account registration#4
-Step1
enter username email and password and submit.
- Pass/Fail: Pass
-Step2 log out and log back in using details
- Pass/Fail: Pass
-Step3 check that the nav bar is displayed on each page of signup menu. 
- Pass/Fail: Pass
#### -photo upload#1
-Step1 check that photos can be uploaded via the admin page. 
- Pass/Fail: Pass
-Step2 check that the photo is in the cloudinary database and viewable on the cloudinary website. 
- Pass/Fail: Pass
#### -add additional information to items#6
-Step1 check that the correct fields exist to add all relevent information on the admin pannel. 
- Pass/Fail: Pass
-Step2 check that the information provided is saved to the admin pannel. 
- Pass/Fail: Pass
#### -manage posts #9
-Step1 check that admin users are able to save the specimen items and comments as daft or published.
- Pass/Fail: Pass
-Step2 check that new uploads can be created and deleted. 
- Pass/Fail: Pass
#### -update information on database items #5
-Step1 check that information can be added and removed from database entries. 
- Pass/Fail: Pass
#### -can see uploads#2
-Step1 check that new entries are added to home page when created. 
- Pass/Fail: Pass
-Step2 check that nwhen entries are deleted, the home page is updated without deleted entries. 
- Pass/Fail: Pass
-Step3 check that information on each upload is displayed. 
- Pass/Fail: pass
#### -view uploads as a page #10
-Step1 check the specimen uploads on the home page link to new page. 
- Pass/Fail: Pass
-Step2 check that new page is able to be viewed. 
- Pass/Fail: pass 
#### -write comments #12
-Step1 check that new comments are abe to be created and posted by the user. 
- Pass/Fail: Pass
-Step2 check that new comments are abe to be created through the specimen display page. 
- Pass/Fail: pass
#### -view comments#11
-Step1 check that comments are able to be viewed in the admin pannel. 
- Pass/Fail: Pass
-Step2 check that new entries are added comment secion. 
- Pass/Fail: pass


### user stories 





