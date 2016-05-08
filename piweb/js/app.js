$(function() {
    $.ajax({

        url: 'http://localhost/piweb/pi_data.php',
        type: 'GET',
        success: function(data) {
            chartData = data;
            var chartProperties = {
                "caption": "Top 10 wicket takes ODI Cricket in 2015",
                "xAxisName": "Player",
                "yAxisName": "Wickets Taken",
                "rotatevalues": "1",
                "theme": "ocean",
            "canvasBgAlpha": "0",
            //Background color and alpha
            "bgColor": "#000000",
            "bgAlpha": "70",
             "baseFontSize": "16",
            "baseFontColor": "#D3D3D3",

            };

            apiChart1 = new FusionCharts({
                type: 'column2d',
                renderAt: 'chart-container1',
                width: '550',
                height: '350',
                dataFormat: 'json',
                dataSource: {
                    "chart": chartProperties,
                    "data": chartData
                }
            });

            apiChart2 = new FusionCharts({
                type: 'column2d',
                renderAt: 'chart-container2',
                width: '550',
                height: '350',
                dataFormat: 'json',
                dataSource: {
                    "chart": chartProperties,
                    "data": chartData
                }
            });

            apiChart3 = new FusionCharts({
                type: 'column2d',
                renderAt: 'chart-container3',
                width: '550',
                height: '350',
                dataFormat: 'json',
                dataSource: {
                    "chart": chartProperties,
                    "data": chartData
                }
            });

            apiChart4 = new FusionCharts({
                type: 'column2d',
                renderAt: 'chart-container4',
                width: '550',
                height: '350',
                dataFormat: 'json',
                dataSource: {
                    "chart": chartProperties,
                    "data": chartData
                }
            });
            apiChart1.render();
            apiChart2.render();
            apiChart3.render();
            apiChart4.render();

        }
    });
});
