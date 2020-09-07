# Scripting With Python
This project based on linked in course: [Scripting for Tester](https://www.linkedin.com/learning/scripting-for-testers/welcome?u=2082620) by Dave Westerveld.

It's about scripting with python language in order to automate manual process

## Tools instalation
- [Python](https://www.python.org/downloads/)

Libraries need to install
- Requests
```
python -m pip install requests
```
- Gspread (for google sheet)
```
python -m pip install gspread
```
- Google api
```
python -m pip install google-api-python-client
```
- Selenium
```
python -m pip install selenium
```
- Chromedriver

### Run Test
Go to test folder execute this command
```
python <filename.py>
```

#### AutomateReport
For Google chart, please take a look this [link](https://developers.google.com/chart/interactive/docs/quick_start)

For test that need access Google sheet, you should provide credential key in json file. heres steps to get the key:
- Create project in [google developer console](https://console.developers.google.com/)
- In newly created project add Google sheet and Google drive library
- Create credential, choose type Service Account
- Download your json file credential
- Get the email from your json file, and share your google sheet file with the email

for further information about gspread library, [checkout here](https://gspread.readthedocs.io/en/latest/)
