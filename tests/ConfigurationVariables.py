#import configparser

#config = configparser.ConfigParser()
#config.read('config.ini')

base_url = 'http://127.0.0.1:8000'
get_order_url = base_url + '/orders'
post_order_url = base_url + '/orders'
get_order_by_id_url = base_url + '/orders/{order_id}'
delete_order_by_id_url = base_url +'/orders/{order_id}'


#base_url = config.get('DEFAULT', 'BaseUrl')
#get_order_endpoint = config.get('DEFAULT', 'GetOrdersEndpoint')
#post_order_endpoint = config.get('DEFAULT', 'PostOrderEndpoint')
#get_order_by_id_endpoint = config.get('DEFAULT', 'GetOrderByIdEndpoint')
#delete_order_by_id_endpoint = config.get('DEFAULT', 'DeleteOrderByIdEndpoint')
