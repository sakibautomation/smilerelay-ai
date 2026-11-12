from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
import re

BASE=Path(__file__).resolve().parent.parent
PAGES=["index.html","services.html","about.html","pricing.html","contact.html","privacy.html","terms.html","refunds.html","delivery.html"]
class Links(HTMLParser):
    def __init__(self):
        super().__init__();self.targets=[];self.ids=set();self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get("id"):self.ids.add(a["id"])
        if tag in ("a","script","link","iframe"):
            url=a.get("href",a.get("src",""))
            if url:self.links.append((tag,url))
    handle_startendtag=handle_starttag

parsed={}
for page in PAGES:
    html=(BASE/page).read_text(encoding="utf-8")
    p=Links();p.feed(html);parsed[page]=p
    assert "<title>" in html, f"{page} missing title"
    assert "rel=\"canonical\"" in html, f"{page} missing canonical"
    for tag,url in p.links:
        if url.startswith(("https://","http://","mailto:","data:")):continue
        path,_,fragment=url.partition("#")
        if not path and fragment:assert fragment in p.ids,f"{page} missing #{fragment}"
        if path and path!="./":
            target=BASE/path
            assert target.is_file(),f"{page}: missing local file {path}"
            if fragment and target.suffix==".html":
                other=parsed.get(path)
                if other is None:
                    other=Links();other.feed(target.read_text(encoding="utf-8"))
                assert fragment in other.ids, f"{page}: {url} has missing target"
assert "forms.zohopublic.com/supportsmiler1" in (BASE/"index.html").read_text(), "Zoho embed missing"
assert (BASE/"CNAME").read_text().strip()=="smilerelayai.com", "custom domain changed"
assert all(x in (BASE/"index.html").read_text() for x in ('id="workflow-lab"','id="enquiry-count"','id="demo-type-form"')), "interactive controls missing"
root=ET.parse(BASE/"sitemap.xml").getroot()
links=[x.text for x in root.iter() if x.tag.endswith("loc")]
assert len(links)>=len(PAGES) and all(x.startswith("https://smilerelayai.com/") for x in links), "sitemap incomplete"
assert len(set(links))==len(links), "duplicate sitemap links"
print("Verified",len(PAGES),"pages, local links, anchors, demo integration, CNAME and sitemap.")
