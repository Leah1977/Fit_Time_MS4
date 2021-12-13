# Testing Of Milestone Project 4

## Table of Contents.

1.  [CSS Validation](#css-validator)
2.  [HTML Validation](#html-validator)
3.  [JS Validation](#js-validator)
4.  [Wireframe Comparison](#wireframe)
5.  [Lighthouse](#lighthouse)
6.  [Mobile](#mobile-testing)
7.  [Project Testing](#deployed-testing)
    - [Links](#links)
    - [Overlay](#overlay)
    - [Sign-up Form](#form)
8.  [User Stories](#user-stories)
    - [User Story 1](#user-story-1)
    - [User Story 2](#user-story-2)
    - [User Story 3](#user-story-3)
    - [User Story 4](#user-story-4)
9.  [Debugging](#debugging)

[Back to README.md](README.md)

## An excel spreadsheet of userstories for testing

![User Stories](media/testingimages/ms4 checklist.png)

## CSS Validator

Tested on W3C CSS Validator
[CSS Validation for https://fit-time-ms4.herokuapp.com/](https://jigsaw.w3.org/css-validator/validator)

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p

## HTML Validator

Pass code through HTML Validator
[CSS Validation for https://fit-time-ms4.herokuapp.com/]

[http://fit-time-ms4.herokuapp.com/](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffit-time-ms4.herokuapp.com%2F)
[https://fit-time-ms4.herokuapp.com/products](https://validator.w3.org/nu/?doc=https%3A%2F%2Ffit-time-ms4.herokuapp.com%2Fproducts%2F)
[https://fit-time-ms4.herokuapp.com/](https://validator.w3.org/nu/?doc=http%3A%2F%2Ffamily-favs-project.herokuapp.com%2Flogin)
[https://fit-time-ms4.herokuapp.com/](https://validator.w3.org/nu/?doc=http%3A%2F%2Ffamily-favs-project.herokuapp.com%2Fcreate_recipe)
[http://fit-time-ms4.herokuapp.com/](https://validator.w3.org/nu/?doc=http%3A%2F%2Ffamily-favs-project.herokuapp.com%2Fget_categories)

## JS Validator

Tested the site with jshint.com validator.

## Wireframe Comparison

Comparing the deployed version against the development version(wireframes)

## Lighthouse

Tested the site using Lighthouse 

![Lighthhouse Review](static/images/testing_images/lighthousereport.png)

## Mobile

Tested the site for mobile-friendly usage

[https://search.google.com/test/mobile-friendly](https://search.google.com/test/mobile-friendly?id=10B7YLqttRT7af4Ml0gyCA)

![Mobile friendly approved](static/images/testing_images/mobilefriendly.png)

## Project Testing

### Links

I have tested all links on all pages. All links work as intended. This allows the user to move from one page to another with ease.


## Debugging

Shopping basket not opening

Missing endfor tag in template
This was an indentation error.
Went back through all the code and corrected indentation for endfor tag.
Also corrected spelling error for basket.
![BasketError](media/testingimages/blocktagmissing.png)


## Favicon issue

Favicon not displaying.
Since my last project, adding the favicon required a few different steps.
Solved this error by going through the steps with 
favicon generator.

And including the following tags

```
<!-- Favicon -->
            <link rel="apple-touch-icon" sizes="180x180" href="{% static 'favicon/apple-touch-icon.png' %}">
            <link rel="icon" type="image/png" sizes="32x32" href="{% static 'favicon/favicon-32x32.png' %}">
            <link rel="icon" type="image/png" sizes="16x16" href="{% static 'favicon/favicon-16x16.png' %}">
            <link rel="manifest" href="{% static 'favicon/site.webmanifest' %}">
```


## Add Review Error

## 500 Error
## No Image not loading
Had a lot of trouble with Internal Server issues

![]()
![Error 500](media/testingimages/error_500.png)


I was getting an issue telling me that my products didnt' exist.
![Products Issue](media/testingimages/Screenshot 2021-12-07 104951.png)

I thought this was an error due to my database, but with help from tutor support, 
I realised I had renamed the images and they no longer matched the database.
![Renamed images in media folder](media/testingimages/Screenshot 2021-12-07 132726.png)

I fixed this error and made sure the image names match with my Amazon S3 media file so that they could be called correctly.
![AmazonS3](media/testingimages/Screenshot 2021-12-07 132812.png)

I updated the media folders through Admin
![DjangoAdmin](media/testingimages/Screenshot 2021-12-07 134912.png)

Once they were the same, the images could now display correctly
![AmazonS3](media/testingimages/Screenshot 2021-12-07 135319.png)

Product Images displaying correctly
![ProductImages](media/testingimages/ProductImages.png)



## Contact page error

## Nutrition Icon missing

## End of Testing Section

## No Image not loading


## Line length too long

Correct all issues with line length.  Run python3 -m flake8 and improve code formatting.

## Syntax Error in Basket

When I tried to open the app.  I got and Error 500
I then reset my config vars to DEVELOPMENT = True so I could see where the error was coming from.

The error pointed to a syntax error in my basket app.

!(SyntaxError)[media/testingimages/syntax_error_basket.png]

Fixed error by finding missing { and inserting it where necessary

Removed DEVELOPMENT = True from Config Vars


## Scrolling error with Footer

Text was scrolling behind footer.  This meant the user couldn't see the buttons for checking
out or submitting.

Removed the fixed bottom option from the header and this resolved the issue.

"""
Error: Element li not allowed as child of element nav in this context. (Suppressing further errors from this subtree.)

From line 115, column 1; to line 115, column 29

eens -->↩↩<li class="list-inline-item">↩ 
"""
- Added <ul> to child element <li>



"""
Error: No space between attributes.

At line 180, column 78

="all-products"type="button"

"""

- add a space to correct this error.


"""
Warning: The type attribute is unnecessary for JavaScript resources.

From line 322, column 13; to line 322, column 43

          <script type="text/javascript">↩    
"""

- Removed the type="text/javascript" as no longer necessary.



## User Story Testing

## User Story 1

  
### What do I expect to find on a sports app?

1. I expect to be able to navigate around the app with ease.

2. I expect to be able to search for items to buy.

3. I would expect the app to be visually appealing.

5. I would like to be able to edit my shopping bag.

6. I would like the site to be informative.


## User Story 2

  As a website user, I want the app to be easy to use.  I would expect to be able to register and for my details to be secure and safe.

### What do I expect to find on a web application?

  

1. Can I view my shopping bag?

2. Can I edit my shopping bag?

3. Can I delete items from my shopping bag?

  

## User Story 3

### Would this app be suitable for younger family members?

  

1. Is the website suitable for all family members?

2. Is it easy to navigate?

3. What age is the app intended?

  

As a user, I would like to be able to edit my shopping bag.
  
## User Story 4

### Would this app have a good range of items?

  
1. Is the app easy to navigate?

2. Are there educational advantages to this app?


As a user, I would like to share my experiences and opinions of items bought.
 

As a first time user, I would expect

•   A registration option.

•   A login option.

•   Good Graphics

•   A good variety of items to buy.

•   A search option
  

As a returning user, I would expect 


•   A login option to create a user profile. 

•   My profile page is to be private for my use.

•   Updated content.

  

As a designer, I would expect

  

•   All buttons to be working

•   All links to be active

•   To be able to navigate through the site with ease

•   To have a 404 page to return users to the home page.

•   Striking colours to engage the user

•   To be able to add or delete categories.

*   To be able to add or delete products.
  
[Return to Table of Contents](#table-of-contents)
