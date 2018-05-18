
from utils.functions import ma


class StuMarch(ma.Schema):
    class Meta:

        fields = ('s_name', 's_age')


stumarsh = StuMarch()
