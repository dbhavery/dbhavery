"""Generate Donald_Havery_Resume_Updated.pdf from resume.html using Playwright."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HTML_PATH = Path(__file__).parent / "resume.html"
PDF_PATH = Path(__file__).parent / "Donald_Havery_Resume_Updated.pdf"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f"file:///{HTML_PATH.as_posix()}", wait_until="networkidle")
        await page.pdf(
            path=str(PDF_PATH),
            format="Letter",
            print_background=True,
        )
        await browser.close()
        print(f"PDF written to: {PDF_PATH}")

asyncio.run(main())
