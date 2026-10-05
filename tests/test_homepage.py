import json, unittest
from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
class HomepageTests(unittest.TestCase):
 def setUp(self):
  self.text=(ROOT/'_pages/about.md').read_text(); self.html=BeautifulSoup(self.text,'html.parser')
 def test_scholar_coverage(self):
  papers=json.loads((ROOT/'_data/publications.json').read_text())
  self.assertEqual(len(papers),8)
  for p in papers:
   self.assertIn(p['title'].replace('&','&amp;'),self.text)
   self.assertIn('Juyuan Wang',p['authors']); self.assertTrue(p['scholar'].startswith('https://scholar.google.com/'))
  weseal=next(p for p in papers if p['title'].startswith('WeSEAL'))
  self.assertTrue(weseal['authors'].startswith('Juyuan Wang, Chenxing Wang'))
  self.assertIsNone(weseal['code'])
 def test_gallery(self):
  self.assertEqual(len(self.html.select('.moment-group')),4)
  photos=self.html.select('.moment-grid img');self.assertEqual(len(photos),12)
  for photo in photos:
   self.assertTrue((ROOT/photo['src'].lstrip('/')).is_file())
   self.assertTrue(photo['alt']); self.assertEqual(photo['loading'],'lazy')
 def test_no_empty_links(self):
  for a in self.html.select('a'):self.assertTrue(a.get('href'))
 def test_profile_and_views(self):
  self.assertNotIn('an undergraduate student',self.text)
  self.assertIn('2024.09 - Present',self.text)
  self.assertEqual(len(self.html.select('#full-publications li')),9)
  self.assertTrue(self.html.select_one('#full-publications').has_attr('hidden'))
 def test_updated_papers_and_logos(self):
  papers=json.loads((ROOT/"_data/publications.json").read_text())
  self.assertEqual(len(self.html.select(".updated-publication")),6)
  for title,venue,image in [("PonsRAG","EMNLP 2026","ponsrag.png"),("When & How","SIGIR 2026","wewrite.png")]:
   p=next(p for p in papers if p["title"].startswith(title))
   self.assertIn(venue,p["venue"]); self.assertIn("Accepted",p["venue"])
   self.assertEqual(p["image"],image); self.assertTrue((ROOT/"images"/image).is_file())
  logos=self.html.select(".experience-logo")
  self.assertEqual(logos[0]["src"],"/images/logos/wechat-search.png")
  self.assertEqual(logos[2]["src"],"/images/logos/wechat-prc.png")
  for logo in logos:self.assertTrue((ROOT/logo["src"].lstrip("/")).is_file())
 def test_timeline_services_and_xjtu(self):
  events=json.loads((ROOT/'_data/news.json').read_text())
  dates=[e['date'] for e in events]
  self.assertEqual(dates,sorted(dates,reverse=True))
  self.assertEqual(len(self.html.select('.news-list li')),len(events))
  for e in events:self.assertIn(e['body_html'],self.text)
  for venue in ['AAAI','ACM MM','SIGIR','EMNLP','CVPR','ICLR','WWW','KDD','ARR','ISCTIS','ICIHCS']:self.assertIn(venue,self.text)
  self.assertIn('2023 - 2024',self.text)
  self.assertTrue((ROOT/'images/logos/xjtu.png').is_file())
  aaai=self.html.select('.moment-group')[1]
  self.assertEqual(len(aaai.select('figure')),3)
 def test_enriched_experience_and_acmmm(self):
  cards=self.html.select('.experience-card')
  self.assertEqual(len(cards),6)
  for card in cards:self.assertTrue(card.select_one('.experience-info span'))
  self.assertIn('vLLM/FlashAttention',cards[0].get_text())
  self.assertIn('Agent harness',cards[1].get_text())
  self.assertIn('LoRA',cards[2].get_text())
  self.assertEqual(cards[4].select_one('a')['href'],'https://www.ai4bread.com/')
  group=self.html.select('.moment-group')[2]
  self.assertIn('ACM MM 2025',group.h3.get_text())
  self.assertEqual(len(group.select('figure')),3)
  self.assertTrue(group.select_one('img')['src'].endswith('acmmm-dublin-conference.jpg'))
 def test_personal_favicon(self):
  head=BeautifulSoup((ROOT/'_includes/head/custom.html').read_text(),'html.parser')
  self.assertIn('personal-logo.png?v=20261006',head.select_one('link[rel="icon"]')['href'])
  self.assertEqual(head.select_one('link[rel="icon"]')['type'],'image/png')
  self.assertIsNone(head.select_one('link[rel="mask-icon"]'))
  manifest=json.loads((ROOT/'images/manifest.json').read_text())
  self.assertEqual(manifest['name'],'Juyuan Wang')
  self.assertTrue((ROOT/'images'/manifest['icons'][0]['src'].split('?')[0]).is_file())
 def test_navigation(self):
  self.assertIn('/#moments',(ROOT/'_data/navigation.yml').read_text())
  for file in ['assets/css/home.css','assets/js/show_publications.js']:self.assertTrue((ROOT/file).is_file())
if __name__=='__main__':unittest.main()
