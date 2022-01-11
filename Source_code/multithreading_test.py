""" 
CPU - 4 Core (4 Thread)  - Python will take One thread (In python that can crete N number of threads)

So (i.e) if 4 requests use one thread menas it will hit and that response delay time another req will hit like that. 

"""

import grequests, requests
from datetime import datetime
import threading, time
import multiprocessing

start_time = datetime.now()

class Test:
    def __init__(self):
        self.urls = open("urls.txt","r").read().split("\n")
        print(f"TOTAL SIZE : {len(self.urls)}")

        self.domains = open("host.txt","r").read().split("\n")
        print(f"TOTAL SIZE : {len(self.domains)}")

        self.ips = open("ip.txt","r").read().split("\n")
        print(f"TOTAL SIZE : {len(self.ips)}")

        self.sync_urls()
        self.sync_domains()
        self.sync_ips()
        # self.sync_urls()
        # self.sync_domains()
        # self.sync_ips()


    def exception(self, request, exception):
        print("Problem: {}: {}".format(request.url, exception))

    def async_(self):
        print("async call received")
        results = grequests.map((grequests.get("https://ADDRESS/dns/host?host="+u) for u in self.urls), exception_handler=self.exception, size=5)
        print(results)
        for i in results:
            print(str(datetime.now()),">> ", i.json())
    
    def sync_urls(self):
        def current():
            print("sync_urls call received")
            count = 1
            for input in self.urls:
                try:
                    url = f"https://ADDRESS/dns/url?url={input}"
                    resp = requests.get(url)
                    print(f"{count} URL >> ",resp.json())
                    count += 1
                except Exception as ex:
                    print(ex)
                    pass
            print("SYNC Process Completed")
        threading.Thread(target = current).start()
        # multiprocessing.Process(target=current).start()
    
    def sync_domains(self):
        def current():
            print("sync_domains call received")
            count = 1
            for input in self.domains:
                try:
                    url = f"https://ADDRESS/dns/host?host={input}"
                    resp = requests.get(url)
                    print(f"{count} HOST >> ", resp.json())
                    count += 1
                except Exception as ex:
                    print(ex)
                    pass
            print("sync_domains Process Completed")
        threading.Thread(target = current).start()
        # multiprocessing.Process(target=current).start()


    def sync_ips(self):
        def current():
            print("sync_ips call received")
            count = 1
            for input in self.ips:
                try:
                    url = f"https://ADDRESS/dns/ip?ip={input}"
                    resp = requests.get(url)
                    print(f"{count} IPs >> ", resp.json())
                    count += 1
                except Exception as ex:
                    print(ex)
                    pass
            print("sync_ips Process Completed")
            end_time = datetime.now() - start_time
            print(end_time)
        threading.Thread(target = current).start()
        # multiprocessing.Process(target=current).start()



if __name__ == "__main__":

    test = Test()
    end_time = start_time - datetime.now()
    print(end_time)
    print("Done!")