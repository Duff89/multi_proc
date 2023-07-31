import random
import time
from seleniumwire import undetected_chromedriver as uc
import multiprocessing

def get_whoer(proxy: str):
    ip, port, login, password = proxy.split(":")
    time.sleep(random.randint(1, 7))
    wire_options = {
        'proxy': {
            'https': f'https://{login}:{password}@{ip}:{port}',
        }
    }
    options = uc.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = uc.Chrome(version_main=108, seleniumwire_options=wire_options, options=options)
    driver.get("https://whoer.net/")
    time.sleep(15)
    driver.quit()


if __name__ == '__main__':
    """ip:port:login:password"""
    proxy_list = list(map(str.rstrip, open('proxy.txt').readlines()))
    with multiprocessing.Pool(processes=4) as p:
        p.map(get_whoer, proxy_list)


