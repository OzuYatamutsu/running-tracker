from datetime import date


MOCK_HISTORICAL_DATA = sorted([{
    'date': date.fromisoformat('2019-08-30'),
    'weight': 135.4,
    'bp_systolic': 98,
    'bp_diastolic': 49
}, {
    'date': date.fromisoformat('2019-08-31'),
    'weight': 134.1,
    'bp_systolic': 91,
    'bp_diastolic': 56
}], key=lambda datapoint: datapoint['date'])


MOCK_TEMPLATED_HISTORICAL_DATA = {
    'datapoints': MOCK_HISTORICAL_DATA[::1],
    'chart_legend': [
        datapoint['date'] for datapoint in MOCK_HISTORICAL_DATA
    ],
    'chart_weight_datapoints': [
        datapoint['weight'] for datapoint in MOCK_HISTORICAL_DATA
    ],
    'chart_bp_systolic_datapoints': [
        datapoint['bp_systolic'] for datapoint in MOCK_HISTORICAL_DATA
    ],
    'chart_bp_diastolic_datapoints': [
        datapoint['bp_diastolic'] for datapoint in MOCK_HISTORICAL_DATA
    ]
}
