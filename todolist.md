Last Update: June 19
#Reviews
Modified the process using the steamreviews API. Files reviews.py and createIDlist.py are no longer needed. 
Currently downloading reviews for over 100.000 games. Approximately, 1.1 million reviews. 
Need to pickle the reviews into a single pkl. 

#NLTK
- Select the key STEM vocabulary to start tracking terms. Currently using NGSS standards big concepts following a LEXIMANCER analysis. 
- Find a way to build a list of nodes and edges based on the NLTK output. 

#NetworkX
- Seems straightforward to use. Need to revise the code to make sure it works. Should I conduct a mock of this study using only a few reviews? It seems a problem since the NLTK output will pretty much determine the outcomes of the network. 

#Visualization
Try Pypis. 

#Output
Not sure whether to use Streamlit or Jupyter. Have little experience with both of them. However, Streamlit has some easy to follow tutorials and seems easier to implement than Jupyter. 