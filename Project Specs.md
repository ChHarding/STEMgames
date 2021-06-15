# STEMgames
General description of the project (2 pts)

This application will create a semantic network for analysis of the hidden STEM (Science, Technology, Engineering, and Mathematics) curriculum in popular video games by showing how scientific concepts are often popularized in video games. 

Using Steam reviews of the games with highest ratings, the network will display:
Which scientific concepts are more often explored in video games. 
How game genres and themes correlate with scientific concepts. 
How games incorporate those concepts. 
How they can be utilized to support science education standards (a) scientific and engineering practices, (b) croscutting concepts, and (c) core ideas. 

Researchers in game studies and educators will use this application to visualize game networks based on their approximation to STEM concepts. This will help users identify games based on their characteristics and use them for research or educational purposes. 

Additionally, I will conduct an analysis of the network using specific terminology about data science to learn how data science concepts are utilized in video games. 

External mechanisms:

Scraping data: STEAM review download API
Building database, parsing text, and analyzing language: NLTK package
Building the network: NetworkX
Visualization: Pyvis

GUI
First, I will create a Streamlit web app for users to interact with the network and to showcase some specific analysis. Streamlit does not seem to support Pyvis, so I may use st.graphviz_chart instead to export the graphs to the web. 

Task Vignettes (User activity "flow") (4 pts)
The Jupyter notebook will include a tutorial for game studies researchers interested in creating their own visualizations using the databases I scraped for this network. This is a way to encourage other researchers and practitioners to engage in network analysis using game data. 

Task 1: Exploring games
User wants to explore which games can be used for a research study around the use of algebra in videogames. First, the user will be able to click on any circle in the network and find a videogame with basic data (date of publication, number of reviews, genre). The larger the circle, the more occurrences of scientific concepts being used by reviewers to describe the game. 

Task 2: Exploring connections 
By clicking on the edges of the games, the user will find what types of concepts are more often found across games. For example, some games may involve concepts of viruses and pandemics. By clicking on an edge about viruses, the user will be able to explore the network of games that incorporate those concepts. 

Task 3: Exploring usage
Once the user has identified a collection of games that incorporate a scientific concept, they will be able to run a query to find the use of the terms in context. In this way, the researcher will be able to determine whether how the term is being used. 

Task 4: Conducting an analysis 
The user will also be able to use interactive widgets to narrow down the search. For example, the user can look for games within certain genres and year of publishing to render a new visualization of the network. By filtering and sorting data, the visualization could help users identify, for example, how the use of concepts such as surveillance, machine learning and data science has evolved over time in video games. 

Task 5: Saving the report
The user will be able to save the output from the analysis for future reference. 




Technical "flow" (3 pts)
Data collection

The first stage of this construction will require mostly manual work as the API requires the user to find all the ID numbers for the STEAM games. The games will be selected based on popularity in the last 10 years, and it will exclude games tagged as “educational games”, “learning games”, “maths”, “science”, etc. Once I have all the IDs, the API will create a document with all the reviews. 

Language Processing

Extract all sentences in which the scientific concept words are used. Identify the part of speech of the words and parse the sentences using a POS tagger. 
Extract the context of each selected concept as it appeared in all the reviews. These are words which appear in close proximity of the concepts. For the context, we can select words we are interested in such as verbs or adjectives thus avoiding functional vocabulary. 
Choose the most frequent context words and represent each word by the context words. This will allow us to create a matrix with concepts, context words, and games. 
Create word clusters foro each concept to determine whether it is possible to derive categories of conceptualizations from the reviews. This will require the nltk.cluster function. 

Network Analysis

Create the nodes for the analysis in NetworkX. At this point, I expect the scientific concepts to become the nodes. This may change to the games as nodes depending on the results of the natural language processing analysis. 
Create edges. At this point, I expect these words to be the context words we found earlier as long as the game tags. 
Import the data to NetworkX
Create graph and add attributes for further analysis. 

Visualization
Import data from NetworkX to Pyvis. 
Get an interactive network.

Deployment
Create a webapp using Streamlit

Unknowns
It is difficult to tell how the natural language processing will go. Maybe, I won’t find meaningful context clusters for the concepts, and I may need to change the strategy to find relevant data. In general, language processing always drops interesting data, but it may not be the data I was originally looking for. This means that the outcomes of the graph and visualizations may differ from my current expectations. 





