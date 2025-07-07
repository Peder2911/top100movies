
# Top 100 movies

Find something to watch!

Use this tool to download the top 100 movies of the 21st. centry list from IMDB, and put all of the movies into an sqlite database. This database can then be queried to figure out what movie you should watch tonight.

Warning: I wrote this in 10 minutes, it is not even remotely good code, but I found it useful and wanted to share!

## Usage

```
git clone https://github.com/peder2911/top100movies
cd top100movies
python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt
python3 . init
python3 . pick 
```
