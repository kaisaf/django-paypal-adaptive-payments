import collections
import requests
import json

def payment(recipient_email, dollars):

    headers = {
        #The first three are from my developer account
        "X-PAYPAL-SECURITY-USERID":"<add your user_id>",
        "X-PAYPAL-SECURITY-PASSWORD":"<add your password>",
        "X-PAYPAL-SECURITY-SIGNATURE":"<add your signature>",
        "X-PAYPAL-APPLICATION-ID": "APP-80W284485P519543T",
        "X-PAYPAL-SERVICE-VERSION":"1.1.0",
        "X-PAYPAL-REQUEST-DATA-FORMAT":"JSON",
        "X-PAYPAL-RESPONSE-DATA-FORMAT":"JSON"
    }

    # Store your paypal credentials in a separate file (my example:
    # "credentials.json" in paypal_project folder) and add that file to .gitignore.
    # Retrieve credentials like so:
    keys = json.load(open("paypal_project/credentials.json"))
    headers["X-PAYPAL-SECURITY-USERID"] = keys["user_id"]
    headers["X-PAYPAL-SECURITY-PASSWORD"] = keys["password"]
    headers["X-PAYPAL-SECURITY-SIGNATURE"] = keys["signature"]

    params = collections.OrderedDict()
    params = {
        "actionType":"PAY",    #Specify the payment action
        "currencyCode":"USD",
        "receiverList":{"receiver":[{
        "amount":"",
        "email":""}]  # The payment Receiver's email address
    },
        # Where the Sender is redirected to after approving a successful payment
        "returnUrl":"http://127.0.0.1:8000/success",
        # Where the Sender is redirected to upon a canceled payment
        "cancelUrl":"http://127.0.0.1:8000/cancel",
        "requestEnvelope":{
        "errorLanguage":"en_US",
        "detailLevel":"ReturnAll"   # Error detail level
    }
    }

    # Assign recipients email and paid amount in dollars to appropriate params:
    params["receiverList"]["receiver"][0]["email"] = recipient_email
    params["receiverList"]["receiver"][0]["amount"] = str(dollars)

    # Send a Pay request to PayPal
    url = "https://svcs.sandbox.paypal.com/AdaptivePayments/Pay"
    response = requests.post(url, data=json.dumps(params), headers=headers)

    # Check the response:
    #print(response.content.decode())
    response_string = response.content.decode("utf-8")
    response_dict = json.loads(response_string)
    payKey = response_dict.get("payKey")

    paypal_redirect_string = "https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_ap-payment&paykey=" + payKey
    return paypal_redirect_string
