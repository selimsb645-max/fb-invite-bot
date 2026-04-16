import os
import asyncio
from playwright.async_api import async_playwright

# তোমার পেজের লিংক এখানে বসাও
PAGE_URL = "https://www.facebook.com/profile.php?id=61572126032952" 

async def run_fb_bot(email, password):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        try:
            print(f"--- {email} দিয়ে কাজ শুরু ---")
            # ১. ফেসবুক লগইন
            await page.goto("https://m.facebook.com/login")
            await page.fill('input[name="email"]', email)
            await page.fill('input[name="pass"]', password)
            await page.click('button[name="login"]')
            await asyncio.sleep(7) 

            # ২. ফ্রেন্ড রিকোয়েস্ট পাঠানো (যাতে তারা পরে ইনভাইট পায়)
            print("ফ্রেন্ড সাজেশনে গিয়ে রিকোয়েস্ট পাঠানো হচ্ছে...")
            await page.goto("https://m.facebook.com/friends/center/suggestions")
            for _ in range(unlimited): # আপাতত unlimited জন করে টেস্ট করি
                try:
                    await page.click('text="Add Friend"', timeout=3000)
                    await asyncio.sleep(2)
                except: break

            # ৩. পেজে গিয়ে সবাইকে ইনভাইট করা
            print("পেজে গিয়ে ইনভাইট অপশন খোঁজা হচ্ছে...")
            await page.goto(PAGE_URL)
            # এখানে ইনভাইট বাটন খোঁজার চেষ্টা করবে বট
            
            print(f"✅ {email} এর কাজ শেষ!")
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
    
