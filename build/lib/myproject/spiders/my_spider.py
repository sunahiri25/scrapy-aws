# myproject/spiders/my_spider.py
import scrapy
from scrapy import Selector
import random
import re
import csv
import os
import datetime

class MySpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ['hosocongty.vn', 'thuvienphapluat.vn']

    def start_requests(self):
        url = 'https://hosocongty.vn'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == 403:
            self.logger.warning(f"403 Forbidden: {response.url}")
            return

        last_page = int(response.xpath('//div[contains(@class, "next-page")]/a/text()').extract()[-1])
        for page in range(1, last_page + 1):
            page_url = f'{response.url}/page-{page}'
            yield scrapy.Request(url=page_url, callback=self.parse_page)

    def parse_page(self, response):
        if response.status == 403:
            self.logger.warning(f"403 Forbidden: {response.url}")
            return

        names = response.xpath('//ul[contains(@class, "hsdn")]/li/h3/a/text()').extract()
        links = response.xpath('//ul[contains(@class, "hsdn")]/li/h3/a/@href').extract()
        addresses = response.xpath('//ul[contains(@class, "hsdn")]/li/div/text()').extract()
        tax_ids = response.xpath('//ul[contains(@class, "hsdn")]/li/div/a/text()').extract()
        addresses = [element.strip() for element in addresses if element != 'Mã số thuế: ']

        for name, link, address, tax_id in zip(names, links, addresses, tax_ids):
            masothue_url = f'https://thuvienphapluat.vn/ma-so-thue/tra-cuu-ma-so-thue-doanh-nghiep?timtheo=ma-so-thue&tukhoa={tax_id}'
            request = scrapy.Request(url=masothue_url, callback=self.parse_company)
            request.meta['name'] = name
            request.meta['address'] = address
            request.meta['tax_id'] = tax_id
            request.meta['link'] = link
            yield request
            
            # hosocompany_url = 'https://hosocongty.vn/' + link
            # request_hoso = scrapy.Request(url=hosocompany_url, callback=self.parse_company_hoso)
            # request_hoso.meta['name'] = name
            # request_hoso.meta['address'] = address
            # request_hoso.meta['tax_id'] = tax_id
            # request_hoso.meta['link'] = link
            # yield request_hoso

    def parse_company_hoso(self, response):
        item = {}
        if response.status == 403:
            self.logger.warning(f"403 Forbidden: {response.url}")
            return

        name = response.meta['name']
        address = response.meta['address']
        tax_id = response.meta['tax_id']
        link = response.meta['link']

        html_content = response.xpath('//div[contains(@class, "box_content")]').extract_first()

        # Define regex patterns for "Ngày cấp", "Trạng thái", "Điện thoại", "Email", and "Ngành nghề chính"
        ngay_cap_pattern = re.compile(r'Ngày cấp:</label><span>\s*<a href="[^"]+" title="[^"]+">([^<]+)</a></span>')
        trang_thai_pattern = re.compile(r'Trạng thái:</label><span>([^<]+)</span>')
        dien_thoai_pattern = re.compile(r'Điện thoại:</label><span class="highlight">([^<]+)</span>')
        email_pattern = re.compile(r'Email:</label><span class="highlight">([^<]+)</span>')
        nganh_nghe_chinh_pattern = re.compile(r'Ngành nghề chính:</label><span>\s*<a href="[^"]+" title="[^"]+">([^<]+)</a></span>')

        # Extract information using regex
        ngay_cap_match = ngay_cap_pattern.search(html_content)
        trang_thai_match = trang_thai_pattern.search(html_content)
        dien_thoai_match = dien_thoai_pattern.search(html_content)
        email_match = email_pattern.search(html_content)
        nganh_nghe_chinh_match = nganh_nghe_chinh_pattern.search(html_content)

        # Get the matched results or None if not found
        ngay_cap = ngay_cap_match.group(1) if ngay_cap_match else None
        trang_thai = trang_thai_match.group(1) if trang_thai_match else None
        dien_thoai = dien_thoai_match.group(1) if dien_thoai_match else None
        email = email_match.group(1) if email_match else None
        nganh_nghe_chinh = nganh_nghe_chinh_match.group(1) if nganh_nghe_chinh_match else None
        # item['name'] = name
        # item['address'] = address
        # item['tax_id'] = tax_id
        # item['incorporation_date'] = ngay_cap_match.group(1) if ngay_cap_match else None
        # item['phone'] = dien_thoai_match.group(1) if dien_thoai_match else None
        # item['email'] = email_match.group(1) if email_match else None
        # item['company_type'] = None
        # item['status'] = trang_thai_match.group(1) if trang_thai_match else None
        # item['field_of_business'] = nganh_nghe_chinh_match.group(1) if nganh_nghe_chinh_match else None
        # item['hosocongty_url'] = 'https://hosocongty.vn/' + link
        # item['masothue_url'] = None
        # item['scraping_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # yield item
        
        # Write to CSV
        self.write_to_csv([
            name,
            address,
            tax_id,
            ngay_cap,
            dien_thoai,
            email,
            None,  # Placeholder for company type from thuvienphapluat.vn
            trang_thai,
            nganh_nghe_chinh,
            'https://hosocongty.vn/' + link,
            None,  # Placeholder for thuvienphapluat.vn URL
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ])
        

    def parse_company(self, response):
        if response.status == 403:
            self.logger.warning(f"403 Forbidden: {response.url}")
            return

        name = response.meta['name']
        address = response.meta['address']
        tax_id = response.meta['tax_id']
        link = response.meta['link']

        if response.xpath('//div[contains(@id, "dvResultSearch")]/div/text()').extract_first() == 'Không tìm thấy kết quả với các điều kiện trên' or response.xpath('//div[contains(@id, "dvResultSearch")]/table/tbody/tr/td[2]/a/strong/text()').extract_first() != tax_id:
            # self.write_to_csv([name, address, tax_id, None, None, None, None, None, None, 'https://hosocongty.vn/' + link, None, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
            yield {
                'name': name,
                'address': address,
                'tax_id': tax_id,
                'incorporation_date': None,
                'phone': None,
                'email': None,
                'company_type': None,
                'status': None,
                'field_of_business': None,
                'hosocongty_url': 'https://hosocongty.vn/' + link,
                'masothue_url': None,
                'scraping_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        else:
            search_results = response.xpath('//div[contains(@id, "dvResultSearch")]/table/tbody/tr/td[3]/div/a/@href').extract_first()
            company_url = 'https://thuvienphapluat.vn' + search_results
            request = scrapy.Request(url=company_url, callback=self.parse_company_details)
            request.meta['name'] = name
            request.meta['address'] = address
            request.meta['tax_id'] = tax_id
            request.meta['link'] = link
            yield request

    def parse_company_details(self, response):
        if response.status == 403:
            self.logger.warning(f"403 Forbidden: {response.url}")
            return

        name = response.meta['name']
        address = response.meta['address']
        tax_id = response.meta['tax_id']
        link = response.meta['link']

        html_content = response.xpath('//ul[contains(@id, "ThongTinDoanhNghiep")]').extract_first()
        if html_content:
            regex_patterns = {
                "Loại hình pháp lý": re.compile(r'<span class="dn_1" id="lbl_head_LoaiHinhDoanhNghiep"[^>]*>Loại hình pháp lý:\s*</span>\s*</div>\s*<div class="col-md-9">\s*<div>([^<]+)</div>'),
                "Điện thoại": re.compile(r'<span class="dn_1">Điện thoại:</span>\s*</div>\s*<div class="col-md-9">\s*<span>([^<]+)</span>'),
                "Email": re.compile(r'<span class="dn_1">Email:</span>\s*</div>\s*<div class="col-md-9">\s*<span>([^<]+)</span>'),
                "Tình trạng": re.compile(r'<span class="dn_1">Tình trạng:\s*</span>\s*</div>\s*<div class="col-md-9">\s*<span[^>]*>\s*([^<]+)\s*</span>'),
                "Ngày cấp": re.compile(r'<span class="dn_1">Ngày cấp:</span>\s*</div>\s*<div class="col-md-9">\s*<span>\s*([^<]+)\s*</span>'),
                "Ngành nghề chính": re.compile(r'<b>([^<]+)</b>\s*<i>\(Ngành nghề chính\)</i>'),
                "Địa chỉ trụ sở": re.compile(r'<span class="dn_1">Địa chỉ trụ sở:</span>\s*</div>\s*<div class="col-md-9">\s*<span id="fill_DiaChiTruSo">([^<]+)</span>'),
            }

            info = self.extract_info(html_content, regex_patterns)
            # self.write_to_csv([
            #     name,
            #     info.get('Địa chỉ trụ sở', address),
            #     tax_id,
            #     info.get('Ngày cấp', None),
            #     info.get('Điện thoại', None),
            #     info.get('Email', None),
            #     info.get('Loại hình pháp lý', None),
            #     info.get('Tình trạng', None),
            #     info.get('Ngành nghề chính', None),                
            #     'https://hosocongty.vn/' + link,
            #     response.url,
            #     datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # ])
            item = {}
            item['name'] = name
            item['address'] = info.get('Địa chỉ trụ sở', address)
            item['tax_id'] = tax_id
            item['incorporation_date'] = info.get('Ngày cấp', None)
            item['phone'] = info.get('Điện thoại', None)
            item['email'] = info.get('Email', None)
            item['company_type'] = info.get('Loại hình pháp lý', None)
            item['status'] = info.get('Tình trạng', None)
            item['field_of_business'] = info.get('Ngành nghề chính', None)
            item['hosocongty_url'] = 'https://hosocongty.vn/' + link
            item['masothue_url'] = response.url
            item['scraping_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            yield item

    def extract_info(self, html_content, regex_patterns):
        extracted_info = {}
        for key, pattern in regex_patterns.items():
            match = pattern.search(html_content)
            if match:
                extracted_info[key] = match.group(1).strip()
        return extracted_info

    def write_to_csv(self, row):
        file_name = './masothue_company_infos.csv'
        file_exists = os.path.isfile(file_name)
        with open(file_name, 'a', newline='', encoding='utf-8') as out_file:
            writer = csv.writer(out_file)
            if not file_exists:
                writer.writerow(['name', 'address', 'tax_id', 'incorporation_date', 'phone', 'email', 'company_type', 'status', 'field_of_business', 'hosocongty_url', 'masothue_url', 'scraping_time'])
            writer.writerow(row)

