# Download the 56 zip files in Images_png in batches
import argparse
import shutil
from multiprocessing.pool import ThreadPool
from time import sleep

import numpy as np
import requests


def parse_args ():
	arg_parser = argparse.ArgumentParser(description='Parser')

	arg_parser.add_argument(
			'--archives-directory',
			type=str,
			metavar='archives_directory',
			default='./database/',
			help=''
	)

	arg_parser.add_argument(
			'--n-threads',
			type=int,
			metavar='nthreads',
			default=2,
			help=''
	)

	return arg_parser.parse_args()


# URLs for the zip files
LINKS = [
	'https://nihcc.box.com/shared/static/vfk49d74nhbxq3nqjg0900w5nvkorp5c.gz',
	'https://nihcc.box.com/shared/static/i28rlmbvmfjbl8p2n3ril0pptcmcu9d1.gz',
	'https://nihcc.box.com/shared/static/f1t00wrtdk94satdfb9olcolqx20z2jp.gz'
	'https://nihcc.box.com/shared/static/0aowwzs5lhjrceb3qp67ahp0rd1l1etg.gz',
	'https://nihcc.box.com/shared/static/v5e3goj22zr6h8tzualxfsqlqaygfbsn.gz',
	'https://nihcc.box.com/shared/static/asi7ikud9jwnkrnkj99jnpfkjdes7l6l.gz',
	'https://nihcc.box.com/shared/static/jn1b4mw4n6lnh74ovmcjb8y48h8xj07n.gz',
	'https://nihcc.box.com/shared/static/tvpxmn7qyrgl0w8wfh9kqfjskv6nmm1j.gz',
	'https://nihcc.box.com/shared/static/upyy3ml7qdumlgk2rfcvlb9k6gvqq2pj.gz',
	'https://nihcc.box.com/shared/static/l6nilvfa9cg3s28tqv1qc1olm3gnz54p.gz',
	'https://nihcc.box.com/shared/static/hhq8fkdgvcari67vfhs7ppg2w6ni4jze.gz',
	'https://nihcc.box.com/shared/static/ioqwiy20ihqwyr8pf4c24eazhh281pbu.gz'
]


def download_urls (link_ix):
	try:
		link = LINKS[link_ix]
		file_name = 'images_%03d' % (link_ix + 1) + '.gz'
		with requests.get(link, stream=True) as r:
			with open(args.archives_directory + file_name, 'wb') as f:
				shutil.copyfileobj(r.raw, f)

		print('DONE ' + str(link))
		sleep(np.random.randint(1, 3))

	except Exception as e:
		print(e)


if __name__ == "__main__":
	args = parse_args()
	print('Archives will be downloaded under ' + str(args.archives_directory) + ' directory.')
	with ThreadPool(args.nthreads) as pool:
		list(pool.imap_unordered(
				download_urls,
				(link_ix for link_ix in range(len(LINKS))),
				chunksize=1
		))
