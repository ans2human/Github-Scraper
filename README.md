# Github-Scraper

Hi! everyone and welcome to  **Github-Scraper**. Here i have coded a very simple script that logs in to your github account using **[Selenium](https://selenium-python.readthedocs.io/)**


# Installation
-   You need to download **[chromedriver](http://chromedriver.chromium.org/)** according to your OS for **selenium** to work.
- Declare the `executable_path` of your chromedriver file.


    ```
    **driver = webdriver.Chrome(executable_path= 'path to chromedriver file')**
    ```
    
-   To make it work you'll need  to install packages from `req.txt`.

- Add your password in the code in encoded form.

- Run this file from the terminal `python github.py`
## Password encoding


```
>>>import base64
>>>print(base64.b64encode(b'Your password'))`
>>>encoded password```
