
class StockDataCrawler:
    def __init__(self):
        self.base_url = "https://api.eastmoney.com" # 东方财富API

    def fetch_financial_data(self,stock_code :str):
        """
        获取上市公司财报
        :param stock_code:
        :return:
        """
        # 使用免费API爬取财报数据
        pass

    def fetch_news(self,stock_code:str):
        """
        获取相关新闻
        :param stock_code:
        :return:
        """
        pass

    def fetch_fund_info(self,fund_code):
        """
        获取基金信息
        :param fund_code:  基金代码
        :return:
        """

        pass

# 使用开放API无需爬虫，更稳定）
# 1. 天天基金 API
# 2. 新浪财经 API
# 3.东方财富 API