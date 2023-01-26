<h1 align="center">Elite Rides</h1>

[Elite Rides](https://pp5-elite-rides.herokuapp.com/) is an E-commerce store that specialises in die-cast models of luxury, high-end cars. As a Customer you are able to purchase a product and set up and online account. Guest checkout is also available. As the Store Admin, you can login from the store-front and edit the product details, and delele products too.
Elite Rides is responsive which makes shopping possible on mobile and table devices. 

[Visit the website](https://pp5-elite-rides.herokuapp.com/)

![image](/documentation/iamreposonsive_image.png)

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

## Header:
- Cream background.
- Dark Green Text.
- Hover States: Underline style.

  - Example:
  <br>
![image](/documentation/readme_folder/images/header.png)

## Footer:
- Brown background.
- Dark Green text.
- Crean Icon.

  - Example:
  <br>
![image](/documentation/readme_folder/images/footer.png)

[Back to contents](#contents)

## Colour Palette:

![image](/documentation/readme_folder/images/colour_pallete.png)


# Manifestations of Data

## Data at rest

- Appointment Data in the Admin
<br>
![image](/documentation/readme_folder/images/data_at_rest_appointments.png)
<br>
- Teacher in the Admin
<br>
![image](/documentation/readme_folder/images/data_at_rest_teachers.png)

## Data in motion

1. Data is `captured` from the appointment form and `stored` in the database.
<br>
![image](/documentation/readme_folder/images/data_in_motion_appointment_form.png)
![image](/documentation/readme_folder/images/data_in_motion_admin.png)
<br>

2. An `email` is sent to the `User` when a appointment is accepted by the `Admin`
<br>
![image](/documentation/readme_folder/images/data_in_motion_email.png)

## Data in use

Appointment Data is `accessed` when the Teacher `Admin` logs into the Teacher Admin area.

![image](/documentation/readme_folder/images/data_in_use_manage_appointment.png)


# The Surface Plane:

## **Mobile First Design**

![Image](/documentation/readme_folder/images/mobile_first_design.png)

---

# Features

## **Navbar**

![Navbar](/documentation/readme_folder/images/navbar_desktop.png)
![Navbar](/documentation/readme_folder/images/navbar_mobile.png)

Navbar links:
- Home Page (School Logo) 
- Make Appointment
- Teacher Admin

To satisfy an MPV and keeping the Navbar simple allows Users to become familiar with the app more quickly.

## **CRUD Create - Make an Appointment includes Django Simple Captcha**

### [Go to page](https://kslg-appointment-app.herokuapp.com/make-an-appointment/)
<br>

![Image](/documentation/readme_folder/images/appointment_form_feature.png)

## **CRUD Read - Manage Appointment**

### [Go to page](https://kslg-appointment-app.herokuapp.com/accounts/login/?next=/manage-appointments/)
<br>

![Image](/documentation/readme_folder/images/crud_read_feature.png)

## **CRUD Update - Manage Appointment**

### [Go to page](https://kslg-appointment-app.herokuapp.com/accounts/login/?next=/manage-appointments/)
<br>

![Image](/documentation/readme_folder/images/crud_update_feature.png)

## **CRUD Delete - Manage Appointment with Defensive Programming**

### [Go to page](https://kslg-appointment-app.herokuapp.com/accounts/login/?next=/manage-appointments/)
<br>

![Image](/documentation/readme_folder/images/crud_delete_feature.png)

## **Sign up page**

### [Go to page](https://kslg-appointment-app.herokuapp.com/accounts/login/)
<br>

![Image](/documentation/readme_folder/images/login_feature.png)

## **Register page**

**NOTE: THIS IS NOT A PUBLIC PAGE - Made for Super Admins to share the link with Teacher Admins**

### [Go to page](https://kslg-appointment-app.herokuapp.com/accounts/signup/)
<br>

![Image](/documentation/readme_folder/images/signup_feature.png)

## **Email Confirmation**

**Sent to the `User` when `Admin` accepts the appointment.**

![Image](/documentation/readme_folder/images/email_confirmation_feature.png)


## **Bootstrap Theme**

### [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

## **Bootstrap Alert Messages**

### **Succes Alert with Appointment has been created**
![Image](/documentation/readme_folder/images/alert_success_appointment_feature.png)

### **Warning Alert when Captcha is invalid**
![Image](/documentation/readme_folder/images/alert_invalid_capthca_feature.png)

### **Success Alert when you login and register**
![Image](/documentation/readme_folder/images/alert_success_login_feature.png)

### **Success Alert when you delete an Appointment**
![Image](/documentation/readme_folder/images/alert_success_appointment_delete_feature.png)

### **Success Alert when you logout**
![Image](/documentation/readme_folder/images/alert_success_logout_feature.png)


## **Time Slot selector on Appointment form**

```Python
  # Time slot options
  TIME_SLOTS = (
      ('0', '15:30 - 15:45'),
      ('1', '15:45 - 16:00'),
      ('2', '16:00 - 16:15'),
      ('3', '16:15 - 16:30'),
      ('4', '16:30 - 16:45'),
      ('5', '16:45 - 17:00'),
  )
```

## **Teacher Dropdown Selector**

**Note:** on_delete CASCADE option not needed as Teachers still exist if an appointment is deleted.

```Python
class Teacher(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
```

## **Date Picker on Make Appointment Page**

```Python
# Date Picker for the Appointment form
class DateInput(forms.DateInput):
    input_type = 'date'
```


[Back to contents](#contents)

---

# User Journeys and Manual Testing

***Testing against the Acceptance Criteria in the User Stories.*

| Journey   | Result |
|-------------|-------------------------------------|
| 1. As a **User** and **Admin** I want **to see a responsive design that can be used to adapt screen sizes** So that **I have a consistent user experience no matter where and how I use the app.** | `PASS`
|2. As a **User** I need **to verify myself as a human user and not a bot** so that **I can successfully submit an appointment** | `PASS`
|6. As a **User** AND **Admin** I can **Create a new appointment** so that **the appointment data is stored in the database.** | `PASS`
|4. As a **User** and **Admin** I can **see notifications messages on the front-end** so that **I know what what is happening or what has happened**)| `PASS`
|5. As a **Teacher Admin** I need to **login to the Teacher Admin Area with a user name and password** so that **I can access the appointment data**| `PASS`
|6. As a **User** I cannot **login to the Teacher Admin Area** so that **I can access the appointment data**| `PASS`
|7. As a **User** I cannot **signup as a Teacher Admin** so that **I can access the appointment data**| `PASS`
|8. As an **Admin** I want to **be notified that I have signed out from the admin** So that **I know I have signed out when working on a shared device.**| `PASS`
|9. As an **Admin** I can **view appointments in the admin area** so that **I can review and edit the appointments.**| `PASS`
|10. As an **Admin** I can **update the appointment record** by **accepting an appointment**| `PASS`
|11. When I **Accept an appointment** I expect **the accepted status attribute to be updated for the appointment record in the database**| `PASS`
|12. As an **Admin** I can **delete the appointment record** so that **the appointment record is removed from the database.**| `PASS`
|13. As a **Admin** I can **click accept on the appointment which send an email confirmation to the user** so that **the User is notified that the appointment is confirmed.**| `PASS`
|14. As a **Teacher Admin** wanting to **Delete an appointment, I can see the Modal Pop up asking me to confirm if I want to Delete** so that **the appointment is not deleted by accident.**| `PASS`


# Agile Project Management

## **User Stories - User**

| Issue ID    | User Story |
|-------------|-------------------------------------|
|[#1](https://github.com/kslg/appointment-app/issues/1)| User Story: Install Bootstrap 4 Theme
|[#2](https://github.com/kslg/appointment-app/issues/24)| User Story: Django Simple CAPTCHA
|[#3](https://github.com/kslg/appointment-app/issues/6)| User Story: CRUD - CREATE Functionality
|[#4](https://github.com/kslg/appointment-app/issues/9)| User Story: Add Bootstrap Alert Messages  
|[#5](https://github.com/kslg/appointment-app/issues/10)| User Story: Role Based Login and Registration Functionality
|[#6](https://github.com/kslg/appointment-app/issues/11)| User Story: Restrict User Access to Teacher Admin Area

## **User Stories - Teacher Admin**

| Issue ID    | User Story |
|-------------|-------------------------------------|
|[#1](https://github.com/kslg/appointment-app/issues/23)| User Story: Sign Out Success Message
|[#2](https://github.com/kslg/appointment-app/issues/5)| User Story: CRUD - READ Functionality
|[#3](https://github.com/kslg/appointment-app/issues/7)| User Story: CRUD - UPDATE Functionality
|[#4](https://github.com/kslg/appointment-app/issues/8)| User Story: CRUD - DELETE Functionality
|[#5](https://github.com/kslg/appointment-app/issues/14)| User Story: Send Email to Parent when appointment is Approved. django.core.mail module.
|[#6](https://github.com/kslg/appointment-app/issues/9)| User Story: Add Bootstrap Alert Messages 
|[#7](https://github.com/kslg/appointment-app/issues/22)| User Story: Delete Appointment - Defensive Programming with Bootstrap Modal
|[#8](https://github.com/kslg/appointment-app/issues/10)| User Story: Role Based Login and Registration Functionality

## **Tasks**

| Issue ID    | Tasks |
|-------------|-------------------------------------|
|[#1](https://github.com/kslg/appointment-app/issues/4)| Task: Create Appointment Model
|[#2](https://github.com/kslg/appointment-app/issues/17)| Task: Update Login, Signup and Log out pages with Bootstrap and Crispy forms.  
|[#3](https://github.com/kslg/appointment-app/issues/3)| Task: Install Django and start up libraries

## **Bugs and Issues**

| Issue ID | Bugs / Issues |
|----------|--------------------------------------------------------------------------|
|[#1](https://github.com/kslg/appointment-app/issues/25)| Issue: Trying to set up email sending via gmail
|[#2](https://github.com/kslg/appointment-app/issues/26)| Issue: Seeing this error when I click the delete button on the appointment
|[#3](https://github.com/kslg/appointment-app/issues/27)| Issue: I cannot get the appointment to delete from the pop up modal
|[#4](https://github.com/kslg/appointment-app/issues/28)| Issue: CAPTCHA Alert not showing as Warning Alert
|[#5](https://github.com/kslg/appointment-app/issues/29)| Issue: Success Alert Message not showing when admin logs out
|[#6](https://github.com/kslg/appointment-app/issues/13)| BUG: Styling on Manage Appointment Cards
|[#7](https://github.com/kslg/appointment-app/issues/19)| BUG: Fix padding issue on Account pages (Login, Sign out)
|[#8](https://github.com/kslg/appointment-app/issues/12)| BUG: Mobile View - Burger Menu does not show Nav Links
|[#9](https://github.com/kslg/appointment-app/issues/18)| BUG: Fix Bootstrap errors seen in the browser console
|[#10](https://github.com/kslg/appointment-app/issues/16)| BUG: Sign Out message showing on appointment page. Needs to show on redirect page.



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
    + [Django Simple Captcha](https://pypi.org/project/django-simple-captcha/): is a simple captcha form to prevent automated bot attacks.
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
    + [pycodestyle 2.9.1](https://pypi.org/project/pycodestyle/): was used to validate Python code.

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