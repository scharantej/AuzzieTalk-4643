## Flask Application Design

### HTML Files

1. `index.html`:
   - This is the main page of the application and will contain the form for adding flashcards.
   - It will use the Bootstrap framework and include the necessary elements for the form, such as input fields, labels, and a submit button.

2. `results.html`:
   - This page will display the results of the translation.
   - It will include a list of the translated flashcards.

### Routes

1. `/`:
   - This is the route for the main page.
   - It will handle the GET request and render the `index.html` file.

2. `/translate`:
   - This is the route for the translation.
   - It will handle the POST request and call the translation logic to translate the flashcards.
   - Once the translation is complete, it will render the `results.html` file with the translated flashcards.