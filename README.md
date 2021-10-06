# WARDEN
#### Video Demo:  https://youtu.be/Lg7HlKYzPVw
#### Description:
Warden was a project based on the laziness of one particular person(me), since my desktop has latency issues while opening a range of tabs at once. So I thought that the concept of centralizing the information for my own convenience was a great idea, and sought out to construct said idea. It requests information from multiple APIs for things ranging from weather to the current news, and displays the information on a host website. The website itself is made with HTML, CSS, and JS for the front-end and Python for the back-end with Bootstrap and Flask to hold it all together. The project did everything I wanted it to achieve, since the APIs grabbed the information directed at the source without bothering to load in any of the surrounding elements and images which made my desktop slow, but the user could still navigate to the original websites through the various buttons. However, the website only contains information from Thailand, since other more wide-ranging APIs usually have a subscription fee.

The website contains four icons which are weather, twitter, news, and covid information respectively. All four of these icons can be flipped over like a card to reveal the information, it also serves to hide the generation of the information which may have caused pictures to glitch into place. The weather card displays common things like temperature and chance of rain, but it also provides information on more niche topics like humidity and wind speed. Continuing from that the twitter card shows up to eight current trends in Thailand on various topics from fashion to politics. While the news card picks top-headlines from websites like the BBC, users can then click the headline to be transported to the page of the written article. Lastly, the covid summary card receives a json file from the national covid-19 database and sets each of the needed data as single variables so that they can be displayed on the website using jinja.

At first, I thought to creating an audio visualiser to sync up to some pre-made audio files that will make it look it the face itself is speaking to the user. However, after hours of testing, the element just doesn't want to cooperate and remained unfunctional. I've even tried to import code from the source as some sort of sanity check, but it still didn't work. So with a heavy heart I had to decide to scrap the idea as my understanding of the code was not at the point where I was able solve the problem. This also means that the audio files that were on my computer went unused. and were also binned with the exception of the intro sound byte that gave instruction to the user. The multiple other faces were subsequently tossed since without the audio visualizer the face lacked the animation that i wanted for Warden; since I was going towards the direction of Jarvis from Iron Man. Although that didn't work out quite as well as I wanted, I was still estatic t0 get the flip cards to work. The first card had no issue being flipped, but when it came time to the second card, it broke both itself and the first card. This issue took the rest of the day to fix, with the first or second card working on their own or neither of the cards working. That last I resorted to a "man make fire. man hit rock" way of thinking, as I found out that the cards would work perfectly if I assigned a unique ID to each and every card. It was a way of solving the problem that I wasn't proud of, but still it got the job done. Other than that, there are the usual problems when dealing with APIs , since some of the features I wanted on the website were locked behind a paywall. This meant that I had to search through multiple different sites to get an API that was both accurate and didn’t need a monthly subscription to use. However, the search did lead me to find the covid database that I am currently using for the website. 

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
