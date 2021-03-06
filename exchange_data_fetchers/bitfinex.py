from exchange_data_fetchers import ExchangeFetcher


class BitfinexFetcher(ExchangeFetcher):
    url = 'https://api.bitfinex.com/v1/pubticker/'
    name = 'bitfinex'

    async def get_pair_value(self, cur1, cur2):
        pair = f'{cur1.lower()}{cur2.lower()}'
        url = self.url
        url += pair
        res = await self.fetcher.fetch(url)
        return (self.name, float(res['last_price']))
