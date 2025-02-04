# Personal Access Tokens

Any admin user can create a PAT (personal access token) under the Integrations page. This token allows the user to access the API calls.

![integrations_pat.png](/integrations_pat.png)

Creating a PAT will give you a token that can only be seen once. Please copy this token and save it somewhere secure.

You can provide an expiry date and remove existing tokens from your user. Please note that this token is connected to your user and not the company.

Then go to the [swagger page](https://sase.jimber.io/docs) where you can use your PAT.

At the top right of the swagger page you have an Authorize button where the token can be used. Fill in your token under the api header called 'x-pat'.

![swagger_x_pat.png](/swagger_x_pat.png)




