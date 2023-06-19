# Automated Birthday Email Sender

This is a Python script that automates the process of sending birthday emails. It reads birthday data from a CSV file, matches the current date with birthdays, and sends personalized emails using pre-defined letter templates.

## Features

- Retrieves current month and day to identify birthdays
- Reads birthday data from a CSV file
- Selects a random letter template from the "Letters" folder
- Personalizes the letter with the birthday person's name
- Sends the email using the SMTP protocol and Gmail account

## Prerequisites

- Python 3.x
- pandas library: Install using `pip install pandas`
- smtplib library (built-in)
- datetime library (built-in)

## Getting Started

1. Clone the repository or download the script file.

2. Install the required libraries by running the following command:
``` bash
pip install pandas

```

3. Update the following variables in the script:
- `my_email`: Your email address.
- `password`: Your app password generated from Gmail account settings.

4. Prepare the birthday data:
- Create a CSV file named `birthdays.csv` with the following columns: `name`, `email`, `month`, and `day`.
- Fill in the details of the people and their respective birthdays in the CSV file.

5. Create letter templates:
- Create text files with the desired letter content in the "Letters" folder.
- Use the placeholder `[name]` to represent the name of the birthday person.

6. Run the script using the following command:

7. The script will identify the birthdays for the current date, select a random letter template, personalize it, and send the email to the respective recipients.


# Running on PythonAnywhere and Scheduling a Task

To automate the birthday email sending process on a regular basis, you can use a platform like PythonAnywhere and schedule a task to run the script periodically.

Here's how you can do it on PythonAnywhere:

1. Sign up for a PythonAnywhere account at [pythonanywhere.com](https://www.pythonanywhere.com).

2. Create a new "Scheduled Task" from the dashboard.

3. Set the task to run the script by specifying the command:
   ```
   python /path/to/script.py
   ```

4. Configure the desired schedule for the task. For example, you can set it to run daily at a specific time.

5. Save the task and let PythonAnywhere handle the rest. The script will be executed automatically according to the defined schedule.

By running the script on PythonAnywhere and scheduling a task, you can ensure that the birthday emails are sent without manual intervention.


## Notes

- Make sure to generate an app password from your Gmail account settings. Using a normal password may not work due to Gmail's security measures.
- Ensure the CSV file and letter templates are correctly formatted and located in the appropriate directories.

Feel free to customize the script and letter templates according to your needs. Happy automating!

