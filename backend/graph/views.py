from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.enums import DurationTypeEnum, DurationSelectionEnum
import datetime
import cryptocompare

cryptocompare.cryptocompare._set_api_key_parameter(settings.CRYPTOCOMPARE_API_KEY )


class HistoricalData(APIView):

    def __init__(self):
        self.currency = 'USD'
        self.exchange = 'CCCAGG'

    def get(self, request):
        self.coin = request.GET.get('coin', 'BTC')
        duration_selection = int(request.GET.get('durationSelection', DurationSelectionEnum.PREDEFINED.value))
        if duration_selection == DurationSelectionEnum.PREDEFINED.value:
            duration_type = int(request.GET.get('durationType', DurationTypeEnum.HOUR.value))
            duration = int(request.GET.get('duration', 1))
            if duration_type == DurationTypeEnum.HOUR.value:
                response = self.get_data_by_minute(duration)
            elif duration_type == DurationTypeEnum.DAY.value:
                response = self.get_data_by_hour()
            elif duration_type in [DurationTypeEnum.WEEK.value, DurationTypeEnum.MONTH.value]:
                response = self.get_data_by_day(duration_type)
            elif duration_type == DurationTypeEnum.YEAR.value:
                # TODO: implement year data
                pass
        elif duration_selection == DurationSelectionEnum.CUSTOM.value:
            # TODO: implement custom range
            pass
        return Response(response)

    def get_data_by_minute(self, duration):
        limit = duration*60
        return cryptocompare.get_historical_price_minute(
            self.coin, self.currency, limit=limit, exchange=self.exchange, toTs=datetime.datetime.now())

    def get_data_by_hour(self):
        return cryptocompare.get_historical_price_hour(
            self.coin, self.currency, limit=24, exchange=self.exchange, toTs=datetime.datetime.now())

    def get_data_by_day(self, duration_type):
        limit = 7 if duration_type == DurationTypeEnum.WEEK.value else 30
        return cryptocompare.get_historical_price_day(
            self.coin, self.currency, limit=limit, exchange=self.exchange, toTs=datetime.datetime.now())