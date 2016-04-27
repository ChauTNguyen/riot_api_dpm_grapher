# riot_api_dpm_grapher
A week or two ago, I wanted to start a new project different from what I have been doing (GUI's, websites, etc). Eventually, I ended up wanting to play with public APIs. After a lot of searching and thinking I decided to go with Riot's API since I thought it would be the most fun as I loved analylzing League of Legends games on my off-time. My initial purpose was to graph just my friend's damage per minute for each of his last 50-100 games. However, I had to get used to Riot's API first, so what I did was play around with the API for a few hours and just practiced extracting information from the json and whatnot... Eventually, I was able to log important info such as champion played, match duration, damage per minute, and the total damage to the console.</br>

Of course, I later realized that data's only fun if you compare it with other data, and so I decided that I wanted to do some graphing! Only today (1-2 weeks since the beginning of the project) did I start graphing everything (using plotly). I had to clean up a bunch of code and modify it so that I can add in other players in a more convenient way.</br>

EXAMPLE OUTPUT IN PYCHARM (LISTS CHAMPION, GAMETIME, ETC): http://pastebin.com/gxPqcHYk</br>
![screenshot](https://raw.githubusercontent.com/ChauTNguyen/riot_api_dpm_grapher/master/dpms_line_graph.png)
![screenshot](https://raw.githubusercontent.com/ChauTNguyen/riot_api_dpm_grapher/master/avg_dpms_bar_graph.png)
