from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Path to ChromeDriver
CHROMEDRIVER_PATH = r"C:\Chromedriver\chromedriver.exe"

# URL of your Google Form
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdAr5peMHXedyK9K1zYvYDol7EoE4r-DfmufRsPBwueNtJjdA/viewform"


def scroll_page(driver):
    """Scroll down and up to ensure the form is fully rendered."""
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)


def fill_form(driver):
    """Fill the Google Form with randomized responses."""
    # Scroll the page to ensure all elements are rendered
    scroll_page(driver)

    # Question 1: Jūsų lytis // Your gender
    gender_options = [
        "//div[@id='i6']",  # Moteris // Female
        "//div[@id='i9']",  # Vyras // Male
        "//div[@id='i12']"  # Nenoriu atskleisti // Dont want to reveal
    ]
    driver.find_element(By.XPATH, random.choice(gender_options)).click()

    # Question 2: Jūsų amžius // Your age
    age_options = [
        "//div[@id='i20']",  # 16–25 
        "//div[@id='i23']",  # 26–35
        "//div[@id='i26']",  # 35–44
        "//div[@id='i29']",  # 45–54
        "//div[@id='i32']",  # 55+
    ]
    driver.find_element(By.XPATH, random.choice(age_options)).click()

    # Question 3: Išsilavinimas
    education_options = [
        "//div[@id='i40']",  # Aukštasis // University
        "//div[@id='i43']",  # Nebaigtas // Not completed university
        "//div[@id='i46']",  # Kolegija // College
        "//div[@id='i49']",  # Aukštesnysis // High school
        "//div[@id='i52']",  # Vidurinis // Vocational
        "//div[@id='i55']",  # Bendras // Overall
        "//div[@id='i58']",  # Kita // Other
    ]
    driver.find_element(By.XPATH, random.choice(education_options)).click()

    # Question 4: Pajamos // Monthly Income
    monthly_income_options = [
        "//div[@id='i66']",  # Iki 500
        "//div[@id='i69']",  # 501–1000
        "//div[@id='i72']",  # 1500–2000
        "//div[@id='i75']",  # 2000–2500
        "//div[@id='i78']",  # 2500+
        "//div[@id='i81']",  # Nenoriu nurodyti
    ]
    driver.find_element(By.XPATH, random.choice(monthly_income_options)).click()

    # Question 5: Pirkinių trukmė // Shopping Time
    shopping_time_options = [
        "//div[@id='i89']",  # Iki 1 val.
        "//div[@id='i92']",  # 1–3 val.
        "//div[@id='i95']",  # 3–5 val.
        "//div[@id='i98']",  # 5+ val.
    ]
    driver.find_element(By.XPATH, random.choice(shopping_time_options)).click()

    # Question 6: Pirkimo būdas // Purchase Method
    purchase_method_options = [
        "//div[@id='i106']",  # Internetu
        "//div[@id='i109']",  # Fiziniuose prekybos centruose
        "//div[@id='i112']",  # Abiem būdais vienodai
    ]
    driver.find_element(By.XPATH, random.choice(purchase_method_options)).click()

    # Likert Scale Sections // Likert Scale
    radiogroups = driver.find_elements(By.XPATH, "//div[@role='radiogroup']")
    print(f"Found {len(radiogroups)} radiogroups")

    global_question_index = 1
    for _ in range(len(radiogroups)):
        try:
            random_option = random.randint(1, 7)
            xpath = f"(//div[@role='radiogroup'])[{global_question_index}]//div[@role='radio' and @aria-posinset='{random_option}']"
            print(f"Trying XPath: {xpath}")
            radio_button = driver.find_element(By.XPATH, xpath)
            driver.execute_script("arguments[0].scrollIntoView();", radio_button)
            radio_button.click()
            global_question_index += 1
        except Exception as e:
            print(f"Error with question {global_question_index}: {e}")
            global_question_index += 1
            continue

    submit_button = driver.find_element(By.XPATH, "//span[text()='Pateikti']")
    submit_button.click()

    driver.get(FORM_URL)


def main():
    """Main function to fill the form multiple times."""
    for i in range(90):  # Change this to the number of responses you need // Change this to the number of responses you need
        try:
            print(f"Submitting response #{i + 1}")
            service = Service(CHROMEDRIVER_PATH)
            driver = webdriver.Chrome(service=service)
            driver.get(FORM_URL)
            fill_form(driver)
            driver.quit()  # Restart browser session for every form submission // Restart browser session for every form submission
        except Exception as e:
            print(f"Error during submission #{i + 1}: {e}")
            continue


if __name__ == "__main__":
    main()
