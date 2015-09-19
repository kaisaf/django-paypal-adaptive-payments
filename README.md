Step-by-Step guide to PayPal Adaptive Payments API DEMO:

First get yourself a PayPal developer account and create a couple of users in their
Sandbox. Then..

1. Clone this repo
2. Create a virtual environment inside the paypal folder:
   $ virtualenv -p python3 env
3. Activate env:
   $ source env/bin/activate
4. Install everything you need:
   $ pip3 install -r requirements.txt
5. Go inside paypal_project:
   $ cd paypal_project
   [This example uses a postgres database; if you don't want to use it, just
   change the settings file before continuing.]
   $ python3 manage.py makemigrations
   $ python3 manage.py migrate
   $ python3 manage.py runserver
6. Open your browser in your root directory 127.0.0.1:8000, you should see a simple form asking recipients email and
dollars. Type in one of the users you created in Sandbox and click submit. This
takes you to PayPal payments. Password is whatever password you created in Sandbox.
