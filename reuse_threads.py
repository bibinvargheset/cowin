from threading import Thread, Event


class ReusableThread(Thread):
    """
    This class provides code for a restartale / reusable thread

    join() will only wait for one (target)functioncall to finish
    finish() will finish the whole thread (after that, it's not restartable anymore)

    """

    def __init__(self, target, args):
        self._startSignal = Event()
        self._oneRunFinished = Event()
        self._finishIndicator = False
        self._callable = target
        self._callableArgs = args

        Thread.__init__(self)

    def restart(self):
        """make sure to always call join() before restarting"""
        self._startSignal.set()

    def run(self):
        """ This class will reprocess the object "processObject" forever.
        Through the change of data inside processObject and start signals
        we can reuse the thread's resources"""

        self.restart()
        while (True):
            # wait until we should process
            self._startSignal.wait()

            self._startSignal.clear()

            if (self._finishIndicator):  # check, if we want to stop
                self._oneRunFinished.set()
                return

            # call the threaded function
            self._callable(*self._callableArgs)

            # notify about the run's end
            self._oneRunFinished.set()

    def join(self):
        """ This join will only wait for one single run (target functioncall) to be finished"""
        self._oneRunFinished.wait()
        self._oneRunFinished.clear()

    def finish(self):
        self._finishIndicator = True
        self.restart()
        self.join()


def doSomething(objectToProcess):
    print(str(objectToProcess[0]))
    pass

if __name__ == "__main__":
    changableObject = [0]
    thread = ReusableThread(target = doSomething,
             args = [changableObject]) #we need [] to tell python it's a list

    # start the thread
    changableObject[0] = 1
    thread.start()

    thread.join()

    changableObject[0] = 2
    thread.restart()

    thread.join()

    changableObject[0] = 3
    thread.restart()

    thread.join()

    thread.finish()