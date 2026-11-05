from threading import Event,Thread
# Avoid relying on time.sleep; explicitly coordinate observable completion.
ready=Event();done=Event();results=[]
def worker():
    ready.wait(timeout=2);results.append('ok');done.set()
t=Thread(target=worker);t.start();ready.set()
assert done.wait(timeout=2)
t.join(timeout=2);assert not t.is_alive() and results==['ok']
