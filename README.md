# Web-Tech-2 Project

## Team:
1. Prithvi MK         (PES1201700142)
2. Harikrishnan V     (PES1201700155)
3. Chintapalli Vishal Ratnam   (PES1201701775)
## Content-Based Research Paper Recommendation and Analytics Engine

### About:

As a part of our WT-2 Project we made a Content-Based Recommendation Website to retrieve the top 10 papers for any specified topic.
<br>For <b>Front-End</b>, we are using <b>Vue JS Framework</b> which is an open-source Model–view–viewmodel JavaScript framework for building user
interfaces and single-page applications.
<br>For <b>Back-End</b>, we are using <b>Flask Framework</b> which is a micro web framework written in Python. It is classified as a microframework
because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where 
pre-existing third-party libraries provide common functions.
<br>For <b>Intelligent Component</b>, we are using a <b>Content-Based Recommender model</b> trained on ARXIV dataset to provide the recommendation
of the top 10 results along with 2 histograms for year and author statistics.

### What does our project do?

Our UI takes a "topic" as an input from the user and sends an XMLHttpRequest to the server, where the trained model produces the recommendation 
and returns it back to the UI along with 2 histograms. The first histogram shows the "Paper published related to the topic per year" and the 
second histogram shows the "Top author and number of papers".
<br>
We use submission throttling to fetch the results after the user types any character. The request goes to the server which uses RESTful API
through Flask to get the results and return it back to the Browser(Client).
<br>

### Demonstration examples can be found in the "demo" directory.
#### &nbsp;&nbsp; Or click here -> https://github.com/harikrishnanv1311/Web-Tech-2/tree/master/demo
