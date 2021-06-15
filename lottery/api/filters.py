def search_normalize(email=None,
                    limit = 30,
                    offset = 0,**data):
    return {
        "email": email, 
        "limit": limit,
        "offset": offset
            }

email_consult = "SELECT * FROM lotto WHERE email = ? \
                    LIMIT ? OFFSET ?"