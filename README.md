
This is a migration from an old project that i am re using, i will be updated as the projects is worked on and ref to WatchBidCentral will be changed to PixelPerfect


todo features
must have
404 page - done
seo
social media page
email thanking for signing up for newsletter



might have


wont have
with pillow when have 3 backgrounds that will overlay the poster onto when loading the product detail
carouseld of high rated and sale items
cookie popup
stock item reduced after sale confirmed
rating system so calculates new rating and writes it

main site for inspiration and images displate.com, email send to them on 27/05/24 requesting permission to use site assets

# Pixel Perfect

Pixel Perfect is an exclusive digital haven tailored for the aficionados of game franchises, offering a marketplace that celebrates the art and craft of high-quality posters. This platform is not just a website; it's a dynamic community for both sellers and buyers to engage in the passionate exchange of exquisite game-themed artwork. From vintage classics to contemporary marvels, Pixel Perfect is dedicated to connecting art enthusiasts around the globe.

Here, users can craft listings for their cherished posters, purchase a diverse collection from esteemed artists, and immerse themselves in a realm where creativity meets fandom. Pixel Perfect prides itself on ensuring a secure, transparent, and straightforward experience, making it the premier destination for acquiring and distributing luxury posters.

Embracing the legacy and innovation of game art, Pixel Perfect is a confluence of history, artistry, and technology. It's a community where every design, print, and story behind the artwork matters, offering a unique space for enthusiasts to share, discover, and elevate their passion for game-inspired posters. Join the journey at Pixel Perfect, where every piece is a celebration of artistic expression and gaming culture.

<center> 

![Mockup image](/assets/img/README_images/index.jpg) 

</center>

Developer: [Barry Flynn](https://github.com/barryCFlynn/) <br>
[Live webpage](https://watch-bid-central-95b83adfb641.herokuapp.com/)<br>
[Project Repository](https://github.com/barryCFlynn/WatchBidCentral)<br>

## Badges
![GitHub Badge](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=for-the-badge)
![Gitpod Badge](https://img.shields.io/badge/Gitpod-FFAE33?logo=gitpod&logoColor=fff&style=for-the-badge)
![Git Badge](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff&style=for-the-badge)
![Heroku Badge](https://img.shields.io/badge/Heroku-430098?logo=heroku&logoColor=fff&style=for-the-badge)
![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=fff&style=for-the-badge)

![HTML5 Badge](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=fff&style=for-the-badge)
![CSS3 Badge](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=fff&style=for-the-badge)
![JSS Badge](https://img.shields.io/badge/JSS-F7DF1E?logo=jss&logoColor=000&style=for-the-badge)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)

![Bootstrap Badge](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=fff&style=for-the-badge)
![Django Badge](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=fff&style=for-the-badge)

---

## Table of Content

# Table of Contents

1. [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
2. [User Experience (UX)](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Stories](#user-stories)
3. [Database](#database)
    - [Database Schema Summary](#database-schema-summary)
4. [Design](#design)
    - [Color](#color)
5. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Tools](#tools)
    - [Supporting Libraries and Packages](#supporting-libraries-and-packages)
6. [Methodology](#methodology)
7. [Features](#features)
    - [Login Landing Page](#login-landing-page)
    - [About Us](#about-us)
    - [Create Listing](#create-listing)
    - [Liked Listings](#liked-listings)
    - [My Listings](#my-listings)
    - [Future Features](#future-features)
8. [Testing](#testing)
    - [Automated Testing](#automated-testing)
    - [Manual Testing](#manual-testing)
9. [Bugs](#bugs)
    - [Known Bugs](#known-bugs)
    - [Fixed Bugs](#fixed-bugs)
10. [Deployment](#deployment)
    - [App Deployment](#app-deployment)
    - [Version Control](#version-control)
11. [Credits](#credits)
    - [Django Documentation](#django-documentation)
    - [Bootstrap Docs](#bootstrap-docs)
    - [Media](#media)
    - [Content](#content)
12. [Acknowledgments](#acknowledgments)

---

# Project Goals
Pixel Perfect is a Django-based web application dedicated to game franchise enthusiasts and collectors, offering a sophisticated platform for the buying and selling of high-quality posters. The main goals of the project include:

1. Create a Secure and User-Friendly Marketplace: Develop a platform where users can list their game-themed posters for sale and purchase a diverse range of artwork in a safe and user-friendly environment.

2. Foster a Community of Enthusiasts: Build a community where poster and game art enthusiasts can share their passion, knowledge, and experiences related to various game franchises and artwork styles.

3. Implement a Transparent Verification Process: Ensure the authenticity and quality of posters listed on the platform through a clear and trustworthy verification process.

4. Provide Comprehensive User Profiles: Offer detailed user profiles that allow sellers to showcase their collections and buyers to express their preferences and interests in game-themed art.

5. Enable a Seamless User Experience: Focus on providing a smooth and intuitive user experience from listing posters to making purchases, with an emphasis on high-quality images and detailed descriptions.

### User Goals
- Discover a Wide Selection of Game-Themed Posters: Explore an extensive collection of high-quality posters from reputable sellers and verified listings.
- Find a Specialized Platform: Utilize a platform that caters exclusively to the needs and interests of game franchise enthusiasts and art collectors.
- Safely Buy and Sell Posters: Engage in buying and selling posters within a secure community that values authenticity, quality, and the artistic elements of game franchises.
- Connect with Other Enthusiasts: Connect with fellow users to share insights, exchange knowledge, and discuss the historical and artistic significance of various game-themed artworks.

### Site Owner Goals
- Establish Pixel Perfect as a Premier Destination: Position Pixel Perfect as the leading online platform for buying and selling high-quality game-themed posters, recognized for its commitment to quality, authenticity, and community engagement.
- Create a Sustainable Business Model: Develop a business model that attracts a global audience of game art lovers and collectors, providing them with a reliable platform for their buying and selling needs.
- Continuously Improve the Platform: Enhance the platform based on user feedback and technological advancements, ensuring a state-of-the-art experience for all community members.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# User Experience

### Target Audience
Pixel Perfect is tailored for the following target audience:

- Game franchise enthusiasts and collectors seeking a dedicated platform to buy and sell high-quality game-themed posters.
- Individuals interested in learning about game art and connecting with a community that shares their passion for high-quality game-themed artwork.
- Sellers looking for a trustworthy marketplace to list their game-themed posters and reach a global audience of potential buyers.
- Buyers in search of a secure and user-friendly environment to discover authentic, high-quality game-themed posters from reputable sellers.

### User Requirements and Expectations
When using Pixel Perfect, users can expect the following features and characteristics to fulfill their needs:

- A visually appealing and easy-to-navigate interface that enhances the experience of buying and selling game-themed posters.
- A secure registration and login process, safeguarding user data and transactions.
- Interactive features such as the ability to create listings, purchase posters, and engage with other users through comments and reviews.
- A personalized user profile where sellers can showcase their posters and buyers can manage their purchases and wishlists.
- Access to a curated selection of high-quality game-themed posters, with detailed information and images to ensure authenticity and quality.



### User Stories

User stories and tasks Grouped below.

- [As a Site Admin, I can create, edit, and delete advertisements - complete](https://github.com/barryCFlynn/WatchBidCentral/issues/1)



<br>

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Database
When creating the database structure schema for this project, I utilized the [dbdiagram.io](https://dbdiagram.io/) website. This online tool allowed me to visually design and document the database schema, making it easier to plan and implement the database for the blog application.

<center> 

 <img src="assets/img/README_images/database.jpg" alt="Description" width= 600px> 

</center>

## Database Schema Summary

### `Django User Auth` Table
- Represents the basic user information according to Django's built-in User model.
- Fields: `username`, `email`, `password`.

### `Listing` Table
- Extends the User model to store additional information and personal preferences.
- Fields: `title`, `status`, `slug`, `author`, `manufacturer`, `body`, `created_on`, `updated_on`, `bid_timer`, `price`, `current_bid`, `reserve`, `likes`.

### `Image` Table
- Stores the watch images so that each listing can have mutiple images.
- Fields: `image`

### `Comment` Table
- Stores comments made by users on blog posts.
- Fields: `listing`, `author`, `parent_comment`, `body`, `created_on`.

This database schema outlines the structure for WatchBidCentral, enabling user engagement with watch listings, personalization of user profiles, categorization of watches by manufacturer, and community interaction through bids, comments and likes.

<br>

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---
# Features

### Using Keywords to Enhance Search Functionality
#### Overview
In our inventory system, each inventory item can have a set of keywords associated with it. These keywords play a crucial role in improving the searchability of items, allowing users to quickly find what they are looking for based on specific terms related to the product. Keywords can include various descriptors such as genre, style, color, theme, and other relevant attributes.

How It Works
Keyword Field in Inventory Item Model:
Each inventory item includes a keywords field where multiple keywords can be stored. These keywords are typically comma-separated strings that describe the item in various ways.

User Experience:
Users can enter terms related to their interests or needs into the search bar. The system will then look for these terms within the keywords, name, and description fields of inventory items, providing a comprehensive set of results that are more likely to match user expectations.

Benefits
Improved Search Accuracy: By leveraging keywords, the search functionality becomes more accurate and relevant, as it considers various aspects of an item beyond its name and description.
Enhanced User Experience: Users can find items more easily, making their interaction with the platform more enjoyable and efficient.
Flexible Categorization: Keywords allow for flexible and dynamic categorization of items, which can adapt to various search patterns and user preferences.
Example
For an inventory item representing a poster of a popular game franchise, keywords might include terms like "fantasy", "dragon", "RPG", and "adventure". This allows users searching for any of these terms to find the poster even if these terms are not explicitly mentioned in the item's name or description.

By integrating keywords into the search functionality, we enhance the discoverability of inventory items and provide users with a more powerful and intuitive search experience.

### Discount Notification Feature
#### Overview
The discount notification feature is designed to inform users when a product has sizes available at a discounted price. This feature ensures that customers are aware of any ongoing sales and can take advantage of the reduced prices.

Implementation Details
The feature works by checking if any of the available sizes for an inventory item includes the term "Sale." If a sale size is detected, a message indicating the discount is displayed on the product detail page.

How It Works
Inventory Detail View Update:
The view function inventory_detail is updated to include a check for sale sizes. It iterates through all the sizes of an inventory item and sets a flag (has_sale_size) if any size contains the term "Sale."

Template Update:
The template inventory_detail.html is updated to conditionally display a message if the has_sale_size flag is set. This informs users that a 25% discount is available on any size.

Benefits
Increased Awareness: Customers are immediately informed of any ongoing discounts, which can lead to increased sales.
User-Friendly: The notification is prominently displayed, ensuring that users do not miss out on any potential savings.
By incorporating this feature, the platform enhances user experience and promotes sales by clearly communicating discounts to potential buyers.

# Models

## Models Description

### Size Model
The `Size` model defines various size options for the posters, each with an associated price. This model allows for flexible pricing based on the size of the poster and is a Many to Many field.

- **Fields:**
  - `size`: A character field with choices for 'Small', 'Medium', and 'Large'.
  - `price`: A decimal field that stores the price for each size option.

### Product Model
The `Product` model represents individual posters in the inventory. This model includes comprehensive details about each product and utilizes a `ManyToManyField` to link to multiple `Size` entries. This setup enables each product to have various size and price options.

- **Fields:**
  - `title`: The name of the product.
  - `description`: A detailed description of the product.
  - `artist`: The name of the artist who created the poster.
  - `rating`: A decimal field to store product ratings.
  - `keywords`: A text field for comma-separated keywords to facilitate search functionality.
  - `category`: A foreign key linking to the `Category` model.
  - `franchise`: A foreign key linking to the `Franchise` model.
  - `sizes`: A many-to-many field linking to the `Size` model, allowing for multiple size and price options per product.
  - `stock`: The quantity of the product available in stock.
  - `available`: A boolean field indicating if the product is available for sale.
  - `created`: The timestamp when the product was created.
  - `updated`: The timestamp when the product was last updated.
  - `image`: An image field to store the product image.

This structure provides a robust framework for managing the inventory, supporting detailed product information, and flexible pricing based on size.

<br>

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Design

The design of WatchBidCentral is meticulously crafted to resonate with the sophistication and elegance associated with luxury watches. The choice of colors, fonts, and layout are carefully selected to provide an upscale and professional feel, inviting users into a world of high-end watch collecting. The interface combines modern design principles with intuitive navigation, ensuring that both seasoned collectors and new enthusiasts can easily explore, bid, and list watches. The design aims to evoke trust and reliability, mirroring the quality and authenticity of the timepieces featured on the platform.

### Color

For colour the template I used "https://startbootstrap.com/template/shop-homepage" had a very simple colour scheme that I opted to not chnang:


Primary Background Colour

 ![#FFFFFF](https://placehold.it/150x40/FFFFFF/000000?text=FFFFFF)

Secondary Background Colour

![#212529](https://placehold.it/150x40/212529/FFFFFF?text=212529)



Contrast Grid - Only AA and AAA options used.

 <img src="assets\img\README_images\contrast grid.jpg" alt="Description" width= 600px>

#### Before User Logs In:

- **Home Page Featuring Top Listings:** Users land on a dynamic homepage that highlights the most liked and recent watch listings. The page features a sleek, modern design with high-quality images of watches, inviting users to explore the offerings. Navigation is streamlined through a top menu bar that includes links to various site sections, including 'Sell Your Watch,' 'Top Liked Watches,' and 'About Us.' For new visitors, clear calls to action for registration or login are prominently placed, ensuring easy access to the platform's full features.

- **About Us:** This page provides insightful information about the platform, its mission, and what new members can expect upon joining. It serves as an introduction to the site's ethos, focusing on creating a secure and user-friendly environment for watch enthusiasts and collectors to buy and sell luxury watches.

- **Register:** The 'Register' page invites new users to easily register, unlocking access to exclusive site features such as creating their own watch listings and managing their collections through 'My Listings'. This step is the gateway to actively participating in the watch enthusiast community, allowing users to buy, sell, and connect with others who share their passion.


#### After User Logs In:

Post-login, users gain access to a range of interactive and personalized features:

- **Create Listings:** A cornerstone feature of the platform, the 'Create Listings' page empowers users to become sellers in their own right. Here, members can list their watches for sale, providing detailed descriptions, setting prices, and uploading high-quality images to showcase their timepieces. This user-friendly interface is designed to guide sellers through the listing process, ensuring that each watch is presented in the best possible light to potential buyers. Whether you're a seasoned collector or looking to sell a single cherished piece, this feature makes it straightforward to connect with interested parties.


- **View My Listings:** Designed for user convenience, the 'View My Listings' page is a personalized dashboard where sellers can manage their active listings. This section allows users to track the status of each watch they have put up for sale, including current bids, and direct messages from interested buyers. It's a central hub for all selling activities, offering tools to edit listings, update prices, or remove items if necessary. This feature ensures sellers have full control over their sales process, making it easy to manage their offerings in a structured and efficient manner.


- **Edit Your Listings:** The 'Edit Your Listings' feature provides sellers with the flexibility to update their watch listings at any time. Whether it's adjusting the price, updating the description, or adding new images, sellers can ensure their listings are always accurate and appealing. This section is accessible directly from the 'View My Listings' dashboard, offering an intuitive interface for making changes. By supporting ongoing adjustments, this feature empowers sellers to respond to market demand, feedback from potential buyers, or changes in the condition or availability of their watches, maintaining the relevance and attractiveness of their offerings.


- **Delete Your Listing:** This functionality allows sellers to remove their watch listings from the platform with ease. Whether the watch has been sold, withdrawn from sale, or for any other reason, sellers can quickly and securely delete their listings from their 'View My Listings' dashboard. This ensures that the platform remains up-to-date with only available watches being displayed, enhancing the buying experience for potential buyers. The deletion process is designed to be straightforward, with confirmation prompts to prevent accidental deletions, ensuring that sellers have full control over their listings on the site.


- **Comment:** The comment feature enhances the interactive experience on the platform, allowing users to engage with listings in a meaningful way. Whether you're interested in learning more about a watch, seeking further details from the seller, or simply want to express admiration for a particular timepiece, the comment section is your space to communicate. This feature fosters a community atmosphere, enabling users to share insights, ask questions, and offer feedback directly on the listing page. It's an invaluable tool for both buyers and sellers to interact, clarify details, and build connections within the watch enthusiast community.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Technologies Used

### Languages
- HTML
- CSS
- Python
- JavaScript

### Frameworks
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design, used for building the Culture Club web application.
- **Crispy Forms**: A Django package that simplifies form layout and styling, making forms more efficient and customizable.
- **Bootstrap v5.0**: The latest version of the popular CSS framework, used for creating responsive and visually appealing user interfaces.

### Database
- **ElephantSQL**: A cloud-hosted PostgreSQL database service, offering a reliable and scalable storage solution for the application's data.

### Media Management Platform
- **Cloudinary**: A cloud-based platform for media upload, storage, optimization, and delivery, used for managing images in the Culture Club project.

### Tools
- **Git**: A version control system for tracking changes in source code during software development.
- **GitHub**: A platform for hosting and managing Git repositories, enabling collaboration and version control for the project's codebase.
- **Gitpod**: A cloud-based IDE that provides a consistent and pre-configured development environment for the Culture Club project.
- **Heroku**: A cloud application platform used for deploying and hosting the Culture Club web application.
- **Adobe Photoshop**: A graphic design software used for editing and refining images for the website.
- **DB Diagram**: A tool for visualizing and creating database schemas, used for planning the database structure of Culture Club.
- **Google Fonts**: A library of free, open-source fonts, used to enhance typography on the website.
- **Font Awesome**: A library of icons and social logos, used for adding graphical elements to the Culture Club interface.
- **ChatGPT**: An AI to help troubleshoot issues.

### Supporting Libraries and Packages

- `asgiref==3.7.2`: foundational package for Django to support asynchronous web protocols like WebSockets.
- `cloudinary==1.36.0`: integration library for Cloudinary - cloud service for storing and managing media files and assets.
- `dj-database-url==0.5.0`: utility to help you configure your Django application's database from the DATABASE_URL environment variable.
- `dj3-cloudinary-storage==0.0.6`: Django storage backend for Cloudinary to handle media and static files.
- `Django==4.2.10`: Django web framework; the core framework for the web application.
- `django-allauth==0.57.2`: integrated set of Django applications addressing authentication, registration, account management, and third-party (social) account authentication.
- `django-crispy-forms==2.1`: Django app that provides a way to render Django forms in a DRY, configurable, and reusable way.
- `django-summernote==0.8.20.0`: Django app that integrates the Summernote WYSIWYG editor for text fields.
- `gunicorn==20.1.0`: Python WSGI HTTP Server for UNIX - robust and performant server to serve the Django application.
- `oauthlib==3.2.2`: generic, spec-compliant implementation of OAuth for use as a foundation for OAuth consumers and providers.
- `psycopg2==2.9.9`: PostgreSQL database adapter for Python, a prerequisite for using PostgreSQL with Django.
- `PyJWT==2.8.0`: Python library to encode and decode JSON Web Tokens (JWT), often used in authentication mechanisms.
- `python3-openid==3.2.0`: Python 3 port of the Python OpenID library, used for OpenID authentication.
- `PyJWT==2.8.0`: Python library that allows accurate and cross-platform timezone calculations.
- `requests-oauthlib==1.3.1`: An OAuthlib authentication support for Requests, which allows you to use OAuth to authenticate with APIs.
- `sqlparse==0.4.4`: non-validating SQL parser for Python, useful for parsing and splitting SQL statements.
- `urllib3==1.26.15`: powerful HTTP client for Python. Used by Requests internally.
- `whitenoise==5.3.0`: efficiently serves static files in Django applications, enhancing performance.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Methodology

The WatchBidCentral project adheres to an agile-inspired methodology, promoting teamwork, adaptability, and incremental development. This strategy has steered the project's progress:

### Agile Project Management with GitHub Projects
To streamline project management, GitHub Projects is employed as a central hub. User stories and tasks are structured as GitHub issues, creating an organized workflow. The GitHub project board serves as a visual representation, tracking progress effectively.

### User Stories as GitHub Issues
Transforming user stories into GitHub issues captures user-centric functionalities. These issues interlink with respective user stories, simplifying access to criteria, tasks, and comments.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Features
### Login Landing Page:
- Description: The landing page provides a carousel of most liked listings and a list of watches ordered by created date.
<details><summary>See Screenshot **Landingpage, large**</summary><img src="assets\img\README_images\index.jpg" width= 600px></details>
<details><summary>See Screenshot **Landingpage, mobile**</summary><img src="assets\img\README_images\index mobile.jpg" width= 300px></details>

### About Us:
- Description: A detailed section about the company and services. 
<details><summary>See Screenshot **About us, large**</summary><img src="assets\img\README_images\about.jpg" width= 600px></details>
<details><summary>See Screenshot **About us, mobile**</summary><img src="assets\img\README_images\about mobile.jpg" width= 300px></details>

### Create Listing:
- Description: A form to create a new listing to host on the site.
<details><summary>See Screenshot **Sign Up, large**</summary><img src="assets\img\README_images\create listing.jpg" width= 600px></details>
<details><summary>See Screenshot **Sign Up, mobile**</summary><img src="assets\img\README_images\create listing mobile.jpg" width= 300px></details>

### Liked Listings:
- Description: A filtered view of all the watch listings by most liked.
<details><summary>See Screenshot **Sign Up, large**</summary><img src="assets\img\README_images\liked listings.jpg" width= 600px></details>
<details><summary>See Screenshot **Sign Up, mobile**</summary><img src="assets\img\README_images\liked listings mobile.jpg" width= 300px></details>

### My Listings:
- Description: A view for a seller of their listings to manage them.
<details><summary>See Screenshot **Sign Up, large**</summary><img src="assets\img\README_images\my listings.jpg" width= 600px></details>
<details><summary>See Screenshot **Sign Up, mobile**</summary><img src="assets\img\README_images\my listings mobile.jpg" width= 300px></details>

### Future Features
Here are some exciting features that I would like to add to the site in the future:

| Feature | Description |
| --- | --- |
| **Restrict Likes to one per site user** | Implement the restriction to limit the times a person can like a post. |
| **Nested Comments** | Implement nested comments to all for greater depth in engagement |
| **Bid Timer** | Allow a seller to set a timer on the listing |
| **Comment Editing and Deletion** | Enable users to edit and delete their comments for better content control. |
|  |  |

<br>

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Testing

WatchBidCentral underwent extensive testing to ensure its functionality, accessibility, and performance were up to standard. This rigorous process included code validation, accessibility checks, performance evaluation, cross-device compatibility testing, browser compatibility confirmation, reviewing user stories, and incorporating user feedback to improve the overall experience.

## Automated testing

### Python Testing

The files are located in each app, in a folder called "Tests". to run the test run "python manage.py test" from a terminal.Extensive unit tests were written for the Python code in Django.

<img src="assets\img\README_images\django test.jpg" width="550" height="150">

## Manual Testing

- The website was tested on Google Chrome and Microsoft Edge.
- The website was viewed on various monitors and resolutions and on a Pixel 7 mobile phone.
- Chrome Dev Tools was used to test how the site looks on various screen sizes.

<details>
<summary>Linter - PASS</summary>

  - Javascript tested on both sites with no significant errors

    - [JSHint](https://jshint.com/)
    - [JSLint](https://www.jslint.com/)
</details>

<details>
<summary>Lighthouse  -  PASS</summary>

- Desktop

    <img src="assets\img\README_images\lighthouse.jpg">

- Mobile

    <img src="assets\img\README_images\lighthouse mobile.jpg">
</details>
W3C Markup Validtor - PASS
W3C CSS Validator - PASS
<detailS>
<summary>Responsive - PASS</summary>

- Resolutions checked

    - 320x568: Used by small smartphones or devices in portrait mode.
    - 375x667: Used by smartphones like iPhone 6/7/8 in portrait mode.
    - 360x640: Common resolution for many budget and mid-range smartphones.
    - 414x896: Found on various iPhone models like iPhone X, XS, 11 Pro, and 12 Pro.
    - 768x1024: Common resolution for tablets in portrait mode, such as the iPad.
    - 1024x768: Another common resolution for tablets, especially in landscape mode.
    - 1280x800: Common resolution for smaller laptops and tablets.
    - 1366x768: Common for laptops and desktop monitors.
    - 1920x1080: Full HD resolution, used on larger monitors, laptops, and some mobile   devices.
    
</details>

#### Manual Testing

- The website was tested on Google Chrome and Microsoft Edge.
- The website was viewed on various monitors and resolutions and on a Pixel 7 mobile phone.
- Chrome Dev Tools was used to test how the site looks on various screen sizes.


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Bugs
The bug description section have been linked with the bug issues in my documentation for better visibility. The issue numbers are clickable to get a more comprehensive bug report.

### Known bugs ❌ 


<details>
<summary>Likes Button no longer working:</summary>

- Error

    <img src="assets\img\README_images\likes bug.jpg">
    <img src="assets\img\README_images\likes bug 2.jpg" width="600" height="150">
  At some point in Development it stoped working and ran out of time to fix it.

</details>


### Fixed bugs ✅

### Django Flatpages, 
- When implementing Django's flatpages for static content, like an "About" page, you faced significant setup challenges. Initially, you attempted to bypass URL pattern requirements with middleware, but issues arose. Switching strategies, you directly added a URL pattern and set APPEND_SLASH = True for troubleshooting, also configuring flatpages admin for various environments (Gitpod, Heroku, localhost).

- Persistent difficulties almost led to abandoning flatpages. However, a fresh start—removing all initial setups and reconfiguring from scratch—resolved the issues. This experience highlighted the effectiveness of resetting configurations and the value of methodical troubleshooting in successfully integrating Django features.

### Listing images not loading on watch_detail page
- Fixed, the issue was the iteration was incorrect
	

### Price showing as "{{ listing.price }}" instead of integer
- Fixed by removing the if statment to show either the price of the bid, these should be shown seperately

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Deployment

### App Deployment
For deploying Your app, Heroku is used. Follow these steps:

 **Create a New App:**
   - Create a new app on Heroku dashboard.

 **Configure Settings:**
   - Navigate to "Settings" in new app.

 **Config Vars Setup:**
   - In "Config Vars," add `PORT` as the key and `8000` as its value.

 **Add PostgreSQL Database:**
   - Choose PostgreSQL as database.

        Example "ElephantSQL" was used in this project

 **Configure DATABASE_URL:**
   - In "Config Vars," add `DATABASE_URL` and copy the URL from PostgreSQL dashboard.

     Note: If using ElephantSQL as PostgreSQL provider, you can use the URL provided by ElephantSQL.

 **Environment Variable Setup:**
   - Create a new file in workspace called `env.py`.
   - Import the `os` library and set the environment variable for `DATABASE_URL` to the Heroku address (or ElephantSQL URL)
   - Add a secret key using `os.environ["SECRET_KEY"] = "your secret key here"`.

 **Heroku Config Vars:**
   - Add the secret key to the Heroku app's config vars in the settings.

 **Django Settings:**
   - In `settings.py` of Django app, import `Path` from `pathlib`, `os`, and `dj_database_url`.
   - Add `if os.path.isfile("env.py"): import env` to the file.
   - Replace the SECRET_KEY with `SECRET_KEY = os.environ.get('SECRET_KEY')`.
   - Replace the database section with `DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}`.

 **Migrate Models:**
   - In workspace terminal, migrate the models to the new database connection.

### Cloudinary
To integrate Cloudinary into project, follow these steps:

 **Cloudinary Account:**
   - Log in to Cloudinary account or create one.

 **Copy CLOUDINARY_URL:**
   - Copy `CLOUDINARY_URL`.

 **Environment Variable Setup:**
   - In `env.py`, add `os.environ["CLOUDINARY_URL"] = "add cloudinary_url here"`.

 **Heroku Config Vars:**
   - In Heroku settings, add `CLOUDINARY_URL` to config vars.

 **Django Settings:**
   - In `INSTALLED_APPS`, add `cloudinary_storage`, `Django.contrib.staticfiles`, and `cloudinary` in this order.
   - Configure static file settings in `settings.py`: URL, storage path, directory path, root path, media URL, and default file storage.

 **Templates Directory Link:**
   - Link the file to the templates directory in Heroku with `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`.

 **Change Templates Directory:**
   - Change the templates directory to `TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]`.

 **Additional Folders:**
   - Create three new folders: `media`, `static`, and `templates`.

 **Procfile Creation:**
   - Create a `Procfile`.
   - Add the following line inside the Procfile: `web: gunicorn project_name_here.wsgi`.

 **Push Changes:**
    - Push all changes to GitHub.

 **Manual Deployment:**
    - In the Heroku deployment tab, deploy to Heroku manually the first time and closely monitor the process.
    - Once successful, set up automatic deployments.

### Version Control
To manage version control and push code to the main repository on GitHub using GitPod, follow these steps:

 **Add Changes:**
   - In the GitPod terminal, use the command `git add .` to stage changes.

 **Commit Changes:**
   - Commit changes with a descriptive comment using the command:
     ```
     git commit -m "Push comment here"
     ```

 **Push to GitHub:**
   - Push the updates to the repository on GitHub with the command:
     ```
     git push
     ```

 **Migrate Models:**
    - In the terminal, migrate the models to the new database connection.


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Credits
### Here's a collection of sites that were helpful in creating this website:

### Django Documentation:
The official Django documentation with guidance on models, forms, templates, and various aspects of Django development.

- [Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)
- [DeleteView](https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/)
generic-editing/)
- [Authentication System](https://docs.djangoproject.com/en/3.2/topics/auth/default/)
- [URL patterns](https://docs.djangoproject.com/en/5.0/topics/http/urls/)
- [Messages](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/)
- [Automated testing](https://docs.djangoproject.com/en/5.0/topics/testing/overview/)

### Bootstrap docs:
- [Increase knowledge of Bootstrap framework](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Bootstrap Template used](https://startbootstrap.com/template/shop-homepage)

### Media

- All watch images were taken from a number of sites, too many to mention.

### Content
- Content for the webpage and readme-file was written together with [ChatGPT](https://chat.openai.com/)


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Acknowledgments
 I'd like to give recognition to the ones who have supported me in creating this project:

My mentor Mitko Bachvarov for his help in guiding me through this project

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---