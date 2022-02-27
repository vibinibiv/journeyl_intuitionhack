import urllib.request
from lxml import etree


def scrape_listing(website: str, url: str) -> dict:

    if website == "fastjobs":

        title_xpath = '//*[@id="jobad"]/div[1]/h1/text()'
        company_xpath = '//*[@id="jobad"]/div[2]/div/div[1]/div[1]/h2'
        location_xpath = '//*[@id="jobad"]/div[1]/div[1]/div[1]/ul/li[1]/text()[2]'
        job_desc_xpath = '//*[@id="jobad"]/div[1]/div[2]/text()'

        r = urllib.request.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(r, htmlparser)
        title = tree.xpath(title_xpath)[0].strip()
        company = tree.xpath(company_xpath)[0].text.title()
        location = tree.xpath(location_xpath)[0].strip()
        job_desc_list = tree.xpath(job_desc_xpath)
        print(job_desc_list)
        job_desc = "\n".join([li.strip() for li in job_desc_list])

    elif website == "indeed":
        pass

    info = {'title': title, 'company': company, 'location': location,
            'listing_url': url, 'job_desc': job_desc}

    return info
