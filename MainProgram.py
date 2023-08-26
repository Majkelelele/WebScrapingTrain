from DataScraper import DataScraper
import time
from Sorting import Sorting
from PairOfCoins import PairOfCoins
class MainProgram:
    def run(self):
        start_time = time.time()
        dataScraper = DataScraper()
        coinsBinance = dataScraper.scrapeAllPages(25,'Binance')
        coinsCoinBase = dataScraper.scrapeAllPages(15, 'CoinBase')
        sorting = Sorting(coinsBinance,coinsCoinBase)
        data = sorting.createListOfMatchingCoins()

        for i, coin in enumerate(data, start=1):
            coin.printInfo(i)
        print(data.__len__())
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Main execution time: {execution_time:.6f} seconds")