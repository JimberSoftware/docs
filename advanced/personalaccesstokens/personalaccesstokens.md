# Personal Access Token (PAT)

Any **admin user** can create a Personal Access Token (PAT) from the **Settings** ![](../../images/menu/menu_settings.png ':size=20') page. This token allows you to access the API securely using your user credentials.

---

### Creating a Personal Access Token

1. Navigate to the **Settings** page in your admin dashboard.  
2. Locate the **PAT - Personal Access Tokens** section.
![pat.png](/screenshots/pat.png ':size=800')
3. Click on **Create New Token**.  
4. Enter a clear, descriptive **name** for your PAT to help you identify its purpose later.  
5. Optionally, set an **expiry date** for the token to enhance security.
![create_pat.png](/screenshots/create_pat.png ':size=500')
6. Once created, the token will be displayed **only once** — make sure to copy it by pressing the copy icon ![](../../images/icons/icon_copy.png ':size=20') and save it securely.
![copy_pat.png](/screenshots/copy_pat.png ':size=800')
7. Your active token will be listed in the section. You can delete the token before it's expiry date by pressing the delete icon ![](../../images/icons/icon_delete.png ':size=20') in it's row. 
![active_pat.png](/screenshots/active_pat.png ':size=800')

> [!WARNING]  
> The token is shown only once at creation. If you lose it, you will need to generate a new one.

---

## Important Notes

- The PAT is **linked to your individual user account**, not to the company account.
- You can revoke or delete existing tokens anytime from your user settings.
- Expiry dates help limit the token’s lifetime and reduce security risks.

---

## Using the PAT in the API (Swagger UI)

After you create your token, you can use it to authenticate API calls through the Swagger documentation site:

👉 [https://sase.jimber.io/docs](https://sase.jimber.io/docs)

### What you can do on the Swagger page:

- **Authorize Using PAT:**  
  Click the **Authorize** button (top right) and enter your Personal Access Token under the `x-pat` header to authenticate your requests.
  
  ![authorize_pat.png](/screenshots/authorize_pat.png ':size=500')
  ![loggedin_pat.png](/screenshots/loggedin_pat.png ':size=500')

- **Explore API Endpoints:**  
  The Swagger UI lists all available API endpoints grouped by functionality. You can browse and read details about request parameters, response formats, and example calls. For example, this section contains API endpoints for Users:

  ![swagger_user.png](/screenshots/swagger_user.png ':size=800')

- **Test API Calls Directly:**  
  Using the interactive interface, you can send requests to the API right from the browser. This helps you validate API behavior before integrating it into your applications.

- **View Request and Response Details:**  
  Swagger shows the full HTTP request and response, including headers, status codes, and response bodies. This is invaluable for debugging and learning how the API works.

- **Try Different HTTP Methods:**  
  The UI supports all methods the API offers (GET, POST, PUT, DELETE, etc.), so you can perform full CRUD operations interactively.



---

## Summary

| Step                     | Action                                    |
|--------------------------|-------------------------------------------|
| Create PAT               | Admin creates token on Settings page      |
| Save Token               | Copy token securely (only shown once)     |
| Use Token                | Authorize API calls via Swagger UI (`x-pat`) |
| Manage Tokens            | Revoke or set expiry via user settings    |

---

If you need help with creating the token or using the API, feel free to reach out to your admin or support team.


