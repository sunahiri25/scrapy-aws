import scrapy
import datetime
import time
from scrapy.utils.project import get_project_settings

class MySpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["infodoanhnghiep.com"]
    def __init__(self, start_urls = "https://infodoanhnghiep.com/Ha-Noi/", page_start=1, page_end=100, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_urls]
        self.page_start = int(page_start)
        self.page_end = int(page_end)

    def start_requests(self):
        for url in self.start_urls:
            # for page in range(self.page_start, self.page_end + 1):
            page_url = f"{url}trang-{self.page_start}/"
            yield scrapy.Request(url=page_url, callback=self.parse)

    # settings = get_project_settings()
    # start_urls = settings.get('START_URLS')
    # start_urls = [
        # "https://infodoanhnghiep.com/Ha-Noi/",
        # "https://infodoanhnghiep.com/TP-Ho-Chi-Minh/",
        # "https://infodoanhnghiep.com/Can-Tho/",
        # "https://infodoanhnghiep.com/Da-Nang/",
        # "https://infodoanhnghiep.com/Hai-Phong/",
        # "https://infodoanhnghiep.com/An-Giang/",
        # "https://infodoanhnghiep.com/Ba-Ria-Vung-Tau/",
        # "https://infodoanhnghiep.com/Bac-Giang/",
        # "https://infodoanhnghiep.com/Bac-Kan/",
        # "https://infodoanhnghiep.com/Bac-Lieu/",
        # "https://infodoanhnghiep.com/Bac-Ninh/",
        # "https://infodoanhnghiep.com/Ben-Tre/",
        # "https://infodoanhnghiep.com/Binh-Dinh/",
        # "https://infodoanhnghiep.com/Binh-Duong/",
        # "https://infodoanhnghiep.com/Binh-Phuoc/",
        # "https://infodoanhnghiep.com/Binh-Thuan/",
        # "https://infodoanhnghiep.com/Ca-Mau/",
        # "https://infodoanhnghiep.com/Cao-Bang/",
        # "https://infodoanhnghiep.com/Dak-Lak/",
        # "https://infodoanhnghiep.com/Dak-Nong/",
        # "https://infodoanhnghiep.com/Dien-Bien/",
        # "https://infodoanhnghiep.com/Dong-Nai/",
        # "https://infodoanhnghiep.com/Dong-Thap/",
        # "https://infodoanhnghiep.com/Gia-Lai/",
        # "https://infodoanhnghiep.com/Ha-Giang/",
        # "https://infodoanhnghiep.com/Ha-Nam/",
        # "https://infodoanhnghiep.com/Ha-Tinh/",
        # "https://infodoanhnghiep.com/Hai-Duong/",
        # "https://infodoanhnghiep.com/Hau-Giang/",
        # "https://infodoanhnghiep.com/Hoa-Binh/",
        # "https://infodoanhnghiep.com/Hung-Yen/",
        # "https://infodoanhnghiep.com/Khanh-Hoa/",
        # "https://infodoanhnghiep.com/Kien-Giang/",
        # "https://infodoanhnghiep.com/Kon-Tum/",
        # "https://infodoanhnghiep.com/Lai-Chau/",
        # "https://infodoanhnghiep.com/Lam-Dong/",
        # "https://infodoanhnghiep.com/Lang-Son/",
        # "https://infodoanhnghiep.com/Lao-Cai/",
        # "https://infodoanhnghiep.com/Long-An/",
        # "https://infodoanhnghiep.com/Nam-Dinh/",
        # "https://infodoanhnghiep.com/Nghe-An/",
        # "https://infodoanhnghiep.com/Ninh-Binh/",
        # "https://infodoanhnghiep.com/Ninh-Thuan/",
        # "https://infodoanhnghiep.com/Phu-Tho/",
        # "https://infodoanhnghiep.com/Phu-Yen/",
        # "https://infodoanhnghiep.com/Quang-Binh/",
        # "https://infodoanhnghiep.com/Quang-Nam/",
        # "https://infodoanhnghiep.com/Quang-Ngai/",
        # "https://infodoanhnghiep.com/Quang-Ninh/",
        # "https://infodoanhnghiep.com/Quang-Tri/",
        # "https://infodoanhnghiep.com/Soc-Trang/",
        # "https://infodoanhnghiep.com/Son-La/",
        # "https://infodoanhnghiep.com/Tay-Ninh/",
        # "https://infodoanhnghiep.com/Thai-Binh/",
        # "https://infodoanhnghiep.com/Thai-Nguyen/",
        # "https://infodoanhnghiep.com/Thanh-Hoa/",
        # "https://infodoanhnghiep.com/Thua-Thien-Hue/",
        # "https://infodoanhnghiep.com/Tien-Giang/",
        # "https://infodoanhnghiep.com/Tra-Vinh/",
        # "https://infodoanhnghiep.com/Tuyen-Quang/",
        # "https://infodoanhnghiep.com/Vinh-Long/",
        # "https://infodoanhnghiep.com/Vinh-Phuc/",
        # "https://infodoanhnghiep.com/Yen-Bai/"
    # ]
        

    # def parse(self, response):
    #     # Lấy danh sách các doanh nghiệp
    #     for doanhnghiep in response.css('div.company-item'):
    #         link = doanhnghiep.css('h3.company-name a::attr(href)').get()
    #         yield scrapy.Request(
    #             url=link,
    #             callback=self.parse_detail,
    #             meta={'link': link}
    #         )
        # # Tìm link đến trang tiếp theo
        # current_page = response.css('ul.pagination li.active a::attr(href)').get()
        # next_page = response.css('ul.pagination li.active + li a::attr(href)').get()
        # # time.sleep(0.2)
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
        # Tìm link đến trang tiếp theo
    def parse(self, response):
        # Lấy danh sách các doanh nghiệp
        for doanhnghiep in response.css('div.company-item'):
            link = doanhnghiep.css('h3.company-name a::attr(href)').get()
            yield scrapy.Request(
                url=link,
                callback=self.parse_detail,
                meta={'link': link}
            )
        
        # Tìm link đến trang tiếp theo, chỉ lấy trang trong khoảng page_start và page_end
        current_page_number = response.css('ul.pagination li.active a::text').get()
        current_page_number = int(current_page_number) if current_page_number else self.page_start

        if current_page_number < self.page_end:
            next_page_number = current_page_number + 1
            next_page_url = f"{self.start_urls[0]}trang-{next_page_number}/"
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_detail(self, response):
        # Lấy dữ liệu chi tiết từ trang doanh nghiệp
        # Extract business information
        description = response.css('div.description p::text').getall()
        name = response.css('div.description strong::text').get()
        tax_id = response.css('div.responsive-table-cell[itemprop="taxID"]::text').get()
        status = response.css('div.responsive-table-cell:contains("Tình trạng hoạt động:") + div.responsive-table-cell::text').get()
        address = response.css('div.responsive-table-cell[itemprop="address"]::text').get()
        license_issue_date = response.css('div.responsive-table-cell:contains("Ngày cấp giấy phép:") + div.responsive-table-cell::text').get()
        industry = response.css('div.responsive-table-cell::text').re_first(r'.*Ngành chính.*')
        
        yield {
            'name': name,
            'tax_id': tax_id,
            'status': status,
            'address': address,
            'license_issue_date': license_issue_date,
            'industry': industry.replace(' (Ngành chính)', '') if industry is not None else None,
            'link': response.meta['link'],
            'scraping_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }