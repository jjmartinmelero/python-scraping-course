from playwright.sync_api import sync_playwright

url = 'https://midu.dev'

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)

    first_course_link = page.locator('a[href*="/curso/"]').first
    first_course_link.click()

    page.wait_for_load_state()

    first_image = page.locator('img').first
    image_src = first_image.get_attribute('src')

    print(f"The first image src of the course page is: {image_src}")

    browser.close()