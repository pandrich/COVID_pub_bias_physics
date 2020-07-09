# COVID_pub_bias_physics
Investigating the possibility of a disproportionate impact of COVID on the academic productivity of women physicists 

## Description of the project

This project takes inspiration from the [work](https://github.com/drfreder/pandemic-pub-bias) of Megan Frederickson concerning the effect of the pandemic on the academic publication output of scientists. Following an [article](https://www.nature.com/articles/d41586-020-01135-9) in Nature suggesting that the restrictions imposed by the lockdown might disproportionally be affecting the productivity of women in the field, Prof. Frederickson collected information on the preprint submissions to arXiv and bioRxiv in the first few months of 2019 and 2020 to investigate this aspect further. From her analysis it does appear that indeed the impact of the pandemic has negatively affected women scientists more greatly. 

In order to shed more light on this importan issue, we here carry out a similar analysis on a subset of arXiv submission categories, namely publications in the condensed matter and astrophysics fields, but on a longer time scale (2012-2020). We limit our attention to first and last authors as we think that they provide the most important information on the impact on publication output.
We believe that an analysis that considers a longer period of time is important as it looks at the overall publication trend and establishes the magnitude of the variance in the male/female publication rates. 

All the passages of the analysis are explained in the 'Data Analysis' notebook (in Python language) in this repository. The 'Data Scraping' notebook provides the code that was used to scrape arXiv for the authors' information. As the scraping process is rather time consuming, the 'Data Analysis' notebook directly imports the scraped data in the 'Data' folder of this repository. 

In order to extract the gender of the publications' authors we use the [gender-guesser](https://pypi.org/project/gender-guesser/) package. As mentioned also by Prof. Frederickson, these approaches have limitations and will not provide a perfectly accurate gender assignment for each entry in the data set. Nevertheless, they can provide a good aggregate overview of the male/female split. 

## Summary of conclusions

From our analysis we can conclude that, at least in the subfields that we considered, there is not a statistically relevant change in the ratio of female-to-male authorship (both in the case of first and last authors) in the first few months of 2020 when this data is compared to the trend of the past 8 years. 

We are nonetheless aware that the publication process can have an impact delayed by up to many months and we believe that this analysis will have to be regularly repeated to consider a possible later emergence of a disproportionate effect of the pandemic on the output of female scientists
