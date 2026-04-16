import os
import asyncio
from playwright.async_api import async_playwright

PAGE_URL = "https://www.facebook.com/profile.php?id=61572126032952" 

async def run_fb_bot(email, password):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        try:
            print(f"--- {email} শুরু হচ্ছে ---")
            await page.goto("https://m.facebook.com/login")
            await page.fill('input[name="email"]', email)
            await page.fill('input[name="pass"]', password)
            await page.click('button[name="login"]')
            await page.wait_for_timeout(5000) 
            print(f"✅ {email} লগইন হয়েছে!")
        except Exception as e:
            print(f"❌ এরর: {e}")
        await browser.close()

async def main():
    for i in range(1, 6):
        email = os.getenv(f'FB_EMAIL_{i}')
        password = os.getenv(f'FB_PASS_{i}')
        if email and password:
            await run_fb_bot(email, password)

if __name__ == "__main__":
    asyncio.run(main())
    
