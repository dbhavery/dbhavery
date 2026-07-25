"""Regenerate the canonical resume PDF (with clickable link anchors) to both
the dbhavery repo and the live-served portfolio path."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HTML = Path(__file__).parent / "resume.html"
OUTS = [
    Path(__file__).parent / "Donald_Havery_Resume.pdf",
    Path("C:/Users/dbhav/Projects/_pf_deploy/public/files/donald-havery-resume.pdf"),
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f"file:///{HTML.as_posix()}", wait_until="networkidle")
        pdf_bytes = await page.pdf(format="Letter", print_background=True)
        await browser.close()
    for out in OUTS:
        out.write_bytes(pdf_bytes)
        print(f"wrote {len(pdf_bytes)} bytes -> {out}")

asyncio.run(main())
