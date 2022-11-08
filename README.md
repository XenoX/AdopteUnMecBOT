# AdopteUnMec BOT

Script used to visit all the profiles resulting from a search.

## Requirements

- Python 3 
- Chrome or [Chromium](https://www.chromium.org/getting-involved/download-chromium/)
- [ChromeDriver](https://chromedriver.chromium.org/downloads)

## Installation

- Clone this repository
- Install dependencies
```shell
$ pip install -r requirements.txt
```
- Download [ChromeDriver](https://chromedriver.chromium.org/downloads) in root project directory and unzip it (Take the version corresponding to your installed Chrome/Chromium)
- Change `email`, `password` and `searchs` values in main.py
- (Optionnal) You can add profile(s) link(s) in `exclude_profiles_links` if you don't want to let the script visit specific profiles
- Run the script !
```shell
$ python3 main.py
```
- Enjoy 🎉