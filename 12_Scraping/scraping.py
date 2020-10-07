import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from urllib.request import urlopen
from bs4 import BeautifulSoup




from contextlib import closing
from selenium.webdriver import Firefox 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


HIDDEN = "http://192.168.1.100/.hidden"

def anchor_tag_links(incoming_url):
    url = incoming_url
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    text = soup.get_text()
    # print(text)

    all_links = soup.find_all("a")
    list_of_links = []
    for link in all_links:
        list_of_links.append(link.get("href"))
        # print(link.get("href"))
    return list_of_links[1:-1]


def start_appending():
    links_i_want = anchor_tag_links(HIDDEN)
    new_appended_list = []
    for link in links_i_want:
        new_link = HIDDEN + "/" + link
        new_appended_list.append(new_link)
    return new_appended_list


def branch_into(appended_list):
    outter_index = 0 
    inner_index = 0 
    while outter_index < len(appended_list):
        html = urlopen(appended_list[outter_index])
        saucy_soup = BeautifulSoup(html, 'lxml')
        inner_links = saucy_soup.find_all("a")
        next_level_links = []
        the_level_after = []
        for link in inner_links:
            # print(link.get("href"))
            next_level_links.append(link.get("href"))
        next_level_links = next_level_links[1:-1]

        for next_link in next_level_links:
            second_level = appended_list[outter_index] + next_link
            the_level_after.append(second_level)
        outter_index += 1

    return the_level_after

def into_the_deep(more_hidden_links):
    index = 0 
    deeper_branches = []
    into_the_deep = []
    deeper_branch_outter_index = 0
    deeper_branch_inner_index = 0
    while index < len(more_hidden_links):
        html = urlopen(more_hidden_links[index])
        saucy_soup = BeautifulSoup(html, 'lxml')
        # print(saucy_soup.get_text())
        inner_links = saucy_soup.find_all("a")
        test = []
        for link in inner_links:
            test.append(link.get("href"))
        test = test[1:-1]
        deeper_branches.append(test)
        
        index += 1
    # print(deeper_branches)
    while deeper_branch_outter_index < len(deeper_branches):
        while deeper_branch_inner_index < len(deeper_branches[deeper_branch_outter_index]):
            new_link = more_hidden_links[deeper_branch_outter_index] + deeper_branches[deeper_branch_outter_index][deeper_branch_inner_index]
            into_the_deep.append(new_link)
            deeper_branch_inner_index += 1

        deeper_branch_outter_index += 1

    return into_the_deep


def starting_to_drown(deep_end):
    index = 0 
    while index < len(deep_end):
        html = urlopen(deep_end[index])
        saucy_soup = BeautifulSoup(html, 'lxml')

        print(saucy_soup)

    with closing(Firefox()) as driver:
        driver.get(deep_end[index])
        # button = driver.find_element_by_id('deviceShowAllLink')
        continue_link = driver.find_element_by_link_text('README')
        test = continue_link.click()
        print(test)
        # wait for the page to load
        # element = WebDriverWait(driver, 10).until(
        # EC.invisibility_of_element_located((By.ID, "deviceShowAllLink"))
        # )
        # # store it to string variable
        # page_source = driver.page_source


        # inner_links = saucy_soup.find_all("a")
        # deeper_end = []
        # for link in inner_links:
        #     # print(link.get("href"))
        #     deeper_end.append(link.get_text())
        #     print(link.get("href"))
        # deeper_end = deeper_end[1:-1]

        index += 1

        


list_i_need = start_appending()
now_i_need_this = branch_into(list_i_need)
deep_end = into_the_deep(now_i_need_this)
starting_to_drown(deep_end)




