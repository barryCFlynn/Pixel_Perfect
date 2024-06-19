# Pixel Perfect Testing

<center> 
<img src="docs/README/am i responsive.jpg" alt="Am I responsive site image" width=900px> 
</center>

[Developer Barry Flynn](https://github.com/barryCFlynn/) <br>
[Live webpage](https://pixel-perfect-d96b20ab326d.herokuapp.com/)<br>
[Project Repository](https://github.com/barryCFlynn/Pixel_Perfect)<br>



## Table of Contents

1. [Code Validation](#code-validation)
2. [Performance Testing](#performance-testing)
3. [Device Compatibility](#device-compatibility)
4. [Browser Compatibility](#browser-compatibility)
5. [Manual Testing](#manual-testing)
6. [Conclusion](#conclusion)



## Code Validation



- **HTML**: Click link to see test results [W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2F8000-barrycflynn-pixelperfec-txa16ud0xsf.ws-eu114.gitpod.io%2F)
    - Error: Element li not allowed as child of element nav - the is linked to the include of mobile-top-header.html, but trying fixes like placing in ul breaks styling and replacing nav with menu gives another error. This does not break the site and can be fixed later.
    - Error: Duplicate ID user-options - This is linked again to the base.html and mobile-top-header.html, only one is displaying at a time so no ID conflict occuring, can fix later

- **CSS**: Click link to see test results [W3C Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fpixel-perfect-d96b20ab326d.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) 
    - No Error Found.

- **JavaScript**: [JSHint](https://jshint.com/)
    - quantity_input_script.html js: no errors, warnings for usings $ for jQuery ignored
    - cart.html js: no errors, warnings for usings $ for jQuery ignored
    - inventory.html js: no errors, warnings for usings $ for jQuery ignored
    - main-nav.html js: no errors, warnings for usings $ for jQuery ignored
    - countryfield.js: no errors, warnings for usings $ for jQuery ignored

- **Python**: [Flake 8 Python Linter](https://flake8.pycqa.org/)
    - Test was done in the GitPod terminal using "command python3 -m flake8", correct all errors except Line too long. Shortened the lines I could but was adding in errors with it, opted to leave them for now.

## Performance Testing

Performance testing using Google Chrome Lighthouse yielded underwhelming results, despite the site being stable and performing well in practice. Addressing these performance issues will require additional time and effort.

### Hosting Impact

One primary factor affecting performance is the use of Cloudinary for hosting images. Significant performance degradation is observed on pages hosting images (except index.html). Future optimizations may involve revisiting image hosting strategies to improve overall site performance.

- **index.html** - Pass
    - Performance: 85
    - Accessibility: 98
    - Best Practices: 79
    - SEO: 90

- **inventory.html**
    - Performance: 57
    - Accessibility: 95
    - Best Practices: 79
    - SEO: 82

- **inventoryitem.html**
    - Performance: 67
    - Accessibility: 77
    - Best Practices: 79
    - SEO: 91

- **cart.html**
    - Performance: 54
    - Accessibility: 82
    - Best Practices: 79
    - SEO: 82

- **orders.html**
    - Performance: 66
    - Accessibility: 89
    - Best Practices: 79
    - SEO: 91

## Device Compatibility

I tested the website on the following devices:

- Various Desktops
- Various Laptop
- iPhone 8
- Samsung Galaxy S20

The website was responsive on all devices and the functionality was consistent across all devices.

## Browser Compatibility

I tested the website on the following browsers:

- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- Safari

The website was responsive on all browsers and the functionality was consistent across all browsers.

#Manual Testing

I conducted manual testing on the website to ensure that all functionality was working as expected. 

**Test Case** | **Description** | **Method** | **Expected Outcome** | **Actual Outcome** | **Pass/Fail**
--- | --- | --- | --- | --- | ---
User Sign-Up | Test user registration functionality | Navigate to sign-up page and create a new account | User account created and user redirected to profile page | User account created and redirected to profile | Pass
User Login | Test user login functionality | Navigate to login page and log in with valid credentials | User successfully logged in and redirected to homepage | User logged in and redirected to homepage | Pass
User Profile Update | Test updating user profile information | Update user information in profile settings | User profile information updated successfully | User profile updated successfully | Pass
Product Listings | Test product listing display | Navigate to products page | All products displayed with correct details | All products displayed correctly | Pass
Product Detail View | Test detailed view of a single product | Click on a product from the listing | Detailed product page displayed with correct information | Detailed product page displayed correctly | Pass
Add to Cart | Test adding items to the shopping cart | Add an item to the cart | Item added to cart and cart count updated | Item added to cart and cart count updated | Pass
Update Cart Quantity | Test updating item quantity in the cart | Change the quantity of an item in the cart | Item quantity updated and cart total recalculated | Item quantity updated and total recalculated | Pass
Remove from Cart | Test removing items from the cart | Remove an item from the cart | Item removed from cart and cart count updated | Item removed from cart and cart count updated | Pass
Checkout Process | Test completing a purchase | Go through checkout process with valid payment details | Purchase completed and order confirmation displayed | Purchase completed and confirmation displayed | Pass
Order History | Test viewing order history | Navigate to order history page | User's past orders displayed correctly | Past orders displayed correctly | Pass
Admin Product Management | Test admin adding and editing products | Admin adds/edits product details in admin panel | Product added/edited successfully and displayed on products page | Product added/edited and displayed correctly | Pass
Newsletter Signup | Test signing up for the newsletter | Submit email in newsletter signup form | Confirmation message displayed and email added to mailing list | Confirmation displayed, email added | Pass
Custom 404 Page | Test custom 404 error page | Navigate to a non-existent URL | Custom 404 page displayed | Custom 404 page displayed | Pass
Responsive Design | Test website responsiveness | Resize browser window or use different devices | Website layout adjusts correctly for different screen sizes | Layout adjusts correctly | Pass

## Summary of Manual Testing

- All functionality is working as expected
- The website is responsive on all devices and browsers
- The website is user-friendly and easy to navigate
- The website is visually appealing and consistent across all pages
- The website is accessible.

### Conclusion

The website has been thoroughly tested and all functionality is working as expected. The website is responsive, user-friendly, visually appealing and accessible. The website is compatible with all devices and browsers. The website has been validated and performance tested. The website has been automated and manually tested. The website is ready for deployment.

<p align="right">[back to top](#table-of-contents)</p>
