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
        # (Q(title__icontains=q) | Q(
        # message__icontains=q) | Q(code__icontains=q))

        #  for key, y in van_obj.iterrows():
        #  for key, x in van_settlement_objs.iterrows():

        # base_rate_objects = BaseRateMapping.objects.using(db_name)
        # base_rate_name = map(lambda base_rate_object: base_rate_objects.rate_name ,base_rate_objects)
        # base_rate_objects.delete()
        # Product.objects.using(db_name).filter(name__in=base_rate_name).delete()

        # productcodedict = {product.get('code'): product for product in products}
        # product_obj = productcodedict.get(product_code, {})
        # product_description = product_obj.get('description', '')


            #     productcodedict = {product.get('code'): product.get('description') for product in products}
            # except Exception as e:
            #     err = str(traceback.format_exc())
            #     print('Error in getting excess_short report %s on hostname: %s' % (err, hostname))

            # for key, y in van_obj.iterrows():
            #     if y.get('name') and y.get('code')
            #         name = y.get('name')
            #         code = y.get('code')
            #         vancodedict.update({
            #             code: name
            #         })

        # product_map = {x.code: x for x in product_objs}
        # partner_domain = {x.partner_domain: x for x in product_objs}
        # self.product_map = product_map
        