#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import arxivscraper
import pandas as pd


# In[ ]:


scraper_cond = arxivscraper.Scraper(category='physics:cond-mat', date_from='2012-01-01', date_until='2020-07-01',timeout=10000)
output_cond = scraper_cond.scrape()


# In[ ]:


scraper_astro = arxivscraper.Scraper(category='physics:astro-ph', date_from='2012-01-01', date_until='2020-07-01',timeout=10000)
output_astro = scraper_astro.scrape()
dfastro = pd.DataFrame(output_astro,columns=cols)


# In[ ]:


cols = ('categories', 'created', 'authors')

dfcond = pd.DataFrame(output_cond,columns=cols)
dfcond.to_csv('Data/arxiv_cond_2012_2020.csv',index=False)
dfastro = pd.DataFrame(output_astro,columns=cols)
dfastro.to_csv('Data/arxiv_astro_2012_2020.csv',index=False)

