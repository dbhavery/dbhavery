# Deprecated résumé-PDF artifacts

- **Donald_Havery_Resume_Updated.STALE.pdf** — old single-path PDF, NO clickable
  links, pre-2026-06-22 content. Misleading "_Updated" name; it is NOT current.
  The canonical résumé is `../Donald_Havery_Resume.pdf` (clickable links, current).
- **generate_pdf.py.superseded** — old generator that wrote the stale `_Updated`
  filename. Superseded by `../regen_resume_pdf.py`, which renders from
  `resume.html` (now with `<a href>` link annotations) to BOTH the repo PDF and
  the live-served copy at `_pf_deploy/public/files/donald-havery-resume.pdf`.

To regenerate the résumé PDF: `python ../regen_resume_pdf.py`
