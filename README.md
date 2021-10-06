# WARDEN
#### Video Demo:  <URL HERE>
#### Description:
Warden was a project based on the laziness of one particular person(me), since my desktop has latency issues while opening a range of tabs at once. So I thought that the concept of centralizing the information for my own convenience was a great idea, and sought out to construct said idea. It requests information from multiple APIs for things ranging from weather to the current news, and displays the information on a host website. The website itself is made with HTML, CSS, and JS for the front-end and Python for the back-end with Bootstrap and Flask to hold it all together. The project did everything I wanted it to achieve, since the APIs grabbed the information directed at the source without bothering to load in any of the surrounding elements and images which made my desktop slow, but the user could still navigate to the original websites through the various buttons. However, the website only contains information from Thailand, since other more wide-ranging APIs usually have a subscription fee.

The website contains four icons which are weather, twitter, news, and covid information respectively. All four of these icons can be flipped over like a card to reveal the information, it also serves to hide the generation of the information which may have caused pictures to glitch into place. The weather card displays common things like temperature and chance of rain, but it also provides information on more niche topics like humidity and wind speed. Continuing from that the twitter card shows up to eight current trends in Thailand on various topics from fashion to politics. While the news card picks top-headlines from websites like the BBC, users can then click the headline to be transported to the page of the written article. Lastly, the covid summary card receives a json file from the national covid-19 database and sets each of the needed data as single variables so that they can be displayed on the website using jinja.

#### TLDR:
##### How to Use the Website
- Press the Element that says click me
- interact with the four icons

##### Things Used to Create Warden
- HTML
- CSS
- JS
- Python
- Flask
- Bootstrap

##### APIs Used in the making of Warden
- Weather APIs (https://www.weatherapi.com/)
- Thailand's Covid-19 database (https://covid19.ddc.moph.go.th/)
- News API (https://newsapi.org/)
- Twitter API (https://developer.twitter.com/en/docs)