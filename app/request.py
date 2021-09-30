from .models import Quote
import urllib.request,json
def get_quote():
    get_quote_details_url = QUOTES_API_BASE_URL.format(id)

    with urllib.request.urlopen(get_quote_details_url) as url:
        quote_details_data = url.read()
        quote_details_response = json.loads(quote_details_data)

        quote_object = None
        if quote_details_response:

            author = _response.get('author')
            title = quote_details_response.get('original_title')
            text = quote_details_response.get('quote')

            new_quote = QUOTE(author,text)
            quote_details.append(new_quote)

    return quote_details

# Getting api key
QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
