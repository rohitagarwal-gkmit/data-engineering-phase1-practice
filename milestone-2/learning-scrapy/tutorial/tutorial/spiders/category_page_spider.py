import scrapy


class SnapdealCategorySpider(scrapy.Spider):
    name = "snapdeal_category"
    allowed_domains = ["snapdeal.com"]
    category_id = 868
    page_size = 20
    total_pages = 1

    custom_settings = {
        "USER_AGENT": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "LOG_LEVEL": "ERROR",
        "DOWNLOAD_DELAY": 1,
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_START_DELAY": 2,
        "AUTOTHROTTLE_MAX_DELAY": 15,
        "AUTOTHROTTLE_TARGET_CONCURRENCY": 3.0,
    }

    def start_requests(self):
        url = f"https://www.snapdeal.com/acors/json/product/get/search/{self.category_id}/0/{self.page_size}"
        yield scrapy.Request(url=url, callback=self.parse_total_pages)

    def parse_total_pages(self, response):
        total_count_text = response.css("div.jsNumberFound::text").get()

        if not total_count_text:
            self.logger.error("Could not find total product count")
            return

        total_count = int(total_count_text.strip())
        self.logger.info(f"Total products found: {total_count}")

        full_pages = total_count // self.page_size
        remainder = total_count % self.page_size

        # Full pages (20 each)
        for page in range(full_pages):
            start = page * self.page_size
            url = f"https://www.snapdeal.com/acors/json/product/get/search/{self.category_id}/{start}/{self.page_size}"

            yield scrapy.Request(url=url, callback=self.parse_listing)

        # Last partial page
        if remainder > 0:
            start = full_pages * self.page_size
            url = f"https://www.snapdeal.com/acors/json/product/get/search/{self.category_id}/{start}/{remainder}"

            yield scrapy.Request(url=url, callback=self.parse_listing)

    def parse_listing(self, response):
        """
        Parse JSON search response
        """

        product_links = response.css("div.product-tuple-image a::attr(href)").getall()

        self.logger.info(f"Found {len(product_links)} products")

        for link in product_links:
            yield response.follow(link, callback=self.parse_product)

    def parse_product(self, response):
        """
        Parse Snapdeal Product Detail Page
        """
        raw_highlights = response.css(
            "div.p-keyfeatures li span.h-content::text"
        ).getall()

        name = response.css("h1.pdp-e-i-head::attr(title)").get()
        highlights = {}
        for item in raw_highlights:
            item = item.strip()
            if ":" in item:
                key, value = item.split(":", 1)
                highlights[key.strip()] = value.strip()
            else:
                highlights["Brand"] = item

        description = response.css('div[itemprop="description"]::text').getall()

        description = (
            description.strip().replace("\n", "").replace("\t", " ")
            if description
            else ""
        )

        print(f"Product {name} Scraped Successfully")

        yield {
            "url": response.url,
            "name": name,
            "price": response.css("span.payBlkBig::text").get(),
            "discount_percent": response.css("span.pdpDiscount span::text").get(),
            "rating": response.css('span[itemprop="ratingValue"]::text').get(),
            "rating_count": response.css('span[itemprop="ratingCount"]::text').get(),
            "review_count": response.css('span[itemprop="reviewCount"]::text').get(),
            "images": response.css("img.cloudzoom::attr(src)").get(),
            "highlights": highlights,
            "description": description,
        }
