<h1 align="center">Elite Rides</h1>

[Elite Rides](https://pp5-elite-rides.herokuapp.com/) is an E-commerce store that specialises in die-cast models of luxury, high-end cars. As a Customer you are able to purchase a product and set up and online account. Guest checkout is also available. As the Store Admin, you can login from the store-front and edit the product details, and delele products too.
Elite Rides is responsive which makes shopping possible on mobile and table devices. 

[Visit the website](https://pp5-elite-rides.herokuapp.com/)

![image](/documentation/iamresponsive_image.png)

<br>

# **Contents**
- [User Experience Design](#user-experience-design)
- [Strategy Plane](#strategy-plane)
    * [Target Audience](#target-audience)
    * [Mission Objectives](#mission-objectives)
    * [The Why](#the-why)
    * [Ideas and Inspiration Mind Map](#ideas-and-inspiration-mind-map)
    * [Content Strategy](#content-strategy)
    * [Typography](#typography)
- [Scope Plane](#scope-plane)
    * [Functional Requirements for an MPV](#functional-requirements-for-an-mpv)
    * [Content Requirements](#content-requirements)
    * [Interaction Design](#interaction-design)
    * [Scope of MVP](#scope-of-mvp)
- [Structure Plane](#structure-plane)
    * [Site Architecture](#site-architecture)
    * [Roles and Processes](#roles-and-processes)
- [Skeleton Plane](#skeleton-plane)
    * [Header and Footer](#header-and-footer)
    * [Colour Palette](#colour-palette)
    * [Manifestations of Data](#manifestations-of-data)
        + [Data at rest](#data-at-rest)
        + [Data in motion](#data-in-motion)
        + [Data in use](#data-in-use)
- [Surface Plane](#surface-plane)
    * [Mobile First Design](#mobile-first-design)
- [Features](#features)
    * [Navbar](#navbar)
        + [Navbar elements for E-commerce](#navbar-elements-for-e-commerce)
    * [CRUD Functionality](#crud-functionality)
        + [CRUD Create - Admins Only](#crud-create---admins-only)
        + [CRUD Read - In My Profile](#crud-read---in-my-profile)
        + [CRUD Update - Admins Only](#crud-update---admins-only)
        + [CRUD Delete - Admins Only](#crud-delete---admins-only)
        + [CRUD Delete - Defensive Programming](#crud-delete---defensive-programming)
    * [Accounts and User Authentication](#accounts-and-user-authentication)
        + [Sign In page](#sign-in-page)
        + [Registration page](#registration-page)
        + [Customer Verification](#customer-verification)
        + [Customer Restrictions](#customer-restrictions)
        + [Using Decorators](#using-decorators)
    * [Order Confirmation Email](#order-confirmation-email)
    * [Bootstrap Theme](#bootstrap-theme)
        + [Bootstrap Toasts - Alert Messages](#)
        + [Bootstrap Carousel - USP (Unique Selling Points)](#)
    * [Guest Checkout](#guest-checkout)
    * [Shipping Logic](#shipping-logic)
    * [Sort By Filter](#sort-by-filter)
    * [404 Page](#404-page)
- [SEO Optimisation](#seo-optimisation)
    * [Internal and External Links and SEO](#internal-and-external-links-and-seo)
    * [Sitemap XML](#sitemap-xml)
    * [Robots.txt](#robotstxt)
    * [Keyword Research](#keyword-research)
- [Web Marketing Strategy](#web-marketing-strategy)
    * [Content Marketing](#content-marketing)
    * [Social Media Marketing](#social-media-marketing)
    * [Email Marketing](#email-marketing)
- [Agile Project Management](#agile-project-management)
- [Strip Integration](#strip-integration)
    * [Testing Stripe](#testing-stripe)
    * [Injecting Stripe](#injecting-stripe)
    * [Get Stripe working in Gitpod](#get-stripe-working-in-gitpod)
    * [Stripe Handle Form Submission](#stripe-handle-form-submission)
    * [Stripe Webhooks](#stripe-webhooks)
- [Accessibility](#accessibility)
- [Performance](#performance)
    * [Google Lighthouse Score](#google-lighthouse-score)
    * [Microsoft Edge Lighthouse score](#microsoft-edge-lighthouse-score)
- [HTML and CSS Code Validation](#html-and-css-code-validation)
- [Technologies used](#technologies-used)
    * [Languages](#languages)
    * [Frameworks and libraries](#frameworks-and-libraries)
    * [Databases](#databases)
    * [Other tools](#other-tools)
- [Information Architecture](#information-architecture)
    * [Entity-Relationship Diagram](#entity-relationship-diagram)
- [Deployments and Database Setup](#deployments-and-database-setup)
    * [Creating an external database using ElephantSQL](#creating-an-external-database-using-elephantsql)
    * [Create a Heroku app to connect to the new database](#create-a-heroku-app-to-connect-to-the-new-database)
    * [Set up the project to connect to new ElephantSQL database](#set-up-the-project-to-connect-to-new-elephantsql-database)
    * [Confirm that the data was migrated to ElephantSQL database](#confirm-that-the-data-was-migrated-to-elephantsql-database)
    * [Deployment to Github](#deployment-to-github)
    * [Deployment to Production](#deployment-to-production)
    * [Heroku Deployment](#heroku-deployment)
    * [Final Deployment Process](#final-deployment-process)
- [Use of env.py](#use-of-envpy)
- [Amazon Web Services S3](#amazon-web-services-s3)
    * [Amazon - Identify and Access Management (IAM)](#amazon---identify-and-access-management-iam)
    * [AWS Config Vars](#aws-config-vars)
    * [AWS Cache Control](#aws-cache-control)
- [Credits and Borrowed Resources](#credits-and-borrowed-resources)
    * [BootStrap Support](#bootstrap-support)
    * [Project Support](#project-support)
    * [E-commerce User Stories Support](#e-commerce-user-stories-support)
    * [Static Content and Copy](#static-content-and-copy)
    * [Product Details and Images](#product-details-and-images)
    * [Mind Map images](#mind-map-images)
    * [Web and Social Media Marketing](#web-and-social-media-marketing)
- [Bugs Encountered during Testing](#bugs-encountered-during-testing)
    * [Bug 1](#bug-1)
    * [Bug 2](#bug-2)
- [Future Features](#future-features)

# User Experience Design
I used the 5 Planes of UX to provide a conceptual framework.

# Strategy Plane

## Target Audience

- `User - Customers` Hobby enthusiasts, mainly adults who can make purchases online.
- `Admin` E-Commerce Managers.
- `Super Admin` Store Owner, E-Commerce Managers.

## Mission Objectives:
- To develop an `mvp (minimum viable product)` that allows `Users` to navigate an online store and purchase a product.
- The shopping experiecne must be simple in design and navigation.
- `Admins` will have a store-front login to manage product cataloge.
- `Super Admins` can access the Django back-end to view and manages Order and Customer data.

## The Why
- As a high-end car aficionado and collector, it's hard to find a company online that deals with only styling models. Also, existing competitors don't stand out in the market. 
- I want to promote an exlusive presence and target a younger and modern audience. 
- Make die-cast models attractive again. Not fucusing on racing and classic cars.

## Ideas and Inspiration Mind Map
![image](/documentation/mind_map/mind_map.png)

## Content Strategy
- Keep content simple and easy to digest. 
- Let the imagery and branding become more engaging.

## Typography
https://fonts.google.com/
Jura was used due to it's luxury, modern look and feel. It's easy to read.
![image](/documentation/typography/google_font.png)

[Back to contents](#contents)

# Scope Plane

## Functional Requirements for an MPV

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

## Content Requirements

- `Customer` Homepage with hero text and a hero banner.
- `Customer` Category Pages
- `Customer` Contact Us Form
- `Customer` Company Information Pages(About, T&Cs, Privacy Policy, Cookie Policy)
- `Customer` Footer to include Social Media Links, Links to Company Info and Newsletter signup. 
- `Customer` Account Related Pages: Login, Register.
- `Admin` Access to manage products with CRUD functionality. 

[Back to contents](#contents)

## Interaction Design

- All CTA (Call to Action) buttons will change colour to let the customers know that the buttons are clickable. 
- The `Customer` and `Admin` are notified for changes and major actions.
- The `Customer` recieves an order email confirmation when checkout has successfully completed.

[Back to contents](#contents)

## Scope of MVP
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

# Structure Plane

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

# Skeleton Plane

## Header and Footer
- White background.
- Black text.
- Hover States: Underline style.

- Wireframes Examples:
<br>

![image](/documentation/wireframes/wireframes_header.png)

![image](/documentation/wireframes/wireframes_footer.png)
<br>


[Back to contents](#contents)

## Colour Palette

![image](/documentation/color_palette/color_palette_blackandwhite.png)

[Back to contents](#contents)

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

[Back to contents](#contents)

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

[Back to contents](#contents)

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

[Back to contents](#contents)

# Surface Plane

## Mobile First Design

Prioritising design for mobiles makes sense as there are space limitations in devices with smaller screen sizes and need to ensure that the key elements of the website are prominently displayed for anyone using those screens.

[See the mobile wireframes here](/documentation/wireframes/)

Web visitors on Mobile contributes to approximately half of the overall web traffic.
The number of mobile users has surpassed desktop users. As per Statcounter GlobalStats, overall mobile users continue to grow with a leading market share of 60.43% as compared to desktop users.

[Back to contents](#contents)

# Features

## Navbar

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

[Back to contents](#contents)

## CRUD Functionality

## *CRUD Create - Admins Only*
- In Model Management, you can add a new product to the catalogue.
### [Go to page](https://pp5-elite-rides.herokuapp.com/products/add/)
<br>

![image](/documentation/features/crud_functionality/crud_create_model_management.png)

## *CRUD Read - In My Profile*
- Customers can see their Default Delivery Information and Order History.

### [Go to page](https://pp5-elite-rides.herokuapp.com/profile/)
<br>

![image](/documentation/manifestations_of_data/data_in_use_delivery_information_and_order_history.png)

## *CRUD Update - Admins Only* 
- Can Edit Product Details directly from the Product Page.

<br>

![image](/documentation/features/crud_functionality/CRUD_Update_Model_Management_Edit.png)

<br>

![image](/documentation/features/crud_functionality/CRUD_Update_Model_Management.png)

## *CRUD Delete - Admins Only* 
- Can Delete the Product directly from the Product Page.
<br>

![image](/documentation/features/crud_functionality/CRUD_Delete_Model_Management.png)

## *CRUD Delete - Defensive Programming*
- I used the Bootstrap modal pop up to alert the Admin that they are about the delete the product from the catalogue.
- Once they click `Delete`, the product is deleted from the `Database`
<br>

![image](/documentation/features/crud_functionality/CRUD_Delete_Defensive_Programming_Modal.png)

[Back to contents](#contents)

## Accounts and User Authentication

`django-allauth` is an integrated set of Django applications dealing with account authentication, registration, management, and third-party (social) account authentication. It is one of the most popular authentication modules due to its ability to handle both store and social logins. 

## *Sign In page*

### [Go to page](https://pp5-elite-rides.herokuapp.com/accounts/login/)
<br>

![image](/documentation/features/accounts_and_authentication/sign_up_page.png)

## *Registration page*

### [Go to page](https://pp5-elite-rides.herokuapp.com/accounts/signup/)
<br>

![image](/documentation/features/accounts_and_authentication/register_page.png)

[Back to contents](#contents)

## *Customer Verification*

1. When the Customer registers for the first time, they are asked to `verify` their email address.
<br>

![image](/documentation/features/accounts_and_authentication/email_verification.png)
2. An email is sent to the Customer asking them to confirm this with an confirmation link.
<br>

![image](/documentation/features/accounts_and_authentication/confirm_email_address_email.png)
3. When the Customer clicks on the link, they are directed back to the store to confirm once more.
<br>

![image](/documentation/features/accounts_and_authentication/confirm_email_address.png)
4. Finally, after confirmation, the Customer is then directed to the Sign In page. A `Toast message` tells the Customer that their email address was successfully confirmed. 
This means The Customer is now stored in the `database`.
<br>

![image](/documentation/features/accounts_and_authentication/email_address_confirmed.png)

[Back to contents](#contents)

## *Customer Restrictions*

To prevent unauthorised access to Admin functionality (Create, Update, Delte), restriction logic is in place to stop Customers access those areas. 

- A `logged in Customer` is presented with `Toast Error Message` when trying to access Model Management URL:
<br>

![image](/documentation/features/accounts_and_authentication/customers_restricted_access_add.png)
<br>

- A `logged in Customer does not` have the ability to `Edit` and `Delete` from the Product pages:
<br>

![image](/documentation/features/accounts_and_authentication/customers_restricted_access_edit_delete.png)

[Back to contents](#contents)

## *Using Decorators*
In the views.py files for Product and Profile apps, I imported from django.contrib.auth.decorators
called `login_required`

Decorators are special functions that wrap around another function and return a new one with some additional functionality.

In the case of `login_required` for example, wherever I use this decorator it will make Django first check whether the Customer is logged in before executing the view.
If the Customer is not logged in, it will redirect them to the Sign In page.
I added `@login_required` on the line immediately above each view I want to decorate.

[Back to contents](#contents)

## Order Confirmation Email

## *An Order Confirmation Email is sent to the Customer after placing an order.*

![image](/documentation/manifestations_of_data/data_in_motion_order_confirmation_email.png)

[Back to contents](#contents)

## Bootstrap Theme
Bootstrap 4 is a free front-end framework for faster and easier web development
Bootstrap includes HTML and CSS based design templates for typography, forms, buttons, tables, navigation, modals, image carousels and many other, as well as optional JavaScript plugins
Bootstrap also gives you the ability to easily create responsive designs

### [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

## Bootstrap Toasts - Alert Messages
- Alert popups are used to `improve Customer user experience`. Alert popup give users clear feedback as a result of their actions and any server response.
- I used Bootstrap 4 Toasts: Lightweight notifications designed to mimic the push notifications that have been popularized by mobile and desktop operating systems.
- 4 Toast Messages: Error, Info, Success and Warning.
- Set a display timer of 3 seconds. After 3 seconds the message will go.
- A close icon on the toast so customers can manually close.

## Bootstrap Carousel - USP (Unique Selling Points)

![image](/documentation/features/bootstrap_carousel.png)

[Back to contents](#contents)

## Guest Checkout
Guest Customers are able to navigate and purchase a product without signing up for a customer account. They don't have to sign in or save any information to website besides their email address.

The Guest Customer has the option to Create an Account at the Checkout Success Page.

`Befenits of Guest Checkout` is that you can `convert the Customer much quicker`, removing the friction for certain customers.

<br>

![image](/documentation/features/guest_checkout.png)

[Back to contents](#contents)

## Shipping Logic

- Customers are offered `Free Shipping` when they spend over £50.
- The delivery fee threshold can be updated at code-level.
- The functionality `calculates the current Bag Total` and informs the Customer of how much they need to spend extra to qualify for free shipping.
<br>

![image](/documentation/features/shipping_logic/free_shipping_calculation.png)
<br>

![image](/documentation/features/shipping_logic/free_shipping_bag_page.png)

[Back to contents](#contents)

## Sort By Filter
I added a sort by product filter on the product listing page. 
This helps the customer order the product by name, price, make, model and cateogry.
This is another way to help boost conversion so the customers can see what they want more quickly, and increase the chances of a purchase being made.

![image](/documentation/sort_by/sort_by_product_filter.png)

[Back to contents](#contents)

## 404 Page
A 404 page, or error page, is the content the Customer sees when they try to reach a non-existent page on the site. It’s the page the server displays when it can’t find the URL requested by the customer.

404 errors can be frustrating for Customers, so the main purpose of a 404 page is to turn the potential negative user experience of encountering an error into a positive one.

I've added a link back to all products page so the Customer can restart their shopping journey.
<br>

![image](/documentation/features/404_error_page.png)

[Back to contents](#contents)

# SEO Optimisation

I've added `meta data` and a `title` to the base.html page. This helps Search engines like Google when looking for matches based on what the user searches for.  

I added a `description`, `keywords` and `author`. Search Engines will display the title and description information in their search results. 

## Internal and External Links and SEO

Social links contain the `rel="noopener"` attribute, which tells search engines not to include these links when it looks at our search engine ranking.  

## Sitemap XML
I've create a xml sitemap which is a file that lists a website’s important page urls, making sure that search engines can crawl, or navigate, through them. It also helps search engines  understand the website structure.
A sitemap file ensures search engines will crawl every essential page on your website.
A sitemap can help speed up content discovery for search engines when they crawl and index the site.

[Back to contents](#contents)

## Robots.txt
I've added a robots.txt file which is a simple text file that tells search engines where they are not allowed to go on a website. It lists out any folders or files that will not be crawled or indexed by search engine spiders. 

Having a robots.txt file shows that I have acknowledged that search engines are allowed on the site and that they may have free access to it.

For this reason, search engines take the existence of this file in your projects as a sign of quality, and so it improves the SEO ranking as a result.

## Keyword Research

| Short-tail Keywords | Long-tail Keywords |
| ------------- | ------------- |
| diecast models | high end diecast cars |
| diecast cars | toy car models |
| ~~luxury toys~~ | luxury toy cars |
| ~~car toys~~ | british diecast models |
| ~~luxury diecast~~ | italian diecast models |
| ~~luxury~~ | german diecast models |
| ~~car models~~ | mercedes diecast models |
| ~~luxury models~~ | ferrari diecast models |
| - | lamborghini diecast models |
| - | bentely diecast models |
| - | luxury diecast models |

[Back to contents](#contents)

# Web Marketing Strategy

1. Who are your users?
- Hobby enthusiasts, mainly adults who can make purchases online.

2. Which online platforms would you find lots of your users?
- I would find them on Social Media such as Facebook, Instagram, Twitter, YouTube. 
- Also on online communities like Reddit.

3. What do your users need? Could you meet that need with useful content? If yes, how could you best deliver that content to them?
- High quality imagery would be most attractive along with detailed product specifications.
- User Reivews would also boost consumer confidence, building on brand trust and loyalty.

4. Would your business run sales or offer discounts? How do you think your users would most like to hear about these offers?
- I would run regular sale promotions during peak seasons. 
- I could setup online voucher codes to be redeemed when purchasing online. 
- The vouchers would be sent via email to customers that have opted in to recieve marketing.
- I can also get into affiliate marketing where content ceators / influencers can promote offers.

5. What are the goals of your business? 
- Main goal is to increase conversion.
- To build brand awareness.
- Build the subscriber list.
- Build social media awareness and keep customers talking about thr brand.

6. Which marketing strategies would offer the best ways to meet those goals?
- I would need to make sure the site is optimised for SEO for prominent search rankings.
- Keep active on social media channels posting regular content and help promote offers.
- Engage with usrs on social media and get feedback from customers.

7. Would your business have a budget to spend on advertising? Or would it need to work with free or low cost options to market itself?
- For the fist year I would need to carefully keep spending low in order to generate revenue. 
- After collecting sales and web statistics, I can see where investements need to be made in order to build on the business goals.

[Back to contents](#contents)

## Content Marketing
The main focus is the product content making sure the product page is attractive and gives the customer what the need to see and know in a short timeframe.

![image](/documentation/web_marketing/marketing_product.png)

## Social Media Marketing
Facebook is currently the most popular social media channel so creating a Facebook business page allows me to target and engage with a wide audience. I can also grow my Elite Ride community, building brand loyalty and trust. I can chat with customers, get customer feedback on a paltform that is free/low cost. 

![image](/documentation/web_marketing/elite-rides-fb-business-page.png)

## Email Marketing
Customers can sign up to `Elite Rides Email Marketing` by providing there email address.
Here I am using MailChimp to `capture the Customer emails` and `manage the subscibers via the MailChimp admin`.
<br>

![image](/documentation/features/newsletter_signup_mailchimp.png)

![image](/documentation/manifestations_of_data/data_at_rest_newsletter_subscribe.png)

[Back to contents](#contents)

# Agile Project Management
I used Jira Project Tracking Software to manage the backlog for the project.
Jira Software is an agile project management tool that supports any agile methodology, be it scrum, kanban, or your own unique flavor. I was able to plan, track, and manage the whole project in Jira.

I tested against the Acceptance Criteria in the Jira User Stories.

[Go to Jira](https://krishangharu.atlassian.net/jira/software/projects/ER/boards/2)

[Back to contents](#contents)

# Strip Integration

## Testing Stripe
Stipe is set up in Developer Mode. This means you can use Stripe Test payments to simulate a live purchase on the store.

- [Stripe Test Cards here](https://stripe.com/docs/testing?locale=en-GB&testing-method=card-numbers#cards)

Note: You can use test cards from any country, but if you want to test UK cards then use these:

| Country | Number | Brand | Date | CVC | Postcode |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| United Kingdom (GB) | 4000008260000000 | Visa | Any future date | Any 3 digits | UK Postcode
| United Kingdom (GB) | 4000058260000005 | Visa (debit) | Any future date | Any 3 digits | UK Postcode
| United Kingdom (GB) | 5555558265554449 | Mastercard | Any future date | Any 3 digits | UK Postcode

## Injecting Stripe

In the base template, I'll add Stripe js script in the corejs block, eventhough I only technically need it on the checkout page.
Stripe recommends putting it in the base template so it'll be available on every page of the site
which allows some of their more `advanced fraud detection features` to work.
<br>

![image](/documentation/stripe/stripe_js_script.png)

## Get Stripe working in Gitpod
As I was using Gitpod, I had to make the Stripe keys permanent to the workspaces page. Othwerwise I would have to keep adding them all the time if I had to create a new workspace.
I did this by clicking your account icon in the upper right > go to settings > entering them there under the environment variables section.
<br>

## Stripe Handle Form Submission
Before we call out to Stripe, we'll want to disable both the card element and the submit button to prevent multiple submissions.
<br>

![image](/documentation/stripe/stipe_handle_form_submission.png)

## Stripe Webhooks
I setup Webhooks in Stripe to help capture the payment intent, in case the Customer somehow intentionally or accidentally closes the browser window after the payment is confirmed but before the form is submitted.
<br>

Each time an event occurs on Stripe such as a payment intent being created, a payment being completed and so on, Stripe sends out what's called a Webhook we can listen for.
Webhooks are like the signals django sends each time a model is saved or deleted.
Except that they're sent securely from Stripe to a checkout URL specified.
<br>

The Admin can then verify that the purchase was made successfully in Stripe, eventhough the order was not captured in the Database. The Admin can then manually create the order on behalf of the Customer knowing that they paid for it.
<br>

![image](/documentation/stripe/stripe_webhooks.png)

[Back to contents](#contents)

# Accessibility

I’ve added ARIA attributes to buttons and game sections. This is to help disabled users understand what the different are and their purpose. 

I’ve used Symantic HTML markup which helps browsers to understand the context of the content, and also helps with the accessibility for users with impairments.

I’ve used `aria-label` attributes on buttons and sections of the game to explain what they are.

[Back to contents](#contents)

# Performance

## Google Lighthouse Score

- Mobile

![image](/documentation/lighthouse_tests/google_lighthouse_mobile.png)

<br>

- Desktop

![image](/documentation/lighthouse_tests/google_lighthouse_desktop.png)

## Microsoft Edge Lighthouse score

- Mobile

![image](/documentation/lighthouse_tests/microsoft_edge_lighthouse_mobile.png)

<br>

- Desktop

![image](/documentation/lighthouse_tests/microsoft_edge_lighthouse_desktop.png)

[Back to contents](#contents)

# HTML and CSS Code Validation
Both the W3C Markup HTML Validator and W3C CSS Validator were used to confirm there are no errors in the codebase.

[Back to contents](#contents)

# Technologies used

## Languages
    
+ [Python 3.8.5](https://www.python.org/downloads/release/python-385/): is the main language used to build the back-end.
+ [JS](https://www.javascript.com/): for the Stripe elements.
+ [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): is markup language used to build the front-end templates.
+ [CSS](https://developer.mozilla.org/en-US/docs/Web/css): is styling language used adjust layout and front-end styles.
+ [Bulma](https://www.javascript.com/): I've used the `.icon` class from another CSS framework similar to bootstrap called Bulma. This helps ensure that whenever I use font awesome icons,
they will always stay perfectly centred, and have a consistent size unless I manually change it.

[Back to contents](#contents)

## Frameworks and libraries

+ [Django](https://www.djangoproject.com/): A high-level Python web framework for the app.
+ [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/overview.html): is an integrated set of Django applications dealing with account authentication, registration and management.
+ [CrispyForms](https://django-crispy-forms.readthedocs.io/): An optimised way of rendering forms on the front-end in a very elegant and `DRY` way. 
+ [Summernote](https://summernote.org/): A JavaScript library that helps you create WYSIWYG editors online. Used in the Django Admin under Products to `enrich product descriptions`.
+ [Pillow](https://pypi.org/project/Pillow/9.3.0/): To manipulate and process images, Pillow provides tools that are similar to ones found in image processing software such as Photoshop.

[Back to contents](#contents)

## Databases

+ [SQLite3](https://sqlite.org/index.html): Local DBMS (Database Management System) to use in Gitpod to store all data.
+ [PostgreSQL by ElephantSQL](https://www.elephantsql.com/): Production DBMS (Database Management System) to store all data on the live site.

[Back to contents](#contents)

## Other tools

+ [Github](https://github.com/): hosting service for software development and version control using Git.
+ [Pip3](https://pypi.org/project/pip/): is the package manager to intstall Python modules and libraries.
+ [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/): "Green Unicorn" is a Python Web Server Gateway to translate HTTP Rquests for Python to understand.
+ [Spycopg2](https://pypi.org/project/psycopg2/): PostgreSQL database adapter so I can manage the Database in Python. 
+ [Heroku](https://dashboard.heroku.com/): the hosting service to host the app.
+ [VSCode](https://code.visualstudio.com/): the IDE used to program the app.
+ [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): used to identify any errors when being rendered in the browser.
+ [Font Awesome](https://fontawesome.com/): used to source social icons to be used on the app.
+ [Lucid.app](https://lucid.app/) used to create the Database schema and Dataflow Diagram.
+ [W3C Validator](https://validator.w3.org/): used to validate HTML5 code.
+ [W3C CSS validator](https://jigsaw.w3.org/css-validator/): used to validate CSS code.
+ [flake8](https://pypi.org/project/flake8/): was used to validate Python code.
+ [Replit.com](https://replit.com/): to store versions of work-in-progress snippets and functions of code.

[Back to contents](#contents)

# Information Architecture

## Entity-Relationship Diagram

* The Database schema was created using [Lucid.app](https://lucid.app/).

![Database Schema](/documentation/erd/EliteRides_Schema.jpeg)

[Back to contents](#contents)

# Deployments and Database Setup
The database I have been using while building Elite Rides in Gitpod is only accessible within Gitpod. The deployed site on Heroku will not be able to access it. So, I had to create a new database that can be accessed by my Heroku app. 

## Creating an external database using ElephantSQL

1. Log in to ElephantSQL.com to access your dashboard
2. Click “Create New Instance”
3. Set up your plan
    - Give your plan a Name (this is commonly the name of the project)
    - Select the Tiny Turtle (Free) plan
    - You can leave the Tags field blank
4. Select “Select Region”
5. Select the nearest data center to me.
6. Then click “Review”
7. Check your details are correct and then click “Create instance”
8. Return to the ElephantSQL dashboard and click on the database instance name for this project
9. In the URL section, clicking the copy icon will copy the database URL to your clipboard

## Create a Heroku app to connect to the new database

1. In Heroku, I clicked New to create a new app
2. Gave the app a name and selected the region closest to me. The I clicked Create app to confirm.
3. Open the Settings tab
4. Under Config Var i added `DATABASE_URL`, and for the value, copied in the `new database url` from ElephantSQL.

## Set up the project to connect to new ElephantSQL database

1. In Gitpod terminal, I installed `dj_database_url` and `psycopg2`, both of these are needed to connect to your external database.
2. I updated the requirements.txt file with the newly installed packages
`pip freeze > requirements.txt`
3. In the settings.py file, I imported dj_database_url underneath the import for os
```python
import os
import dj_database_url
```
4. In settings.py, at the DATABASES section, I updated it to the following code, so that the original connection to sqlite3 is commented out and I connect to the new ElephantSQL database instead. I pasted in the ElephantSQL database URL in the position indicated.
 ```python
 # DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #     }
 # }
     
 DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
 ```
5. In the terminal, I ran the showmigrations command to confirm I'm connected to the external database `python3 manage.py showmigrations`
6. I migrated the database models to the new database `python3 manage.py migrate`
7. I had to create a new superuser for your new database `python3 manage.py createsuperuser`


## Confirm that the data was migrated to ElephantSQL database
1. On the ElephantSQL page for your database, in the left side navigation, select “BROWSER”
2. Click the Table queries button, select `auth_user`
3. When I clicked “Execute”, I should see the newly created superuser details displayed. This confirms the data tables have been created, and I can add data to the external database.


## Deployment to Github

`$ git add .` - Adding this to the editor terminal commits all the latest file changes.
The period (.) at the end is what adds all files to the commit.

`$ git commit -m “{Commit Details}”` - Pushes the latest changes to the GIT Repository.
`-m` means "message" which is common practice to add so you and other developers know what changes were being made.


## Deployment to Production

Once I verified and tested by changes, I then deploy thr changes to Production.

`$ git push` deploys the code to the GitHub and into the main branch of code which is connected to Production (the Live Public URL).

## Heroku Deployment
1. To prevent exposing the database when I push to GitHub, I deleted it again from my settings.py. I used an if statement so that when our app is running on Heroku where the database URL environment variable will be defined, we connect to Postgres. Otherwise we connect to SQLite when working locally in Gitpod. 
If database URL is in os.environ I'll get its value using dj_database_url.parse and use that as my database setting; otherwise, I'll use the default configuration.
```python
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

2. To now make my deployments to work on the first try, I need to install gunicorn, which will act as our webserver `pip3 install gunicorn`, and freeze that into our requirements.txt file.
3. I created the `Procfile` at root directory level to tell Heroku to create a web dyno which will run gunicorn and serve my Django app.
4. I need to temporarily disable collectstatic by using
`heroku config:set DISALBE-COLLECTSTATIC=1` so that Heroku won't try to collect staticfiles when I deploy.
5. I need to add the hostname of our Heroku app to ALLOWED_HOSTS in settings.py I also added `localhost` in here so that Gitpod will still work too.
```python
ALLOWED_HOSTS = ['pp5-elite-rides.herokuapp.com', 'localhost']
```
6. I need to create a new secret key for the Heroko app and add it to the Congif Vars in Heroku.
7. I setup `automatic deployments to Heroku` so when I `$ git push` to Github, I also deploy to Heroku at the same time.

![image](/documentation/deployment/heroku_automatic_deployment_setup.png)

## Final Deployment Process

* Set DEBUG=False in settings.py.
* Delete DISABLE_COLLECTSTATIC from Config Vars in Heroku.
* Commit and push the changes to GitHub which deploys to Heroku.

[Back to contents](#contents)

# Use of env.py
I've used the env.py to store secret keys and other senstive environment varaibles.
This ensures that the project secret keys and variables are safe and out of version control, and not stored in Github.

[Back to contents](#contents)

# Amazon Web Services S3
I need a place to store our static files and images. For this, I'm using `Amazon Web Services s3` which is a `cloud-based storage service` that gives us a small piece of Amazon's infrastructure that I can use to store static files.

## Amazon - Identify and Access Management (IAM)
After setting up the s3 bucket, I have to create a user to access it.
I did this through another service called `IAM` which stands for `Identity and Access Management`.

The process here is first I create a group for our user to live in.
Then create an access policy giving the group access to the s3 bucket we created.
And finally, assign the user to the group so it can use the policy to access all our files.

## AWS Config Vars
In settings.py I added a key `USE_AWS` which is set to true.
This is so thr settings file knows to use the AWS configuration when we deploy to Heroku.

## AWS Cache Control
I added another setting to settings.py called `AWS_S3_OBJECT_PARAMETERS`.
This will tell the browser that it's okay to cache static files for a long time

[Back to contents](#contents)

# Credits and Borrowed Resources

## BootStrap Support
- [Carousel](https://getbootstrap.com/docs/4.0/components/carousel/)
- [Pop up Modal](https://getbootstrap.com/docs/4.6/components/modal/)
- [Accordion](https://getbootstrap.com/docs/4.6/components/collapse/#accordion-example)
- [Responsive Layout](https://getbootstrap.com/docs/4.0/layout/grid/)

## Project Support
- [Django admin how to show currency numbers in comma separated format](https://stackoverflow.com/questions/73514339/django-admin-how-to-show-currency-numbers-in-comma-separated-format)
- [What Is a Positional Argument in Python](https://www.codingem.com/what-is-a-positional-argument-in-python/)
- [Python Docstrings](https://www.programiz.com/python-programming/docstrings)
- [Python round() Function](https://www.w3schools.com/python/ref_func_round.asp)
- [How should I format a long url in a python comment and still be PEP8 compliant](https://stackoverflow.com/questions/10739843/how-should-i-format-a-long-url-in-a-python-comment-and-still-be-pep8-compliant/25034769)
- [Build a Contact Form in Python Django](https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid)
- [Integrating Summernote WYSIWYG Editor in Django ](https://djangocentral.com/integrating-summernote-in-django/)
- [Colour Pallete](https://www.color-hex.com/color-palette/2286)
- [What is CAPTCHA](https://support.google.com/a/answer/1217728?hl=en#:~:text=CAPTCHA%20offers%20protection%20from%20remote,must%20to%20pass%20the%20test.)
- [How to auto close an alert after few seconds with Bootstrap?](https://stackoverflow.com/questions/68165290/how-to-auto-close-an-alert-after-few-seconds-with-bootstrap)
- [Bootstrap Modal](https://getbootstrap.com/docs/4.6/components/modal/)
- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
- [Favicon](https://upload.wikimedia.org/wikipedia/commons/b/b8/ER_logo.svg) 
- [Sitemap.xml](https://www.xml-sitemaps.com/)
- Insipred by the `Boutique Ado` Walkthrough Project.
- Special thanks to CI Tutor Support for their support and guidance.

## E-commerce User Stories Support
- [AllAuth](https://www.digitalocean.com/community/tutorials/how-to-authenticate-django-apps-using-django-allauth)
- [Website Footer](https://blog.hubspot.com/website/website-footer)
- [Product Detail Page](https://business.adobe.com/blog/basics/learn-about-product-detail-pages)
- [Website Navigation](https://www.bigcommerce.co.uk/ecommerce-answers/what-website-navigation-and-how-does-it-impact-ecommerce/)
- [Product Categorisation](https://www.comalytics.com/e-commerce-product-categorisation-a-how-to-guide/)
- [Mini Cart](https://agenciaeplus.com.br/en/mini-cart-o-que-e-e-qual-sua-utilidade-no-e-commerce/)
- [Cart Page](https://www.omniconvert.com/what-is/cart-page/)
- [Checkout Page](https://www.bolt.com/thinkshop/checkout-page-best-practices-templates-examples-to-end-abandonment)
- [About Us](https://www.searchenginejournal.com/about-us-page-examples/250967/)
- [Privacy Policy](https://blog.shift4shop.com/why-all-websites-need-a-privacy-policy-and-how-to-create-one)
- [Cookie Policy](https://www.termsfeed.com/blog/sample-cookies-policy-template/)
- [Contact Form](https://support.bigcommerce.com/s/article/Creating-a-Contact-Form?language=en_US)
- [Product Listing Page](https://www.dynamicyield.com/glossary/product-listing-pages-plps/#:~:text=What%20is%20a%20product%20listing,pages%20and%20closer%20to%20conversion)
- [Filter and Sorting](https://inviqa.com/blog/filter-and-sort-improving-ecommerce-product-findability)
- [Code Refactoring](https://www.altexsoft.com/blog/engineering/code-refactoring-best-practices-when-and-when-not-to-do-it/)

## Static Content and Copy
- [model-car-world.co.uk](https://www.model-car-world.co.uk/)
- [carmodel.com](https://www.carmodel.com/)
- [Hero Image](https://pixabay.com/photos/diecast-model-toys-car-lamborghini-6001104/)

## Product Details and Images
- [carmodel.com](https://www.carmodel.com/)

## Mind Map images
- [rosewe.com](https://www.rosewe.com/images/201905/source_img/222314_P_15587932650450.jpg)
- [Wikipedia - Sillitoe Tartan black and white.svg](https://upload.wikimedia.org/wikipedia/commons/0/0f/Sillitoe_Tartan_black_and_white.svg)
- [goodhousekeeping.com](https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/black-and-white-bedroom-rinfret-limited-1611167676.jpg?crop=0.668xw:1.00xh;0.0238xw,0&resize=768:*)
- [clipart-library.com](http://clipart-library.com/images/8cEbRBjxi.jpg)

## Web and Social Media Marketing
- [MailChimp Newsletter Sign Up](https://mailchimp.com/)
- [Facebook Business Page](https://www.facebook.com/)

[Back to contents](#contents)

# Bugs Encountered during Testing

## Bug 1
I realised that on the checkout success page, the grand total is calculating a little less.

For example, when I add a product with shipping cost, the Grand Total should be `£14.25` but shows on the checkout success page as `£14.24`

Order Total £12.95
Delivery £1.30
Grand Total should be £14.25

![image](/documentation/bugs/1_bug_shopping_bag.png)

![image](/documentation/bugs/1_bug_checkout_success.png)

The issue was in `Checkout App > models.py` where I need to add a `round() funtion` to the grand_total and output the price with 2 decimal places.

![image](/documentation/bugs/1_bug_fix.png)

## Bug 2

When I try to remove an item from my bag, nothing happens.
I checked the browser console and saw a 403 error.

![image](/documentation/bugs/2_bug_403_error.png)

In the `Bag App > bag.html` I removed the csrfToken from `var = data` by accident as I wanted to remove the size reference.

![image](/documentation/bugs/2_bug_403_fix.png)

[Back to contents](#contents)

# Future Features
1. Product Reviews
2. CAPTCHA on the Contact Us form.
3. Optimised My Profile section.
4. Display Sale Price.
5. Promo Code at Checkout.
6. Alternative payment methods (PayPal, Amazon Pay).
7. Customer Control over Marking Channel Opt In - GDPR Compliance

[Back to contents](#contents)

---

<h2 align="center">End of Readme</h2>