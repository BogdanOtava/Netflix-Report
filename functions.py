import pandas as pd
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
FILE = ROOT.joinpath("viewing_activity.csv")

try:
    netflix_data = pd.read_csv(FILE)
except FileNotFoundError:
    sys.exit("File could not be found in working directory. Name should be: viewing_activity.csv")
else:
    netflix_data = netflix_data.drop(["Start Time", "Attributes", "Supplemental Video Type", "Bookmark", "Latest Bookmark"], axis = 1)
    netflix_data["Duration"] = pd.to_timedelta(netflix_data["Duration"])

def list_shows(profile_name: str, order = True, dataframe=netflix_data):
    """Returns all the TV Show watched on Netflix in alphabetical order.

    Args:
        * profile_name: the name of the Netflix profile.
        * order: will returns the shows in either alphabetical order (True) or by watch order (False).  
    """

    search = dataframe[(dataframe["Profile Name"] == profile_name) & (dataframe["Duration"] > "0 days 00:01:00") & dataframe["Title"].str.contains(":")]
    search = search["Title"].str.split(":", expand = True)
    search.rename(columns = {0 : "Title", 1 : "Season", 2 : "Episode", 3 : "Other"}, inplace = True)
    search = search[~search["Title"].str.contains("Season|Recap|Teaser|Trailer")]
    title_list = []

    for i in search["Title"]:
        if i not in title_list:
            title_list.append(i)

    if order == True:
        title_list = sorted(title_list)
    else:
        title_list = reversed(title_list)

    print(f"Watched TV Shows for {profile_name}:")
    for title in title_list:
        print(title)

def watch_time(profile_name: str, dataframe=netflix_data): 
    """Returns the total watch time for the Netflix profile.

    Args:
        * profile_name: the name of the Netflix profile.
    """

    watchtime = dataframe.groupby("Profile Name").get_group(profile_name)
    watchtime_sum = watchtime["Duration"].sum()

    print(f"Total watch time for {profile_name} is: {watchtime_sum}.")

def search_activity(profile_name: str, title:str, dataframe=netflix_data):
    """Returns the amount of days/hours/minutes/seconds you spent watching the given show.

    Args:
        * profile_name: the name of the Netflix profile.
        * title: the title of the show/movie you want to see information about.
    """

    search = dataframe[(dataframe["Profile Name"].str.contains(profile_name)) & (dataframe["Title"].str.contains(title)) & (dataframe["Duration"] > "0 days 00:01:00")]
    watchtime = search["Duration"].sum()

    print(f"Total watch time for {title} is: {watchtime}.")

def watch_device(profile_name: str, dataframe=netflix_data):
    """Returns a list of devices Netflix was watched on.

    Args:
        * profile_name: the name of the Netflix profile.
    """

    watched_on = dataframe[dataframe["Profile Name"] == profile_name]
    watched_on = watched_on["Device Type"].str.split("(", expand = True)

    print(watched_on[0].value_counts())

def watch_from(profile_name: str, dataframe=netflix_data):
    """Returns a list of countries Netflix was watched from.

    Args:
        * profile_name: the name of the Netflix profile.
    """

    watched_from = dataframe[dataframe["Profile Name"] == profile_name]

    print(watched_from["Country"].value_counts())
