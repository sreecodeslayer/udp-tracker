from pybtracker import TrackerServer
import asyncio

loop = asyncio.get_event_loop()
print(":: Setting Loop...")
tracker = TrackerServer(local_addr=('0.0.0.0', 6565), loop=loop)
print(":: Setting up tracker at 0.0.0.0:6565 ...")
asyncio.ensure_future(tracker.start())
try:
	print(":: Server started ... 'udp://54.202.194.106:6565'")
	loop.run_forever()
except KeyboardInterrupt:
	print(":: Server stopped! ...")
	loop.run_until_complete(tracker.stop())
except Exception as e:
	raise e