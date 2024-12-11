<h1>Google Form Automation with Selenium (Python)</h1>

<p>
  This Python script automates the process of filling out and submitting responses to a Google Form multiple times using Selenium WebDriver. The form is filled with randomized answers to simulate diverse survey responses. The script is designed to handle multiple-choice questions, Likert scale questions, and input fields in Google Forms.
</p>

<h2>Features</h2>
<ul>
  <li>Randomized Inputs: Automatically selects random answers for each question in the form (gender, age, education, income, shopping habits, and Likert scale).
</li>
  <li>Form Navigation: Scrolls through the page to ensure all form elements are loaded.
</li>
  <li>Automated Submissions: Submits responses repeatedly to simulate survey participation.
</li>
  <li>Error Handling: Includes error handling to continue submitting forms even if some questions or elements are not found or interacted with successfully.
</li>
  <li>Customizable: You can easily adjust the number of form submissions or modify the input options to fit your needs.
</li>
</ul>

<h2>Prerequisites</h2>
<ul>
  <li>
    Python 3.x: Ensure that you have Python installed on your system.
  </li>
  <li>Selenium: Install the Selenium library for browser automation.
</li>
  <li>
    ChromeDriver: Ensure that you have ChromeDriver installed and correctly referenced in the script.
  </li>
<li>
  Web Browser: The script uses Google Chrome for automation.
</li>
</ul>

<h2>How to use</h2>
<ol>
  <li>Clone the repository or download the script.
</li>
  <li>Ensure you have Python and Selenium installed on your machine.
</li>
  <li>Download and install ChromeDriver, and update the CHROMEDRIVER_PATH variable in the script to point to your ChromeDriver executable.
</li>
  <li>Modify the FORM_URL variable to point to your specific Google Form URL.
</li>
  <li>
    Run the script to automatically fill and submit the form. The script will attempt to submit 90 responses (or more, depending on your settings). - <b>python automate_form_submission.py</b>
</ol>

<h3>Notes</h3>
<ul>
  <li>The script currently contains URL to Google forms, PATH to Chromedriver and questions for my survey. Please update for your own use</li>
  <li>The script uses randomized data to fill out each question, which helps simulate real-world survey submissions.
</li>
  <li>Ensure you are allowed to use automated submissions for the form to avoid violating terms of service.
</li>
  <li>The script waits for elements to load before interacting with them, making it resilient to slow internet connections.
</li>
</ul>
