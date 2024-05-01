



import time
from time import perf_counter
from initinterception import left_click
from humancursor import SystemCursor




class Helper:

    def __init__(self) -> None:
        self.hc = SystemCursor()
        pass

    async def move_to(self,x,y):
        self.hc.move_to((x,y))

    async def move_to_and_click(self,x,y):
        self.hc.move_to((x,y))
        time.sleep(.1)
        left_click()