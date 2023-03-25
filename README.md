# form-notifier

## developer guid setup
- Create application and credentials using this manual - https://developers.google.com/sheets/api/quickstart/python
	- Save the credentials json file as 'credentials.json' in your project's directory
	- Enable Google sheets API
- Create form on your Google account - https://www.google.com/forms/about/
- Configure your form to save the results into Google sheet in your GoogleDrive account
- Save the Google sheet ID of your sheet
	- Get your sheet link (By sharing your sheet with others mechanism)
	- Extract your google sheed ID from the link by this format - https://docs.google.com/spreadsheets/d/{{Google_sheet_ID}}/...
	- Set the value of GOOGLE_SHEET_ID variable in your project
