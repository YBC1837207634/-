import logging
import multiprocessing
from master.getter import Getter
from master.tester import Tester
from master.server import app


logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.WARNING)
# redis_process = openRedis()


class Run:
    """
        主程序，用来调度模块
    
    """
    def getter(self):
        g = Getter()
        g.run()

    def tester(self):
        t = Tester()
        t.run()

    def server(self):
        app.run()

    def run(self):
        try:
            getterProcess = multiprocessing.Process(target=self.getter, daemon=True)
            testerProcess = multiprocessing.Process(target=self.tester, daemon=True)
            serverProcess = multiprocessing.Process(target=self.server, daemon=True)
            getterProcess.start()
            testerProcess.start()
            serverProcess.start()
            getterProcess.join()
            testerProcess.join()
            serverProcess.join()
        except:
            logging.warning('启动进程时发生错误！')
        else:
            logging.info('进程正常启动~~~~~~~')            
        finally:
            # redis_process.kill()
            getterProcess.terminate()
            testerProcess.terminate()
            serverProcess.terminate()
        logging.info('程序退出!!!!')


    # def close(self):
        # redis_process.kill()


if __name__ == '__main__':
    r = Run()
    r.run()









