import requests

with open("valid_proxy.txt", "r") as f:
    proxies = f.read().split("\n")


sites_to_check = ["https://magicpin.in/", "https://google.com/", "https://www.wikipedia.org/"]

counter = 0

for site in sites_to_check:
    try:
        print(f"Using the proxy: {proxies[counter]}")
        res = requests.get(site, proxies={"http": proxies[counter],
                                          "https": proxies[counter]})
        print(res.status_code)
        print(res.text)
    except:
        print("Failed")
    finally:
        counter += 1
        counter % len(proxies)

