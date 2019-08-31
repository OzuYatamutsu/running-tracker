from datetime import date


MOCK_HISTORICAL_DATA = sorted([{
    'date': date.fromisoformat('2019-08-30'),
    'weight': 135.4,
    'bp': '98/45'
}, {
    'date': date.fromisoformat('2019-08-31'),
    'weight': 134.1,
    'bp': '91/56'
}], key=lambda datapoint: datapoint['date'], reverse=True)
