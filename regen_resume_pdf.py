"""Regenerate the canonical resume PDF (with clickable link anchors) to both
the dbhavery repo and the live-served portfolio path."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HTML = Path(__file__).parent / "resume.html"
OUTS = [
    Path(__file__).parent / "Donald_B_Havery_Resume.pdf",
    # Live site since 2026-07-02 is the static build below (served at /Donald_B_Havery_Resume.pdf).
    Path("C:/Users/dbhav/Documents/Codex/2026-06-24/c-users-dbhav-pictures-screenshots-snip/outputs/portfolio-page/Donald_B_Havery_Resume.pdf"),
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
