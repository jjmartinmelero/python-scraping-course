from playwright.sync_api import sync_playwright

url = 'https://midu.dev'

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    first_article_anchor = page.locator('article a').first
    first_article_anchor.click()

    page.wait_for_load_state()

    first_image = page.locator('main img').first
    image_src = first_image.get_attribute('src')

    print(f"The first src image article is: {image_src}")