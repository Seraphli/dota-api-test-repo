import od_python
from od_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = od_python.MatchesApi()
match_id = 3328375973 # int |

try:
    # GET /matches/{match_id}
    api_response = api_instance.matches_match_id_get(match_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->matches_match_id_get: %s\n" % e)