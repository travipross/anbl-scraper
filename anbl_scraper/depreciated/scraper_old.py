import json
import queue
import time
from threading import Thread
from anbl_scraper.anbl_scraper_tools import url_scraper_worker
from anbl_scraper.anbl_converter import anbl_csv_writer

AUTOSAVE = False
STATUS_PERIOD = 5
N_WORKERS = 100
results_json = "run_results.json"
output_name = "parsed_data"
stats = {"failed": 0}

# load json file with results
with open(results_json) as f:
    data = json.load(f)

# put all product dicts into a queue to share between workers
q = queue.Queue()
n = 0
for category in data["product_categories"]:
    print("Queueing all products in [%s] category..." % category["name"])
    for item in category["product"]:
        q.put([item, n])
        n = n + 1
print("%d products queued" % n)

# start url scraper workers
workers_list = []
t_start = time.time()
for i in range(N_WORKERS):
    workers_list.append(
        Thread(target=url_scraper_worker, args=(q, i, stats), name="worker%d" % i)
    )
    workers_list[i].start()
    q.put([None, None])

# main loop: occasionally print
while not q.empty():
    print("Items remaining in queue: %d" % q.qsize())
    if q.qsize() <= 10:
        print("Workers remaining: %s" % [t.name for t in workers_list if t.is_alive()])
    if AUTOSAVE:
        with open(output_name, "w") as f:
            json.dump(data, f, indent=4)
        print("Results saved to %s" % output_name)
    time.sleep(STATUS_PERIOD)

# print statistics about scraping session
t_end = time.time()
elapsed = t_end - t_start
print("-" * 80)
print("%d/%d products had complete data" % ((n - stats["failed"]), n))
print("Time elapsed: %d seconds" % elapsed)
print("%.2f pages scraped per minute" % (n / elapsed))
print("%.2f seconds per page per worker" % (elapsed / n * N_WORKERS))

# join workers and wait for job to finish before saving to disk
for w in workers_list:
    w.join()

# save final results to file
with open(output_name + ".json", "w") as f:
    json.dump(data, f, indent=4)

anbl_csv_writer(data, output_name + ".csv")
