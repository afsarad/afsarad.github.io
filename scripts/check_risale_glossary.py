#!/usr/bin/env python3
"""Every word in a published Risale excerpt must have a glossary entry."""
from pathlib import Path
from html.parser import HTMLParser
import json,re,sys,unicodedata
ROOT=Path(__file__).resolve().parents[1]
bundle=(ROOT/'assets/risale-lugat-01.js').read_text()
data=json.loads(re.search(r'const all=(.*);\nconst entries=',bundle).group(1))
token=re.compile(r"[^\W\d_]+(?:['’‘\-‑–]+[^\W\d_]+)*",re.UNICODE)
def key(word,lang):
 if lang=='en':return word.lower()
 word=unicodedata.normalize('NFC',word).replace('İ','i').replace('I','ı').lower()
 return word.translate(str.maketrans({"’":"'","‘":"'","`":"'","‑":"-","–":"-","â":"a","à":"a","î":"i","ì":"i","û":"u","ù":"u"}))
class Page(HTMLParser):
 def __init__(self,s):
  super().__init__();self.lang='tr';self.inside=False;self.words=[];self.feed(s)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang','tr')
  if tag=='blockquote' and 'risale-original' in a.get('class','').split():self.inside=True
 def handle_endtag(self,tag):
  if tag=='blockquote':self.inside=False
 def handle_data(self,s):
  if self.inside:self.words.extend(token.findall(s))
errors=[];count=0
for path in list(ROOT.glob('risale-*.html'))+list((ROOT/'en').glob('risale-*.html')):
 page=Page(path.read_text())
 for word in page.words:
  if key(word,page.lang) not in data.get(page.lang,{}):errors.append(f'{path.name}: missing {page.lang} glossary word {word}')
 count+=len(page.words)
if errors:print('\n'.join(errors));sys.exit(1)
if not count:print('No Risale excerpts checked.');sys.exit(1)
print(f'Validated every word in Risale excerpts: {count} word occurrences across Turkish and English.')
