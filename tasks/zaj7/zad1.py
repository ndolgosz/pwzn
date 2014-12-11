import requests
from multiprocessing.pool import ThreadPool
import hashlib
import unittest

def getter(num_threads) :

    response = requests.head("http://db.fizyka.pw.edu.pl/pwzn-data/zaj7/rand-data-a")
    resp_len = int(response.headers['Content-Length'])


    data = []
    step = int(resp_len/num_threads)
    p = ThreadPool(num_threads)
    request_range=[]
    for ii in range(0, resp_len, step):
        request_range.append((ii, min(resp_len, ii+step-1)))
    response = p.map(one_getter, request_range)

    collected = b"".join([d.content for d in response])
    sha = hashlib.sha256()
    sha_origin = hashlib.sha256()
    original = requests.get("http://db.fizyka.pw.edu.pl/pwzn-data/zaj7/rand-data-a")
    sha_origin.update(original.content)
    sha.update(collected)
    if sha.hexdigest() == sha_origin.hexdigest():
        print("OK!")



def one_getter(request_range) :
    return requests.get("http://db.fizyka.pw.edu.pl/pwzn-data/zaj7/rand-data-a", headers = {"Range": "bytes={}-{}".format(*request_range)})

getter(5)