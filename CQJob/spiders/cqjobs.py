# -*- coding: utf-8 -*-
import time
import scrapy
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
from CQJob.items import CqjobItem

class CqjobsSpider(scrapy.Spider):
    name = 'cqjobs'
    allowed_domains = ['lagou.com']
#     start_urls = ['https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?px=default&city=%E6%9D%AD%E5%B7%9E#filterBox'] #杭州
#     start_urls = ['https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?px=default&city=%E4%B8%8A%E6%B5%B7#filterBox'] #上海
    start_urls = ['https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?px=default&city=%E5%85%A8%E5%9B%BD#filterBox']  #全国

    def parse(self, response):
        browser = webdriver.Chrome()
        browser.get(self.start_urls[0])
        browser.implicitly_wait(10) 
        # 使用beautifulsoup定位
        for i in range(31):
            selector = etree.HTML(browser.page_source)
            soup = BeautifulSoup(browser.page_source, features='lxml')    
#             span = soup.find("div", attrs={"class": "next_disabled next"})
#             classSpan = span["class"]
            print('----------------------------------------------')
#             print(classSpan) # 输出内容为 -> ['pager_next', 'pager_next_disabled']
#             next_flag = classSpan[-1]
            self.parsedata(selector)
            if i<30:
#             if next_flag == "next":
                 print("还有下一页，爬虫继续")
        # 这里一定要注意不能直接copy源代码的xpath，因为每个页面元素标签有可能不一样！
                 browser.find_element_by_xpath('//*[@action="next"]').click()  # 点击下一页 
                 time.sleep(6)
                 print('第{}页抓取完毕'.format(i + 1))
                 i = i+1
            else:
                print("已经爬到最后一页，爬虫结束")
                break 
               
            
        browser.close()

        items = CqjobItem()
        items['name'] = self.name_list
        items['company'] = self.company_list
        items['location'] = self.location_list
        items['welfare'] = self.welfare_list
        items['salaryMin'] = self.salaryMin_list
        items['salaryMax'] = self.salaryMax_list
        items['salaryMid'] = self.salaryMid_list
        items['experience'] = self.experience_list
        items['education'] = self.education_list
        items['companyType'] = self.companyType_list
        items['companyLevel'] = self.companyLevel_list
        items['companySize'] = self.companySize_list
        items['label'] = self.label_list
        items['hr'] = self.hr_list

        yield items
        print(items['company'])
        print(items['hr'])

        
    name_list = []
    location_list = []
    company_list = []
    welfare_list = []
    salaryMin_list = []
    salaryMax_list = []
    salaryMid_list = []
    experience_list = []
    education_list = []
    companyType_list = []
    companyLevel_list = []
    companySize_list = []
    label_list = []
    hr_list = []
    
    def parsedata(self, selector):
        sel_list = selector.xpath('//*[@id="s_position_list"]/ul/li')
        for item in sel_list:
            name = item.xpath('div[1]/div[1]/div[1]/a/h3/text()')[0]
            self.name_list.append(name)
            location = item.xpath('div[1]/div[1]/div[1]/a/span/em/text()')[0]
            self.location_list.append(location)
            hr = item.xpath('div[1]/div[1]/div[1]/input[@class="hr_name"]/@value')[0]
            self.hr_list.append(hr)        
            company = item.xpath('div[1]/div[2]/div[1]/a/text()')[0]
            self.company_list.append(company)
            welfare = item.xpath('div[2]/div[2]/text()')[0]
            self.welfare_list.append(welfare)
            salaryList = item.xpath('div[1]/div[1]/div[2]/div/span/text()')[0].strip().split("-")
            # print(salaryList) # [10k-15k]
            label_words = item.xpath('div[2]/div[1]/span/text()')
            for label_word in label_words:
                label= (' '.join(str( label_word) for label_word in label_words ))
            self.label_list.append(label)
            salaryMin = salaryList[0][:len(salaryList[0]) - 1] # 10 去除k,只留数字
            self.salaryMin_list.append(salaryMin)
            salaryMax = salaryList[1][:len(salaryList[1]) - 1] # 15
            self.salaryMax_list.append(salaryMax)
            salaryMid = (int(salaryMin) + int(salaryMax)) / 2
            self.salaryMid_list.append(salaryMid)

            educationArray = item.xpath('div[1]/div[1]/div[2]/div//text()')[3].strip().split("/")
            # print(educationArray)
            experience = educationArray[0].strip()
            self.experience_list.append(experience)
            education = educationArray[1].strip()
            self.education_list.append(education)
            # conmpanyMsgArray = item.xpath('div[1]/div[2]/div[2]/text()')[0].strip().split("/")
            conmpanyMsgList = item.xpath('div[1]/div[2]/div[2]/text()')[0].strip().split("/")
            companyType = conmpanyMsgList[0].strip()
            self.companyType_list.append(companyType)
            companyLevel = conmpanyMsgList[1].strip()
            self.companyLevel_list.append(companyLevel)
            companySize = conmpanyMsgList[2].strip()
            self.companySize_list.append(companySize)
        
            
            
            
            
