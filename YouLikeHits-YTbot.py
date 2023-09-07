# YOUTUBE VIDEO BOT
# when the first window opens, you must quickly enter the captcha and then the bot will run normal. It will always have 2 youtube windows open. 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

driver.get('https://www.google.com/')
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
# the class to manage bot's features
class YLH:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.options = Options()
        self.options.add_argument("--lang=en")
        self.bot_ylh = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options = self.options)

    # this method will open the login link, fill the form and click login button
    def open_link(self):
        bot_ylh = self.bot_ylh
        bot_ylh.get("https://www.youlikehits.com/login.php")
        username = bot_ylh.find_element(By.NAME, "username")
        username.send_keys(self.username)
        password = bot_ylh.find_element(By.NAME, "pass")
        password.send_keys(self.password)
        button = bot_ylh.find_element(By.XPATH, "/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/center/form/table/tbody/tr[3]/td/span/input").click()
        time.sleep(5)
        testBOT.ylh_loop()
        
    # this method loop the actions for earn point
    def ylh_loop(self):
        bot_ylh = self.bot_ylh
        bot_ylh.get("https://www.youlikehits.com/youtubenew2.php")
        
        time.sleep(10)

        try:
            bot_ylh.find_element(By.CLASS_NAME, "followbutton").click()
        except:
            None

        while len(bot_ylh.window_handles) > 2:
            time.sleep(1)
            print("I am snatching points for you...")
            print("The next video will play soon")
            
        testBOT.ylh_loop()

# Fill the line below with your Youlikehits username and your password
testBOT = YLH("username", "password")
testBOT.open_link()
