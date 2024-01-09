from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

def get_job_list(query):
    # Set up headless Firefox options
    options = Options()
    options.headless = True

    # Create a Firefox webdriver instance
    driver = webdriver.Firefox(options=options)

    # Construct the URL with the query
    url = f"https://www.indeed.com/jobs?q={query}"

    # Open the URL in the webdriver
    driver.get(url)

    # Get the page source and encode it as UTF-8
    page = driver.page_source.encode('utf-8')

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(page, 'html.parser')

    # Find all the job title spans
    job_titles = soup.find_all('span', id=lambda value: value and value.startswith('jobTitle-'))

    # Find all the company name spans
    company_names = soup.find_all('span', attrs={'data-testid': 'company-name'})

    # Find all the job location divs
    job_locations = soup.find_all('div', attrs={'data-testid': 'text-location'})

    # Create an empty list to store the job entries
    job_list = []

    # Iterate over the job title, company name, and job location spans simultaneously
    for title_span, company_span, location_span in zip(job_titles, company_names, job_locations):
        # Create a dictionary for each job entry
        job_dict = {
            "Job Title": title_span.text,
            "Company Name": company_span.text,
            "Job Location": location_span.text
        }
        # Append the job dictionary to the job list
        job_list.append(job_dict)

    # Quit the webdriver
    driver.quit()

    # Return the job list
    return job_list


query = "Python developer"
jobs = get_job_list(query)
print(jobs)