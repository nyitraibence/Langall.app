var lang_chart_1 = document.getElementById('language-popularity-chart');
var myChart = new Chart(lang_chart_1, {
    type: 'bar',
    data: {
        labels: ['Angol', 'Spanyol', 'Német', 'Olasz', 'Orosz', 'Kínai'],
        datasets: [{
            label: '# nyelvek iránti érdeklődés',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor:
                'rgba(255, 99, 132, 0.2)',
            borderColor:
                'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            xAxes: [{
                gridLines: {
                    display: false
                }
            }],
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                gridLines: {
                    display: false
                }
            }]
        }
    }
});