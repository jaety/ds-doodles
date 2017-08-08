What does it take to do data science in this day and age? I'm rusty, and this is going to be my blog to polish up my understanding.

The heart of data science certainly hasn't changed
* Find Data
* Clean Data
* Analyze to Find Insights
* Write about those insights

## 8/8/17

* TODO: resample takes '5Min' in this example: https://pandas.pydata.org/pandas-docs/stable/timeseries.html#up-sampling but I can find
  no documentation that explains what's possible. Can I do a decade for instance? 10A works

## 8/7/17

* Learned today that Pandas supports rich Period math

## 8/5/17

* The World Bank is easily accessible from Python. Someone's done all the work already. Does it make sense that we should have to pull it into Scala? Hypothesis: Let's truly, natively support polyglot.

## 8/4/17

Re-envisioning the pipeline.

1. I need a space to find & investigate data. As a starting point, use pandas + wbdata + notebook from previous exploration. This lets me find individual indicators. 03_DataPipeline.
2. Now, I want an isolation layer between my work environment and outside sources, so I need a way to register indicators into my own space. Started creating 'domain' in lib to represent this. Very much a placeholder. Need to talk about, for instance, row level security, and how these are propagated into different languages.
3. For lightweight manipulation in scala, I found Framian https://github.com/tixxit/framian/wiki/Framian-Guide. We can look at spark, but I'd like something lighterweight for now while just messing around. [Quick introduction (and other comparisons here)](https://darrenjw.wordpress.com/tag/framian/)
4. Framian didn't really go anywhere. Turned to spark, and it's up and running. I had to compile the Country case class outside of the notebook, so that it was an outer class. Took a long while to figure out how to add the cwd to the classpath. Took longer to realize I'd compiled Country.scala against the wrong version of scala. It needed to be 2.11 to match jupyter-scala's spark.
5. List of spark's operations on RDD's: https://spark.apache.org/docs/latest/rdd-programming-guide.html#transformations

## 7/9/17
For today's exercise, finding some interesting data. Little bit of googling around took me to this page: https://www.dataquest.io/blog/free-datasets-for-projects/ and, mostly at random, decided to look into the World Bank (#12)

The World Bank has a detailed API, and Oliver Sherouse has been kind enough to write a Python wrapper around it. http://wbdata.readthedocs.io/en/latest/

* note that wbdata.get_indicator? in a notebook, is massively powerful. Drastically changes my workflow. (Admittedly more when you're getting to know a new library)

Separately, I'm going to start this little static, markdown based blog. Rendering pipeline for that.
