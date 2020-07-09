# COVID_pub_bias_physics
Investigating the possibility of a disproportionate impact of COVID on the academic productivity of women physicists 

## Content of repository

NOTE: All the code is in Python language

1. Data: folder with the arXiv scraped data. In the analysis I used two datasets containing the information on the arXiv submissions between January 1st, 2012 and July 1st, 2020 in the Condensed Matter and Astrophysics categories respectively. I had to compress this folder because one of the files is bigger than 25 MB. In the future I will make sure to scrape the records in batches.
2. Data_analysis files: I uploaded both the jupyter notebook used in my analysis and the .py file extracted from it. The HTML rendering of the compiled notebook is also available in order to visualize the analysis without the need to run the code.
3. Data_scraping files: the jupyter notebook and relative .py files used to scrape the arXiv records and save the .csv files.

## Description of the project

This project takes inspiration from the [work](https://github.com/drfreder/pandemic-pub-bias) of Megan Frederickson concerning the effect of the pandemic on the academic publication output of scientists. Following an [article](https://www.nature.com/articles/d41586-020-01135-9) in Nature suggesting that the restrictions imposed by the lockdown might disproportionally be affecting the productivity of women in the field, Prof. Frederickson collected information on the preprint submissions to arXiv and bioRxiv in the first few months of 2019 and 2020 to investigate this aspect further. From her analysis it appears that the impact of the pandemic has indeed negatively affected women scientists to a larger extent. 

In order to shed more light on this importan issue, I here carry out a similar analysis on a subset of arXiv submission categories, namely publications in the condensed matter and astrophysics fields, but on a longer time scale (2012-2020). I limit my attention to first and last authors as I believe that they provide the most important information on the impact on publication output.
I believe that an analysis that considers a longer period of time is important as it provides information on the overall publication trend and establishes the magnitude of the variance in the male/female publication rates. 

The steps of the analysis are explained throughout the 'Data_analysis' notebook. As mentioned above, the 'Data_scraping' notebook provides the code that I used to scrape arXiv for the authors' information. As the scraping process is rather time consuming, the 'Data_analysis' notebook directly imports the scraped data stored in the 'Data' folder. 

In order to extract the gender of the authors I use the [gender-guesser](https://pypi.org/project/gender-guesser/) package. As mentioned also by Prof. Frederickson, this type of approach has limitations and will not provide a perfectly accurate gender assignment for each entry in the data set. Nevertheless, they can provide a good aggregate overview of the male/female split. 

## Summary of conclusions

From my analysis I can conclude that, at least in the subfields that I considered, there is not a statistically relevant change in the ratio of female-to-male authorship (both in the case of first and last authors) in the first few months of 2020, when this data is compared to the trend of the past 8 years. 

I am nonetheless aware that the publication process can have an impact delayed by up to many months and I believe that this analysis will have to be regularly repeated to consider this additional factor.

## Comments

This is my first repository and Python data science project. I appreciate any comment and suggestion on how to improve it, tips on how to better present the findings in the repository, and particularly inputs on aspects of the analysis where I might have committed mistakes. 
Thanks! 
