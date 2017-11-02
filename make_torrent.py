from dottorrent import Torrent
import os

def make_torrent(location):
	try:
		t = Torrent(
			location,
			trackers = ['udp://192.168.10.109:3535'],
			private = True,
			comment = "Download made available by Datahut",
			include_md5 = True
			)

		t.generate()

		filename = location.split('/')[-1] + '.torrent'
		path = os.path.join(os.getcwd(),filename)
		print("Path : ",path)

		with open(path, 'wb') as fp:
			t.save(fp)

	except FileNotFoundError:
		print("File not found")
		return False
	except Exception as e:
		raise e
