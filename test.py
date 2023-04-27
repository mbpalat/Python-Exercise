import threading


def func():
    threading.Timer(3.0, func).start()
    print('hello')
    total_offer_count = 178
    disable_offer_count = 119
    print(total_offer_count,type(total_offer_count))
    disable_offer_by_percent = disable_offer_count/total_offer_count
    print(disable_offer_by_percent,'disable_offer_by_percent')
func()

        # product_codes = set(x.product_code for x in co_objs)
        # product_objs = Product.objects.using(self.db_name).filter(code__in=product_codes)

        # Product.objects.using(self.db_name).filter(code__in=product_codes, partner_domain__in=created_by)

        # Q(code__in=product_codes) & Q(partner_domain__in=created_by)

