def timeout_handler():
    return "The request has timed out. Please try again later.", 504

def not_found_handler(e):
    return "The requested resource was not found.", 404