import asyncio
import threading

_loop = asyncio.new_event_loop()

_thr = threading.Thread(target=_loop.run_forever, name="Async Runner",
                        daemon=True)

# This will block the calling thread until the coroutine is finished.
# Any exception that occurs in the coroutine is raised in the caller
def run_async(coro):  # coro is a couroutine, see example
    if not _thr.is_alive():
        _thr.start()
    future = asyncio.run_coroutine_threadsafe(coro, _loop)
    return future.result()

if __name__ == "__main__":
    async def hel():
        await asyncio.sleep(0.1)
        print("Running in thread", threading.current_thread())
        return 4
    
    def i():
        y = run_async(hel())
        print("Answer", y, threading.current_thread())
    
    async def h():
        i()
    
    asyncio.run(h())
