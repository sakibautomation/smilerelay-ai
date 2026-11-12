# SmileRelay AI Website

Standalone website for **https://smilerelayai.com** and the SmileRelay AI dental-clinic communication business.

The public demo enquiry form is provided by **Zoho Forms**. Submitted enquiries are emailed to **support@smilerelayai.com**. Do not include patient information in form submissions.

## Publish to GitHub Pages

1. In this repository, go to **Settings → Pages**.
2. Under **Build and deployment**, select **Deploy from a branch**. Choose **main** and **/(root)**, then save.
3. Wait for the GitHub Pages preview at `https://sakibautomation.github.io/smilerelay-ai/`.
4. In **Pages → Custom domain**, enter **smilerelayai.com** and save.
5. At Hostinger DNS, add the GitHub Pages records shown by GitHub. **Do not delete or modify the Zoho MX, SPF, DKIM, or verification TXT records**; those are required for business email.
6. Enable **Enforce HTTPS** once GitHub issues the certificate.
7. Test the Zoho form on desktop and mobile, and verify that a submission reaches the SmileRelay AI inbox.
8. After the live site is accessible, verify the domain in Google Search Console and submit `https://smilerelayai.com/sitemap.xml`.

The chatbot on the homepage is a scripted demonstration and **does not** book appointments, send real WhatsApp messages or handle clinical issues.
