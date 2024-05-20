import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


def download_files(download_url, download_path, driver_path, total_pages):
    # Configure Firefox options
    firefox_options = Options()
    firefox_options.set_preference('browser.download.folderList', 2)  # Use custom download path
    firefox_options.set_preference('browser.download.manager.showWhenStarting', False)
    firefox_options.set_preference('browser.download.dir', download_path)
    firefox_options.set_preference('browser.helperApps.neverAsk.saveToDisk',
                                   'application/octet-stream')  # Adjust MIME type if needed

    # Create a service for GeckoDriver
    service = Service(driver_path)

    # Initialize the WebDriver
    driver = webdriver.Firefox(service=service, options=firefox_options)

    try:
        # Navigate to the URL
        driver.get(download_url)

        # Find the select element by CSS selector and click it
        select_element = driver.find_element(By.CSS_SELECTOR,
                                             '#tblControl_length > label:nth-child(1) > select:nth-child(1)')
        select_element.click()

        # Wait for a brief moment to ensure the dropdown options are loaded
        time.sleep(1)

        # Find the option element by CSS selector and select it
        option_element = driver.find_element(By.CSS_SELECTOR,
                                             '#tblControl_length > label:nth-child(1) > select:nth-child(1) > option:nth-child(4)')
        option_element.click()

        # Loop through each page
        for page_number in range(1, total_pages + 1):
            # Wait for the page to load
            time.sleep(10)  # Adjust time as needed

            # Scroll to the bottom of the page to ensure the button is visible
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Find and click the download button by its class name
            try:
                download_button = driver.find_element(By.CLASS_NAME, 'buttons-csv')

                # Scroll to the download button
                driver.execute_script("arguments[0].scrollIntoView();", download_button)

                # Click the download button
                download_button.click()

                # Wait for the download to complete
                time.sleep(10)  # Adjust time based on file size and connection speed
            except Exception as e:
                print(f"An error occurred on page {page_number}: {e}")

            # Scroll to the next page button
            next_page_button = driver.find_element(By.XPATH, f'//a[text()="{page_number + 1}"]')
            driver.execute_script("arguments[0].scrollIntoView();", next_page_button)

            # Navigate to the next page if not the last page
            if page_number < total_pages:
                try:
                    next_page_button.click()
                except Exception as e:
                    print(f"Failed to navigate to page {page_number + 1}: {e}")
                    break

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    # URL of the webpage with the download link
    url = 'https://sullygnome.com/channels/2023/watched?language=en'  # Replace with the actual URL

    # Path to save the downloaded files
    download_dir = '/path/to/your/downloads'  # Replace with your desired download path

    # Path to the GeckoDriver executable
    gecko_driver_path = '/Users/miki/Documents/geckodriver'  # Replace with the actual path to your GeckoDriver

    # Total number of pages to navigate
    total_pages = 5  # Adjust based on the number of pages available

    # Call the function to download the files
    download_files(url, download_dir, gecko_driver_path, total_pages)
