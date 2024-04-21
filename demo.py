# -*- coding: utf-8 -*-

import crawling_comics as cc

if __name__ == '__main__':
    # 漫画首页url
    site = 'https://comic.acgn.cc/manhua-thesculptordiaokejia.htm'

    crawler = cc.CrawlingComics(
        site=site,  # 漫画首页
        begin=0,    # 起始章节
        end=-1,     # 结束章节
        save_folder='./download',  # 保存路径，不存在会自动创建
        browser=cc.BrowserType.FIREFOX,         # 浏览器类型：FIREFOX，CHROME，SAFARI，IE，PHANTOMJS
        driver_path='./driver/geckodriver.exe'  # 驱动程序路径
    )
    crawler.start()
    crawler.displays_unloaded()
