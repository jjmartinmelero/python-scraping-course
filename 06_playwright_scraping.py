from playwright.sync_api import sync_playwright

url = 'https://midu.dev'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto(url)

    first_course_link = page.locator('a[href*="/curso/"]').first
    first_course_link.click()

    page.wait_for_load_state()

    first_image = page.locator('img').first
    image_src = first_image.get_attribute('src')

    print(f"The first image src of the course page is: {image_src}")


    # use xpaths
    # xpath is more specific and less prone to change
    first_image = page.locator('xpath=/html/body/div[1]/div/div[1]/img')
    print(first_image.get_attribute('src'))



    browser.close() 