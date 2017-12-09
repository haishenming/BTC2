
from ..models import Okex


def get_new_okex_data():

    return Okex.query.filter_by()