import json
import re
from playwright.sync_api import Page, expect, sync_playwright
import os
from markdownify import markdownify as md

def test_example(page: Page) -> None:
    page.goto("https://www.linkedin.com/pulse/how-reach-out-recruiters-land-your-dream-internship-first-legagneux-7izjc/")
    selected_div = page.get_by_role("main").get_by_role("article").locator("div").filter(has_text="I've always considered my").nth(4)
    selected_div.click()
    inner_html = selected_div.inner_html()
    markdown_content = md(inner_html)
    print(markdown_content)
    with open("output.md", "w") as file:
        file.write(markdown_content)

def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        script_dir = os.path.dirname(__file__)
        auth_path = os.path.join(script_dir, '../auth.json')
        with open(auth_path, 'r') as f:
            auth_cache = json.load(f)
        context.add_cookies(auth_cache["cookies"])
        page = context.new_page()
        test_example(page)
        browser.close()

if __name__ == "__main__":
    main() 