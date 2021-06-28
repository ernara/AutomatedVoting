from asyncio import wait
from telnetlib import EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from tbselenium.tbdriver import TorBrowserDriver
import time
from multiprocessing import Pool
import math
from screeninfo import get_monitors


# Your vote function
def vote(args):
    for a in range(args[4]):
        with TorBrowserDriver("/home/ernestas/Desktop/tor-browser_en-US") as driver:
            driver.set_window_rect(x=args[0], y=args[1], width=args[2], height=args[3])

            driver.set_page_load_timeout(60)

            try:
                driver.get(
                    'https://apklausa.lt/f/ar-reikia-padaryti-naujas-gyvenvietes-p5sma7d/answers/new.fullpage')
                driver.find_element_by_css_selector("[data-id='11577040']").click()
                driver.find_element_by_css_selector(".submit").send_keys(Keys.ENTER),
                time.sleep(10)
            finally:
                driver.close()


# Your vote_parallel function
def vote_parallel(threads, votes):
    width = 0
    height = 0
    for m in get_monitors():
        width = m.width
        height = m.height

    n = math.ceil(math.sqrt(threads))

    array = []

    size_x = width / n
    size_y = height / n

    count = 0

    for y in range(n):
        for i in range(n):
            if count <= threads:
                array.append([width / n * i, height / n * y, size_x, size_y, int(votes / threads)])
                count += 1

    pool = Pool(threads)
    pool.map(vote, array)


def main():
    count = 9
    votes = 10
    vote_parallel(count, votes)


if __name__ == "__main__":
    main()
