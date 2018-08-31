var gaugeOptions = {

  chart: {
    type: 'solidgauge'
  },

  title: null,

  pane: {
    center: ['50%', '85%'],
    size: '140%',
    startAngle: -90,
    endAngle: 90,
    background: {
      backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || '#EEE',
      innerRadius: '60%',
      outerRadius: '100%',
      shape: 'arc'
    }
  },

  tooltip: {
    enabled: false
  },

  // the value axis
  yAxis: {
    stops: [
      [0.1, '#55BF3B'], // green
      [0.5, '#DDDF0D'], // yellow
      [0.9, '#DF5353'] // red
    ],
    lineWidth: 0,
    minorTickInterval: null,
    tickAmount: 2,
    title: {
      y: -70
    },
    labels: {
      y: 16
    }
  },

  plotOptions: {
    solidgauge: {
      dataLabels: {
        y: 5,
        borderWidth: 0,
        useHTML: true
      }
    },
    series: {
            animation: {
                duration: 0.5
            }
        }
  }
};

function plot_donut(donut_location_name, number_of_people, capacity) {

  // The speed gauge
  var chart = Highcharts.chart(donut_location_name, Highcharts.merge(gaugeOptions, {
    yAxis: {
      min: 0,
      max: capacity,
      title: {
        text: ''
      }
    },

    credits: {
      enabled: false
    },

    series: [{
      name: 'Count',
      data: [number_of_people],
      dataLabels: {
        format: '<div style="text-align:center"><span style="font-size:25px;color:' +
          ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y}</span><br/>' +
             '<span style="font-size:12px;color:silver">Visitors</span></div>'
      },
      tooltip: {
        valueSuffix: 'visitors'
      }
    }]

  }));

  return chart;
}

