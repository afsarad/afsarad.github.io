#!/usr/bin/env python3
"""Reject publication when a Turkish page lacks an up-to-date English pair."""
from pathlib import Path
from html.parser import HTMLParser
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'index-english.html','google6aae26d58307514f.html'}
def pages():
 return {str(p.relative_to(ROOT)) for p in ROOT.rglob('*.html') if not any(x in p.relative_to(ROOT).parts for x in ('.git','en','.preview','.openai')) and p.name not in EXCLUDED}
def digest(path):return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.language='';self.alternates={};self.canonical='';self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.language=a.get('lang','')
  if tag=='link' and a.get('rel')=='alternate':self.alternates[a.get('hreflang')]=a.get('href')
  if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href')
def check():
 manifest=json.loads((ROOT/'translations.json').read_text());errors=[]
 records=manifest['pages'];actual=pages()
 if actual!=set(records):errors.append('Update translations.json: new or removed Turkish page detected: '+str(actual.symmetric_difference(records)))
 for source,entry in records.items():
  target=entry['english']
  for path,key in [(source,'source_sha256'),(target,'english_sha256')]:
   if not (ROOT/path).is_file():errors.append('Missing '+path)
   elif digest(path)!=entry[key]:errors.append('Unreviewed change: '+path+'; update both editions and their translation record together.')
  if not (ROOT/source).exists() or not (ROOT/target).exists():continue
  tr=Page((ROOT/source).read_text());en=Page((ROOT/target).read_text());url='https://afsarad.github.io/'
  if en.language!='en':errors.append('Wrong language: '+target)
  if tr.alternates.get('en')!=url+target or en.alternates.get('tr')!=url+source:errors.append('Missing reciprocal language links: '+source)
  if en.canonical!=url+target:errors.append('Wrong canonical: '+target)
 if errors:
  print('\n'.join(errors));return 1
 print(f'Validated {len(records)} Turkish–English page pairs; both editions match their reviewed content.');return 0
if __name__=='__main__':sys.exit(check())
