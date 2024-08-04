# DjangoForms
<div>
<p>
    Django Forms is an essential part of Django.
    For  handling form  data validation and manipulation.
</p>
<p>
    Django Forms is a Django component that facilitates  the creation, validation, and manipulation of HTML forms.
    It abstracts the complexity of form processing, providing   an  organized and secure way to handle user data input.
</p>

##### Obs: Don't worry i'll explain specific terms (<u>underlined</u>) that you might not understand ( there at the end )

</div>

## Essential points
<ul>
    <li>Form Definition</li>
    <li>Data Validation</li>
    <li>Error Management</li>
    <li>Rendering</li>
    <li>Widgets</li>
    <li>Security</li>
</ul>

## When should i use

**User Data Input:**  

<p style='margin-left:20px'>
    Whenever your application requires user data input, such as registration forms, login forms, or any other information input, Django Forms is the natural choice. 
</p>

**Data Manipulation:**  

<p style='margin-left:20px'>
   To manipulate and validate data that comes from POST requests, such as form submissions.
 
</p>

**Integration With <u>Models</u>:**  

<p style='margin-left:20px'>
    When you need to create a form based on a Django Models, making it easy to create and edit Models instances.
</p>

## Good practices (that i recommend)

**1 - Use <u>ModelForm</u> When Possible**:
<p style='margin-left:20px;'>
 If the form is directly related to a model, use ModelForm to take advantage of automatic integration with the <u>Django ORM</u>. This reduces code duplication and simplifies logic.
</p>

**2 - Validate Data Appropriately:**
<p style='margin-left:20px;'>
 Define custom validation methods only if you need specific rules that are not covered by standard validators. (if not, don't do it :)
</p>    

**2 - Keep Business Logic in the Backend:**
<p style='margin-left:20px;'>
    Avoid validation logic or complex processing in the frontend. Maintain business logic and validation in the backend, ensuring data is processed and validated securely.

**"What I recommend is that you carry out validations at both the backend and frontend  levels."**
    <br>
    <br>
    **frontend level:** Simple validations like email, password, birth date, user's number etc... 
    <br>
    <br>
    **backend level:** Now yes, validations must be done in more depth, such as checking whether the email received is already being used, check whether the data sent complies with the system guidelines.
</p>

**3 - Display coherent error messages:**
<p style='margin-left: 20px'>
    What I see in many systems is error messages illustrated in such a way that the user does not understand what is really wrong messages like this (invalid username or password, use another email)
    <br>
    <br>

**What I recommend is create a method to handle all errors and assign their respective messages after deciding whether to display a list of error messages or just a string that joins the error messages together**
</p>

**4 - Protect Against CSRF (i highly recommend):**
<p style='margin-left:20px'>
 Always use the <u>CSRF tokens</u> provided by Django to ensure your POST requests are secure.
<p>

**5 - Test Your Forms (i highly recommend):**
<p style='margin-left:20px'>
  Write tests to verify that your forms are validating and processing data correctly, helping you avoid <u>regressions</u>.
<p>


## Explaining specific underlined terms

### Model
<p style='margin-left:20px'>
In Django, a Model is a Python class that represents a table in the database. Each class attribute represents a field in the table.
</p>

### ModelForm
<p style='margin-left:20px'>
In Django, a ModelForm is a class that automatically creates a form from a model (Model). It provides a convenient way to generate HTML forms based on fields in a template, saving time and reducing code repetition
</p>

### Django ORM
<p style='margin-left:20px'>
Django ORM (Object-Relational Mapping) is a system that allows developers to interact with the database in a more intuitive and abstract way, using Python classes and objects instead of directly writing SQL. It is a central part of the Django framework, which maps Python classes to database tables and class instances to rows in those tables.
</p>

### CSRF token
<p style='margin-left:20px'>
Imagine that you are authenticated on a banking website and, at the same time, you visit a malicious website. The malicious website may attempt to send a request in your name to the banking website, such as a money transfer. As you are already authenticated, the banking website will process the request as if it were legitimate, resulting in unwanted actions. This is CSRF (Cross-Site Request Forgery).

</p>

### Regression
<p style='margin-left:20px'>
A regression is a situation where a new change to the software results in loss of functionality or bugs in parts of the system that were previously working correctly.
</p>
