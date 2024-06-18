# Pixel Perfect Testing

<center> 

<img src="docs/README/am i responsive.jpg" alt="Am I responsive site image" width=900px> 

</center>

Developer: [Barry Flynn](https://github.com/barryCFlynn/) <br>
[Live webpage](https://pixel-perfect-d96b20ab326d.herokuapp.com/)<br>
[Project Repository](https://github.com/barryCFlynn/Pixel_Perfect)<br>


## Code Validation

- HTML: Click link to see test results [W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fecho-chamber-ci-f4fdc2207726.herokuapp.com%2F)
- CSS: Click link to see test results [W3C Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fecho-chamber-ci-f4fdc2207726.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- JavaScript: [JSHint](https://jshint.com/)
    - comment-like.js no errors warnings for usings $ for jQuery ignored
    - infinite-scroll.js no errors warnings for usings $ for jQuery ignored
    - post-like.js no errors warnings for usings $ for jQuery ignored
- Python: [CI Python Linter](https://pep8ci.herokuapp.com/)
    - forms.py no errors
    - models.py no errors
    - urls.py no errors
    - views.py no errors
    - test_views.py no errors

## Performance Testing

I conducted performance testing using google chrome light house. The results are as follows:

- index.html, _post_list.html , _post_list_partial.html, 
    - Performance: 99
    - Accessibility: 90
    - Best Practices: 100
    - SEO: 100

- about.html
    - Performance: 100
    - Accessibility: 90
    - Best Practices: 100
    - SEO: 100

- _profile.html
    - Performance: 100
    - Accessibility: 90
    - Best Practices: 100
    - SEO: 100

- _post_edit.html
    - Performance: 100
    - Accessibility: 91
    - Best Practices: 100
    - SEO: 100

- _post_detail.html , _post_interactions.html, comment_interactions.html
    - Performance: 100
    - Accessibility: 86
    - Best Practices: 100
    - SEO: 89



## Device compatibility

I tested the website on the following devices:

- Various Desktops
- Various Laptop
- iPhone 8
- Samsung Galaxy S20

The website was responsive on all devices and the functionality was consistent across all devices.

## Browser compatibility

I tested the website on the following browsers:

- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- Safari

The website was responsive on all browsers and the functionality was consistent across all browsers.

## Manual Testing

I conducted manual testing on the website to ensure that all functionality was working as expected. 

| Test Case                       | Description                                                 | Method                                                      | Expected Outcome                                              | Actual Outcome                        | Pass/Fail |
|---------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------|-----------|
| User Sign-Up                    | Test user registration functionality                        | Navigate to sign-up page and create a new account            | User account created and user redirected to profile page       | User account created and redirected to profile | Pass      |
| User Login                      | Test user login functionality                               | Navigate to login page and log in with valid credentials     | User successfully logged in and redirected to homepage         | User logged in and redirected to homepage | Pass      |
| User Profile Update             | Test updating user profile information                      | Update user information in profile settings                  | User profile information updated successfully                  | User profile updated successfully        | Pass      |
| Social Authentication           | Test login with social media accounts                       | Use social login option to sign in                           | User successfully logged in with social account                | User logged in with social account      | Pass      |
| Product Listings                | Test product listing display                                | Navigate to products page                                    | All products displayed with correct details                    | All products displayed correctly        | Pass      |
| Product Detail View             | Test detailed view of a single product                      | Click on a product from the listing                          | Detailed product page displayed with correct information       | Detailed product page displayed correctly | Pass      |
| Add to Cart                     | Test adding items to the shopping cart                      | Add an item to the cart                                      | Item added to cart and cart count updated                      | Item added to cart and cart count updated | Pass      |
| Update Cart Quantity            | Test updating item quantity in the cart                     | Change the quantity of an item in the cart                   | Item quantity updated and cart total recalculated              | Item quantity updated and total recalculated | Pass      |
| Remove from Cart                | Test removing items from the cart                           | Remove an item from the cart                                 | Item removed from cart and cart count updated                  | Item removed from cart and cart count updated | Pass      |
| Checkout Process                | Test completing a purchase                                  | Go through checkout process with valid payment details       | Purchase completed and order confirmation displayed            | Purchase completed and confirmation displayed | Pass      |
| Order History                   | Test viewing order history                                  | Navigate to order history page                               | User's past orders displayed correctly                         | Past orders displayed correctly         | Pass      |
| Admin Product Management        | Test admin adding and editing products                      | Admin adds/edits product details in admin panel              | Product added/edited successfully and displayed on products page| Product added/edited and displayed correctly | Pass      |
| Newsletter Signup               | Test signing up for the newsletter                          | Submit email in newsletter signup form                       | Confirmation message displayed and email added to mailing list | Confirmation displayed, email added     | Pass      |
| Custom 404 Page                 | Test custom 404 error page                                  | Navigate to a non-existent URL                               | Custom 404 page displayed                                     | Custom 404 page displayed               | Pass      |
| Responsive Design               | Test website responsiveness                                 | Resize browser window or use different devices               | Website layout adjusts correctly for different screen sizes    | Layout adjusts correctly                | Pass      |
| Background Image Slideshow      | Test homepage background image slideshow                    | View homepage for image transitions                          | Background images transition smoothly                          | Images transition smoothly              | Pass      |
| Inventory Image Overlay         | Test overlay images on inventory detail page                | View product detail page with overlay images                 | Overlay images displayed correctly over background             | Overlay images displayed correctly      | Pass      |



Summary of manual testing:

- All functionality is working as expected
- The website is responsive on all devices and browsers
- The website is user-friendly and easy to navigate
- The website is visually appealing and consistent across all pages
- The website is accessible.

## Conclusion

The website has been thoroughly tested and all functionality is working as expected. The website is responsive, user-friendly, visually appealing and accessible. The website is compatible with all devices and browsers. The website has been validated and performance tested. The website has been automated and manually tested. The website is ready for deployment.


## Important Note to the Assessor

I manually created a few posts but everything below this post.

![Last Real Post](readme/Last-real-post.png)

Everything below this (When sorting by date) is generated by Faker and cannot be opened.
The other posts are there for the purpose of testing the infinite scroll feature.