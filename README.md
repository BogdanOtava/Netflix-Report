## About The Project

It was made entirely in Python and it uses the pandas library for reading and manipulating the dataset. The program facilitates getting some information about your Netflix watch time, TV Shows, used devices for watching, or where it was watched from.

## Getting Started
### External dependencies & services
From the Netflix account we can download our personal information, which includes a copy of our entire viewing activity on Netflix. We can request a copy of this data  and will receive it within 24 hours. Submit a request for the information from:

`Account -> Settings -> Download your personal information -> Submit Request`

### Prerequisites

  * [pandas](https://pandas.pydata.org/) -> data manipulation and analysis tool built on top of Python.
  
  `pip install pandas`
  
## How To Use
The functions are written in *functions.py* file along with documentation for each one of them. Refer to the documentation for more information about how it works.

For instance, let's say we have a profile named __John__ and we want to see __John's__ activity on Netflix. Give as first argument the profile name and the TV Show as second argument to see the watch time for it.

  * List all TV Shows watched on profile
  
  `list_shows("John")`
  
  * Get total watch time on profile
  
  `watch_time("John")`
  
  * Get total watch time for a particular TV Show
  
  `search_activity("John", "Friends")`
  
  * List the devices Netflix was watched on
  
  `watch_device("John")`
  
  * List all countries Netflix was watched from
  
  `watch_from("John")`
