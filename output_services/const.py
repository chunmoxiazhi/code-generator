
config_mapper_sample = '''
# This is an example of recursive mapping method
def config_mapper(snake_str):
    if isinstance(snake_str, dict):
        camel_dict = {}
        for key, value in snake_str.items():
            camel_key = config_mapper(key)
            camel_dict[camel_key] = config_mapper(value)
        return camel_dict

    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def generate_request_body(request_body): 
    camel_dict = {}
    for key, value in request_body.items():
        camel_key = config_mapper(key)
        if isinstance(value, dict):
            camel_dict[camel_key] = config_mapper(value)
        else:
            camel_dict[camel_key] = value
    return camel_dict
'''
