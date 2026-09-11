from scholarly import scholarly, ProxyGenerator
import json
import os
import sys
import signal
from datetime import datetime

SCHOLAR_ID = os.environ['GOOGLE_SCHOLAR_ID']


class Timeout(Exception):
    pass


def _deadline(seconds):
    """Context-free hard timeout so a hung proxy/CAPTCHA loop can't run forever."""
    def _handler(signum, frame):
        raise Timeout()
    signal.signal(signal.SIGALRM, _handler)
    signal.alarm(seconds)


def _clear_deadline():
    signal.alarm(0)


def fetch_author():
    """Fill the author record. Returns the dict or raises."""
    author = scholarly.search_author_id(SCHOLAR_ID)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    return author


def try_once(use_proxy, per_attempt_timeout=150):
    if use_proxy:
        pg = ProxyGenerator()
        # Rotate through free proxies so the request doesn't come from a
        # blocked GitHub datacenter IP.
        if not pg.FreeProxies():
            raise RuntimeError("FreeProxies setup failed")
        scholarly.use_proxy(pg)
    else:
        # Direct connection. scholarly 1.5.1's use_proxy() requires a
        # ProxyGenerator (passing None throws), so hand it a fresh,
        # unconfigured one, which defaults to no proxy.
        scholarly.use_proxy(ProxyGenerator())
    _deadline(per_attempt_timeout)
    try:
        return fetch_author()
    finally:
        _clear_deadline()


def main():
    # Attempt order: one direct try (fast when it works), then several
    # proxied tries. Each is time-boxed so the job never hangs.
    attempts = [False, True, True, True, True]
    author = None
    for i, use_proxy in enumerate(attempts, 1):
        mode = "proxy" if use_proxy else "direct"
        try:
            print(f"[attempt {i}/{len(attempts)}] fetching via {mode} ...", flush=True)
            author = try_once(use_proxy)
            print(f"[attempt {i}] success", flush=True)
            break
        except Timeout:
            print(f"[attempt {i}] timed out ({mode})", flush=True)
        except Exception as e:
            print(f"[attempt {i}] failed ({mode}): {e!r}", flush=True)

    if author is None:
        print("ERROR: could not fetch Google Scholar data after all attempts "
              "(likely CAPTCHA / rate-limited). Leaving existing data untouched.",
              file=sys.stderr, flush=True)
        sys.exit(1)

    name = author['name']
    author['updated'] = str(datetime.now())
    author['publications'] = {v['author_pub_id']: v for v in author['publications']}
    print(json.dumps(author, indent=2))

    os.makedirs('results', exist_ok=True)
    with open('results/gs_data.json', 'w') as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    with open('results/gs_data_shieldsio.json', 'w') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)
    print(f"Wrote results for {name}: {author['citedby']} citations")


if __name__ == '__main__':
    main()
