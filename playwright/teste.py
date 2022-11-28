import re
import time

from playwright.sync_api import sync_playwright, Playwright, Browser, Page, \
    expect

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context(
#         color_scheme="dark",
#         # record_video_dir='.',
#         viewport={'width':800, 'height':600}
#     )
#     page = context.new_page()
#     page.goto('http://dgg.gg')
#     print(page.title())
#     time.sleep(4)
#     context.close()


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     iphone = p.devices['iPhone 6']
#     context = browser.new_context(
#         color_scheme="dark",
#         **iphone
#     )
#     page = context.new_page()
#     page.goto('http://dgg.gg')
#     print(page.title())
#     time.sleep(4)
#     context.close()

# Imprime todos os tipos de device
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     print(p.devices.keys())

# with sync_playwright() as p:
#     request = p.request.new_context()
#     response = request.get('http://ddg.gg')
#     print(response.status)
#     print(response.status_text)
#     print(response.text())
# print(response.json())

# with sync_playwright() as p:
#     browser: Browser = p.chromium.launch(headless=False)
#     page: Page = browser.new_page()
#     page.goto('http://dgg.gg')
#     time.sleep(2)
#     page.goto('http://google.com')
#     time.sleep(2)
#     page.go_back()
#     time.sleep(2)
#     page.go_forward()
#     time.sleep(2)
#     browser.close()

print('---------------------------------------------------------')

#
# def event_handler(request_event):
#     response = request_event.response()
#     print(request_event.url)
#     print(response.status)
#
#
# with sync_playwright() as p:
#     browser: Browser = p.chromium.launch(headless=False)
#     page: Page = browser.new_page()
#     # page.on('EVENTO', CALLBACK)
#     page.on('request', event_handler)
#
#     page.goto("http://dgg.gg")
#     time.sleep(2)
#     browser.close()

# print('---------------------------------------------------------')
#
# with sync_playwright() as p:
#     browser: Browser = p.chromium.launch(headless=False)
#     page: Page = browser.new_page(
#         base_url='https://selenium.dunossauro.live/'
#     )
#
#     page.goto("aula_05_a.html")
#     # div = page.locator('div').nth(0) Tradicional
#     # div = page.locator('xpath=//*[@id="python"]') XPATH
#     # div = page.locator('#python') CSS
#     div = page.locator('id=python')  # locator playwright
#
#     h2 = page.locator('#phyton > h2')
#     print(div.text_content())
#     print(h2.text_content())
#     time.sleep(2)
#     browser.close()

print('---------------------------------------------------------')

with sync_playwright() as p:
    browser: Browser = p.chromium.launch(headless=False)
    page: Page = browser.new_page(
        base_url='https://selenium.dunossauro.live/'
    )
    page.goto("todo_list.html")
    page.locator('#todo-name').fill('Fazer Line #222')
    page.locator('#todo-desc').fill('Live com Playwright')
    page.locator('#todo-submit').click()
    page.locator('.btn.btn-primary.btn-ghost.do').click()
    card = page.locator('.terminal-card')
    title = card.locator('header')
    desc = card.locator('.description')
    expect(title).to_have_text('Fazer Line #222')
    expect(desc).to_have_text('Live com Playwright')
    expect(title).to_have_text(re.compile('.*Line.*'))
    # expect(title).not_to_have_text(re.compile('.*Line.*'))
    expect(page).to_have_title('Todo list')

    request = p.request.new_context()
    response = request.get('https://selenium.dunossauro.live/todo_list.html')
    expect(response).to_be_ok()
    page.screenshot(path='result.png', full_page=True)

    time.sleep(2)
    browser.close()
