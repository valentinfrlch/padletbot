# get links for images from google
import requests
# import BeautifulSoup
from bs4 import BeautifulSoup


def get_images(searchquery):
    # search google for images of cats
    search_url = "https://www.google.com/search?q=" + searchquery + "&source=lnms&tbm=isch"
    # open the search url
    response = requests.get(search_url)
    # parse the html using beautiful soup
    soup = BeautifulSoup(response.text, "html.parser")
    # find all the images
    images = soup.findAll("img")
    # get the src attribute for each image
    links = [img.get("src") for img in images]
    return links

def get_videos(searchquery):
    search_url = "https://www.google.com/search?q=" + searchquery + "&source=lnms&tbm=vid"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "html.parser")
    # find all videos
    videos = soup.findAll("video")
    # get the src attribute for each video
    links = [vid.get("src") for vid in videos]
    return links