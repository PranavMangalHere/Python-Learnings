from playwright.async_api import Page, expect, async_playwright
import pytest

@pytest.mark.asyncio
async def test_verify():
    
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        mypage = await browser.new_page()

        myurl = await mypage.url
        await p.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        await expect(p).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
