What does it take to do data science in this day and age? I'm rusty, and this is going to be my blog to polish up my understanding.

The heart of data science certainly hasn't changed
* Find Data
* Clean Data
* Analyze to Find Insights
* Write about those insights

## 8/4/17

Re-envisioning the pipeline.

1. I need a space to find & investigate data. As a starting point, use pandas + wbdata + notebook from previous exploration. This lets me find individual indicators. 03_DataPipeline.
2. Now, I want an isolation layer between my work environment and outside sources, so I need a way to register indicators into my own space. Started creating 'domain' in lib to represent this. Very much a placeholder. Need to talk about, for instance, row level security, and how these are propagated into different languages.
3. For lightweight manipulation in scala, I found Framian https://github.com/tixxit/framian/wiki/Framian-Guide. We can look at spark, but I'd like something lighterweight for now while just messing around. [Quick introduction (and other comparisons here)](https://darrenjw.wordpress.com/tag/framian/)

## 7/9/17
For today's exercise, finding some interesting data. Little bit of googling around took me to this page: https://www.dataquest.io/blog/free-datasets-for-projects/ and, mostly at random, decided to look into the World Bank (#12)

The World Bank has a detailed API, and Oliver Sherouse has been kind enough to write a Python wrapper around it. http://wbdata.readthedocs.io/en/latest/

* note that wbdata.get_indicator? in a notebook, is massively powerful. Drastically changes my workflow. (Admittedly more when you're getting to know a new library)

Separately, I'm going to start this little static, markdown based blog. Rendering pipeline for that.
