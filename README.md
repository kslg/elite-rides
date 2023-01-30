<h1 align="center">Elite Rides</h1>

[Elite Rides](https://pp5-elite-rides.herokuapp.com/) is an E-commerce store that specialises in die-cast models of luxury, high-end cars. As a Customer you are able to purchase a product and set up and online account. Guest checkout is also available. As the Store Admin, you can login from the store-front and edit the product details, and delele products too.
Elite Rides is responsive which makes shopping possible on mobile and table devices. 

[Visit the website](https://pp5-elite-rides.herokuapp.com/)

![image](/documentation/iamresponsive_image.png)

<br>

## **Contents**
* [User Experience Design](#user-experience-design)
* [Strategy Plane](#strategy-plane)
* [The Scope Plane](#the-scope-plane)
* [The Structure Plane](#the-structure-plane)
* [The Skeleton Plane](#the-skeleton-plane)
* [Manifestations of Data](#manifestations-of-data)
* [The Surface Plane](#the-surface-plane)
* [Features](#features)
* [User Journeys and Manual Testing](#user-journeys-and-manual-testing)
* [Agile Project Management](#agile-project-management)
* [Performace](#performance)
* [Technologies Used](#technologies-used)
* [Information Architecture](#information-architecture)
* [Deployment](#deployment)
* [Heroku Deployment](#heroku-deployment)
* [Credits and Acknowledgements](#credits-and-acknowledgements)
* [Future Features](#future-features)
* [w3c Markup Valiation notice](#w3c-markup-valiation-notice)

---

# User Experience Design

I used the 5 Planes of UX to provide a conceptual framework.


# Strategy Plane:

## Target Audience:

- `User - Customers` Hobby enthusiasts, mainly adults who can make purchases online.
- `Admin` E-Commerce Managers.
- `Super Admin` Store Owner, E-Commerce Managers.

## Mission Objectives:

- To develop an `mvp (minimum viable product)` that allows `Users` to navigate an online store and purchase a product.
- The shopping experiecne must be simple in design and navigation.
- `Admins` will have a store-front login to manage product cataloge.
- `Super Admins` can access the Django back-end to view and manages Order and Customer data.

### The Why:

- As a high-end car aficionado and collector, it's hard to find a company online that deals with only styling models. Also, existing competitors don't stand out in the market. 
- I want to promote an exlusive presence and target a younger and modern audience. 
- Make die-cast models attractive again. Not fucusing on racing and classic cars.

## Ideas and Inspiration Mind Map
![image](/documentation/mind_map/mind_map.png)

## Content Strategy:

- Main functionality is to purchase a product through checkout.
- Keep content simple and easy to digest. 
- Let the imagery and branding become more engaging.

## Typography:
https://fonts.google.com/
Jura was used due to it's luxury, modern look and feel. It's easy to read.
![image](/documentation/typography/google_font.png)

[Back to contents](#contents)

# The Scope Plane:

## Functional Requirements for an MPV:

1. Checkout functionality 
2. Account Profile and User Authentication
3. CRUD Functionality
4. Site Navigation
5. Newsletter SignUp
6. Stripe 3rd Party Payment Integration
7. Search Functionality
8. Order Confirmation Email
9. SEO Optimisation
10. Company Information Pages
11. Accessibilty
12. Product Detail Page
13. Product Listing Page
14. Triggered Customer Messaging
15. Taxonomy: Category Tree
16. Standard E-commerce store layout (Header, Footer, Homepage)
17. Error Handling
18. 404 Error Page
19. Shipping Rate Logic

[Back to contents](#contents)

## Content Requirements:

- `Customer` Homepage with hero text and a hero banner.
- `Customer` Category Pages
- `Customer` Contact Us Form
- `Customer` Company Information Pages(About, T&Cs, Privacy Policy, Cookie Policy)
- `Customer` Footer to include Social Media Links, Links to Company Info and Newsletter signup. 
- `Customer` Account Related Pages: Login, Register.
- `Admin` Access to manage products with CRUD functionality. 

[Back to contents](#contents)

## Interaction Design:

- All CTA (Call to Action) buttons will change colour to let the customers know that the buttons are clickable. 
- The `Customer` and `Admin` are notified for changes and major actions.
- The `Customer` recieves an order email confirmation when checkout has successfully completed.

[Back to contents](#contents)

## Scope of MVP:
Using the MoSCoW prioritisation method to outline the importance of each requirement and what needs to be delivered in the MVP.

| Requirements | Must Have | Should Have | Could Have | Won't Have |
| ------------- | ------------- | ------------- | ---------- | ---------- |
| USP (Unique Selling Point) Carousel on Homepage | Y | - | - | - |
|Checkout functionality | Y | - | - | - |
|Role-Based Login and Registration | Y | - | - | - |
|Restrict User access to Admin area | Y | - | - | - |
|Admin CRUD Functionality | Y | - | - | - |
|Site Navigation | Y | - | - | - |
|Newsletter SignUp | Y | - | - | - |
|Stripe 3rd Party Payment Integration | Y | - | - | - |
|Search Functionality | Y | - | - | - |
|Order Confirmation Email | Y | - | - | - |
|SEO Optimisation | Y | - | - | - |
|Company Information Pages | Y | - | - | - |
|Accessibilty | Y | - | - | - |
|Product Detail Page | Y | - | - | - |
|Product Listing Page | Y | - | - | - |
|Triggered Customer Messaging | Y | - | - | - |
|Taxonomy: Category Tree | Y | - | - | - |
|Standard E-commerce store layout (Header, Footer, Homepage) | Y | - | - | - |
|Error Handling | Y | - | - | - |
|404 Error Page | Y | - | - | - |
|Responsive Design | Y | - | - | - |
|Front-end messages to notify the user and admin of any changes. | Y | - | - | - |
|CAPTCHA Function | - | Y | - | - |
|Display Sale Price | - | Y | - | - |
|Current login state reflected to the user | - | - | - | Y |
|Hero Banner Carousel | - | - | - | Y |
|Product Reviews | - | - | - | Y |
|Product Image Carousel | - | - | - | Y |
|Shipping Rate Logic | Y | - | - | - |


[Back to contents](#contents)

# The Structure Plane:

## Site Architecture

![image](/documentation/site_architecture/EliteRides_Data_Flow_Diagram.jpeg)

[Back to contents](#contents)

## Roles and Processes

- Permitted access based on `User`, Teacher `Admin` and `Super Admin` Role:

| Page Name | Customer | Admin | Super Admin |
| ------------- | ------------- | ------------- | ---------- |
| Home page                   | Y | Y | Y |
| Login page                  | Y | Y | Y |
| Registration page           | Y | Y | Y |
| Logout page                 | Y | Y | Y |
| Admin: Model Management               | N | Y | Y |
| Product Page w/ Edit & Delete  | N | Y | Y |
| Checkout           | Y | Y | Y |
| Contact Us         | Y | Y | Y |


[Back to contents](#contents)

# The Skeleton Plane:

## Header and Footer:
- White background.
- Black text.
- Hover States: Underline style.

- Wireframes Examples:
<br>

![image](/documentation/wireframes/wireframes_header.png)
![image](/documentation/wireframes/wireframes_footer.png)
<br>


[Back to contents](#contents)

## Colour Palette:

![image](/documentation/color_palette/color_palette_blackandwhite.png)


# Manifestations of Data

## Data at rest

1. Customer Orders in the Admin
<br>

![image](/documentation/manifestations_of_data/data_at_rest_orders.png)
<br>

2. Products and Categories in the Admin
<br>

![image](/documentation/manifestations_of_data/data_at_rest_products.png)
![image](/documentation/manifestations_of_data/data_at_rest_product_categories.png)

3. Customer Messages in the Admin
<br>

![image](/documentation/manifestations_of_data/data_at_rest_customer_messages.png)

4. Newsletter Subscribers in MailChimp 
<br>

![image](/documentation/manifestations_of_data/data_at_rest_newsletter_subscribe.png)



## Data in motion

1. Order Data is `captured` from the Checkout and `stored` in the database.
<br>

![image](/documentation/manifestations_of_data/data_in_motion_orders.png)
<br>

2. An `order confirmation email` is sent to the `Customer` when they have successfully completed checkout.
<br>

![image](/documentation/manifestations_of_data/data_in_motion_order_confirmation_email.png)
<br>

3. Products and Categories can be `edited` and `added` from the admin area.
<br>

![image](/documentation/manifestations_of_data/data_in_motion_products.png)
![image](/documentation/manifestations_of_data/data_in_motion_categories.png)
<br>

4. Customer messages can be `viewed` and `updated` from the admin area.
<br>

![image](/documentation/manifestations_of_data/data_in_motion_customer_messages.png)
<br>



## Data in use

1. `Customers` can `update` delivery information and `view` order history in thier online profile.
<br>

![image](/documentation/manifestations_of_data/data_in_use_delivery_information_and_order_history.png)
<br>

2. `Customers` can view a `completed order` with details.
<br>

![image](/documentation/manifestations_of_data/data_in_use_completed_order.png)
<br>

3. `Customers` can `subscribe to the newsletter` from the footer.
<br>

![image](/documentation/manifestations_of_data/data_in_use_newsletter_subscribe.png)
<br>

# The Surface Plane:

## **Mobile First Design**

Prioritising design for mobiles makes sense as there are space limitations in devices with smaller screen sizes and need to ensure that the key elements of the website are prominently displayed for anyone using those screens.

[See the mobile wireframes here](/documentation/wireframes/)

Web visitors on Mobile contributes to approximately half of the overall web traffic.
The number of mobile users has surpassed desktop users. As per Statcounter GlobalStats, overall mobile users continue to grow with a leading market share of 60.43% as compared to desktop users.

---

# Features

## **Navbar**

## *Navbar elements for E-commerce:*
- Home Page link (Elites Rides Logo) 
- Search bar
- My Account
- Shopping Bag
- Dropdown Navigation Menu

To satisfy an MPV and keeping the Navbar simple allows Customers to become familiar with the store more quickly.

- Mobile
<br>
![image](/documentation/features/navbar/navbar_mobile.png)
<br>
- Desktop
<br>
![image](/documentation/features/navbar/navbar_desktop.png)

<br>

## **CRUD Functionality**

## *CRUD Create: Admins Only - In Model Management, you can add a new product to the catalogue*

### [Go to page](https://pp5-elite-rides.herokuapp.com/products/add/)
<br>

![image](/documentation/features/crud_functionality/CRUD_Create_Model_Management.png)

## *CRUD Read - In My Profile, Customers can see their Default Delivery Information and Order History*

### [Go to page](https://pp5-elite-rides.herokuapp.com/profile/)
<br>

![image](/documentation/manifestations_of_data/data_in_use_delivery_information_and_order_history.png)

## *CRUD Update - Admins Only - Can Edit Product Details directly from the Product Page*

<br>

![image](/documentation/features/crud_functionality/CRUD_Update_Model_Management_Edit.png)
![image](/documentation/features/crud_functionality/CRUD_Update_Model_Management.png)

## *CRUD Delete - Admins Only - Can Delete the Product directly from the Product Page*
<br>

![image](/documentation/features/crud_functionality/CRUD_Delete_Model_Management.png)

## *CRUD Delete - Defensive Programming using Bootstrap Modal*

I used the Bootstrap modal pop up to alert the Admin that they are about the delete the product from the catalogue.
Once they click `Delete`, the product is deleted from the `Database`
<br>

![image](/documentation/features/crud_functionality/CRUD_Delete_Defensive_Programming_Modal.png)

[Back to contents](#contents)

## **Accounts and User Authentication**

`django-allauth` is an integrated set of Django applications dealing with account authentication, registration, management, and third-party (social) account authentication. It is one of the most popular authentication modules due to its ability to handle both store and social logins. 

## *Sign in page*

### [Go to page](https://pp5-elite-rides.herokuapp.com/accounts/login/)
<br>

![image](/documentation/features/accounts_and_authentication/sign_up_page.png)

## *Registration page*

### [Go to page](https://pp5-elite-rides.herokuapp.com/accounts/signup/)
<br>

![image](/documentation/features/accounts_and_authentication/register_page.png)

## *Customer Verification*

1. When the Customer registers for the first time, they are asked to `verify` their email address.
![image](/documentation/features/accounts_and_authentication/email_verification.png)
2. An email is sent to the Customer asking them to confirm this with an confirmation link.
![image](/documentation/features/accounts_and_authentication/confirm_email_address_email.png)
3. When the Customer clicks on the link, they are directed back to the store to confirm once more.
![image](/documentation/features/accounts_and_authentication/confirm_email_address.png)
4. Finally, after confirmation, the Customer is then directed to the Sign In page. A `Toast message` tells the Customer that their email address was successfully confirmed. 
This means The Customer is now stored in the `database`.
![image](/documentation/features/accounts_and_authentication/email_address_confirmed.png)

## *Customer Restrictions*

To prevent unauthorised access to Admin functionality (Create, Update, Delte), restriction logic is in place to stop Customers access those areas. 

- A `logged in Customer` is presented with `Toast Error Message` when trying to access Model Management URL:
![image](/documentation/features/accounts_and_authentication/customers_restricted_access_add.png)
<br>

- A `logged in Customer does not` have the ability to `Edit` and `Delete` from the Product pages:
![image](/documentation/features/accounts_and_authentication/customers_restricted_access_edit_delete.png)


[Back to contents](#contents)

## **Order Confirmation Email**

**An Order Confirmation Email is sent to the Customer after placing an order.**

![image](/documentation/manifestations_of_data/data_in_motion_order_confirmation_email.png)

[Back to contents](#contents)

## **Bootstrap Theme**
Bootstrap 4 is a free front-end framework for faster and easier web development
Bootstrap includes HTML and CSS based design templates for typography, forms, buttons, tables, navigation, modals, image carousels and many other, as well as optional JavaScript plugins
Bootstrap also gives you the ability to easily create responsive designs

### [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

## **Bootstrap Toasts - Alert Messages**
- Alert popups are used to `improve Customer user experience`. Alert popup give users clear feedback as a result of their actions and any server response.
- I used Bootstrap 4 Toasts: Lightweight notifications designed to mimic the push notifications that have been popularized by mobile and desktop operating systems.
- 4 Toast Messages: Error, Info, Success and Warning.
- Set a display timer of 3 seconds. After 3 seconds the message will go.
- A close icon on the toast so customers can manually close.

## **Bootstrap Carousel - USP (Unique Selling Points)**

![image](/documentation/features/bootstrap_carousel.png)


[Back to contents](#contents)


## **Guest Checkout**
Guest Customers are able to navigate and purchase a product without signing up for a customer account. They don't have to sign in or save any information to website besides their email address.

The Guest Customer has the option to Create an Account at the Checkout Success Page.

`Befenits of Guest Checkout` is that you can `convert the Customer much quicker`, removing the friction for certain customers.

<br>

![image](/documentation/features/guest_checkout.png)


[Back to contents](#contents)

## **Shipping Logic**

- Customers are offered `Free Shipping` when they spend over £50.
- The delivery fee threshold can be updated at code-level.
- The functionality `calculates the current Bag Total` and informs the Customer of how much they need to spend extra to qualify for free shipping.
<br>

![image](/documentation/features/shipping_logic/free_shipping_calculation.png)
<br>

![image](/documentation/features/shipping_logic/free_shipping_bag_page.png)

[Back to contents](#contents)

## **MailChimp Integration**
- Customers can sign up to `Elite Rides Email Marketing` by providing there email address.
- Here I am using MailChimp to `capture the Customer emails` and `manage the subscibers via the MailChimp admin`.
<br>

![image](/documentation/features/newsletter_signup_mailchimp.png)
![image](/documentation/manifestations_of_data/data_at_rest_newsletter_subscribe.png)


[Back to contents](#contents)

## **404 Page**
A 404 page, or error page, is the content the Customer sees when they try to reach a non-existent page on the site. It’s the page the server displays when it can’t find the URL requested by the customer.

404 errors can be frustrating for Customers, so the main purpose of a 404 page is to turn the potential negative user experience of encountering an error into a positive one.

I've added a link back to all products page so the Customer can restart their shopping journey.
<br>

![image](/documentation/features/404_error_page.png)


[Back to contents](#contents)

---

# Agile Project Management
I used Jira Project Tracking Software to manage the backlog for the project.
Jira Software is an agile project management tool that supports any agile methodology, be it scrum, kanban, or your own unique flavor. I was able to plan, track, and manage the whole project in Jira.

I tested against the Acceptance Criteria in the Jira User Stories.

[Go to Jira](https://krishangharu.atlassian.net/jira/software/projects/ER/boards/2)


[Back to contents](#contents)

---

# **Performance**

### **Google Lighthouse Score**
![Image](/documentation/readme_folder/images/google_lighthouse_score.png)

### **Microsoft Edge Lighthouse score**
![Image](/documentation/readme_folder/images/microsoft_devtools.png)

[Back to contents](#contents)

---

# **Technologies used**

- ## Languages:
    
    + [Python 3.8.5](https://www.python.org/downloads/release/python-385/): is the main language used to build the back-end.
    + [JS](https://www.javascript.com/): for the CAPTCHA Refesh function and to handle the timeout for bootstrap alerts.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): is markup language used to build the front-end templates.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): is styling language used adjust layout and front-end styles.

- ## Frameworks and libraries:

    + [Django](https://www.djangoproject.com/): a high-level Python web framework for the app.
    + [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/overview.html): is an integrated set of Django applications dealing with account authentication, registration and management.
    + [CrispyForms](): is an optimised way of rendering forms on the front-end in a very elegant and `DRY` way. 

- ## Databases:

    + [PostgreSQL](https://www.postgresql.org/): database to store all data.

- ## Other tools:

    + [Github](https://github.com/): hosting service for software development and version control using Git.
    + [Pip3](https://pypi.org/project/pip/): is the package manager to intstall Python modules and libraries.
    + [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/): "Green Unicorn" is a Python Web Server Gateway to translate HTTP Rquests for Python to understand.
    + [Spycopg2](https://pypi.org/project/psycopg2/): PostgreSQL database adapter so I can manage the Database in Python. 
    + [Heroku](https://dashboard.heroku.com/): the hosting service to host the app.
    + [VSCode](https://code.visualstudio.com/): the IDE used to program the app.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): used to identify any errors when being rendered in the browser.
    + [Font Awesome](https://fontawesome.com/): used to source social icons to be used on the app.
    + [Draw.io](https://www.lucidchart.com/) used to create the Database schema.
    + [W3C Validator](https://validator.w3.org/): used to validate HTML5 code.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): used to validate CSS code.
    + [flake8](https://pypi.org/project/flake8/): was used to validate Python code.

[Back to contents](#contents)

---

# Information Architecture


## Entity-Relationship Diagram

* The ERD was created using [lucid.app](https://www.lucid.app).

![Database Schema](/documentation/erd/EliteRides_Schema.jpeg)



[Back to contents](#contents)


---

## Deployment

- The app was deployed to [Heroku](https://heroku.com).
- The app can be reached by the [link](https://kslg-appointment-app.herokuapp.com/)


---


## Heroku Deployment

**Final Deployment Process**

* Set DEBUG=False in settings.py.
* Delete DISABLE_COLLECTSTATIC from Config Vars in Heroku dashboard.
* Commit and push the changes to GitHub. 
* Trigger a deplopyment in Heroku

[Back to contents](#contents)

---

## Credits and Acknowledgements

- [Date Picker](https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django)
- [Customise User Registration, Login, and Logout in Django](https://ordinarycoders.com/blog/article/django-user-register-login-logout)
- [What is PEP8's E128: continuation line under-indented for visual indent?](https://stackoverflow.com/questions/15435811/what-is-pep8s-e128-continuation-line-under-indented-for-visual-indent)
- [How to Create a Drop-down List in a Django Form](http://www.learningaboutelectronics.com/Articles/How-to-create-a-drop-down-list-in-a-Django-form.php)
- [Django @login_required for class views](https://stackoverflow.com/questions/28555260/django-login-required-for-class-views)
- [Django message upon logout is confusing to users #2031](https://github.com/pennersr/django-allauth/issues/2031)
- [Bootstrap 4 Alerts](https://getbootstrap.com/docs/4.6/components/alerts/)
- [Django Simple Captcha](https://django-simple-captcha.readthedocs.io/en/latest/usage.html)
- [Colour Pallete](https://www.color-hex.com/color-palette/1006818)
- [What is CAPTCHA](https://support.google.com/a/answer/1217728?hl=en#:~:text=CAPTCHA%20offers%20protection%20from%20remote,must%20to%20pass%20the%20test.)
- [How to auto close an alert after few seconds with Bootstrap?](https://stackoverflow.com/questions/68165290/how-to-auto-close-an-alert-after-few-seconds-with-bootstrap)
- [Bootstrap Modal](https://getbootstrap.com/docs/4.6/components/modal/)
- Insipred by the `Hello Django Project` and the `I Think Threfore I Blog Project`
- Readme.md layout inspired by fellow student Luliia Konovalova (Juliia_Konn_5P)  



[Back to contents](#contents)

---

# Future Features
1. Users could manage thier own appointments.
2. Add Relational Database model between Teacher, Class and Child.
3. Restrict appointment dates in the past.

[Back to contents](#contents)

# w3c Markup Valiation notice

Upon chekcing the markup validation for the appointment page I can see alerts related to the captcha but these are not elements i can easlily get to and resolve.

![Database Schema](/documentation/readme_folder/images/w3cvaliadation_captcha.png)

---

## End of readme.md

---