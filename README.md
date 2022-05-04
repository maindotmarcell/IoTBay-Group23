# IoTBay
## Disclaimer!!!
Do **not** push anything to the main branch! Create your own branch and work on that. Otherwise we will have merge conflicts and it will be very hard and timely to fix it...
Thanks!
## Start Here
Here are a few notes that can help you guys  get up to speed with the application. I will be adding more stuff to this document. Make sure to check out the [video](https://www.youtube.com/watch?v=sm1mokevMWk&t=10777s) I followed to get the current application. 

The most important bits are: how the **database** works and how the **views, models and controllers** are linked. 

Don't worry about the styling, we can use bootstrap and add custom styling when we're done with everything.
## Installing Dependencies
You need to install the following packages to get the proper styling (you need to have **Python** and **pip** installed first):
- Bootstrap
```
pip install django-bootstrap-v5
```
- Django crispy forms
```
pip install django-crispy-forms
```

- Pillow
```
pip install pillow
```

## Pushing to GitHub
Open the terminal and make sure to create your branch with:
```
git branch yourname
```
And switch to that branch with:
```
git checkout yourname
```
Type in:
```
git status
```
This should give you the list of files you have changed.
Once you have verified that nothing is out of place, you can add the changes to the "staging", like so:
```
git add .
```
(. meaning you add everything, you could also put a filename there alternatively if you don't want to add everything).
Then you can create your commit like so:
```
git commit -m "insert message"
```
Once all your commits have been created (you can do multiple, but I usually just do one), you can push this to the GitHub:
```
git push origin marcell
```
Change marcell to whatever your branch name is.

*You can use any other graphical method to commit, this is just how I do it, it's also the traditional and most common way*


## How to run
Enter into the IoTBay_Group23 directory (the innermost one):
```
cd IoTBay_Group23
```
Then type the following command into your terminal:
```
python manage.py runserver
```
You can then click on the IP and port combination it gives you and you'll see the application working in your browser.

## What we need to do first

- We need to reset the database completely and rewrite the models.py file so that we have everything from our data dictionary/ERD diagram. We also need to use properties from the built in User class, as foreign keys (and get rid of the Customer class I created). We will need to then drop all the tables in the SQLight database and import/migrate all the updated models back into the database (from that point we won't have anything to do with the DB, Django will take care of that).
- We need to create an edit page, this should be very easy to do.
- We need to find some content online that can give us a guide to create the list of products (and how to properly display them on the page).