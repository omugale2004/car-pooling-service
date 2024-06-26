from jsonschema import Draft4Validator

signup_post_schema = {
}

signup_put_schema = {
}


v_post = Draft4Validator(signup_post_schema)
v_put = Draft4Validator(signup_put_schema)


def validate_post_data(request_data):
    return [{ 
            'field': 'non_field_error',
            'code': 1000,
            'client_message': x.message,
            'server_message': x.message
        } for x in v_post.iter_errors(request_data)]


def validate_put_data(request_data):
    return [{ 
            'field': 'non_field_error',
            'code': 1000,
            'client_message': x.message,
            'server_message': x.message
        } for x in v_put.iter_errors(request_data)]

