from mock_example.api import get_weather

def test_get_weather():
    weather = get_weather('kathmandu')
    print(weather.json())
    #assert type(weather) is dict
    assert type(weather.json()) is dict

def test_get_weather_mocked(mocker):
    mock_data = {
    "temperature": "+24 °C",
    "wind": "4 km/h",
    "description": "Light rain",
    "forecast": [
        {
        "day": "1",
        "temperature": "+26 °C",
        "wind": "3 km/h"
        },
        {
        "day": "2",
        "temperature": "21 °C",
        "wind": "4 km/h"
        },
        {
        "day": "3",
        "temperature": "28 °C",
        "wind": "3 km/h"
        }
    ]
    }

    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_data
    
    mocker.patch("requests.get", return_value = mock_response)

    result = get_weather('kathmandu')

    print(result)

    assert result.json() == mock_data 
    assert result.status_code == mock_response.status_code
    assert result.json()["temperature"] == '+24 °C'
    assert isinstance(result.json(), dict)