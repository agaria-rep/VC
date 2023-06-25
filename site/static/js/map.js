var jsons;
var map = L.map('map').setView([0, 0], 3);

var point_marker = L.icon({
    iconUrl: '/static/images/map/point_marker.png',
    iconSize: [16, 16]
});

var capital_point_marker = L.icon({
    iconUrl: '/static/imgs/images/capital_point_marker.png',
    iconSize: [16, 16]
});

async function loadMap() {
    const json = await fetch("https://oovc.piwerm.repl.co/map").json();

    L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/terrain-background/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 6,
        minZoom: 2
    }).addTo(map);

    json.forEach(function(element) {
        let id = element.id;
        let name = element.name;
        let flag = element.flag;
        let description = element.description;
        let geojson = element.geojson;

        L.geoJSON(geojson, {
            style: function(feature) {return {fillColor: feature.properties.fill, color: feature.properties.stroke}},
            pointToLayer: function(geoJsonPoint, latlng) {return L.marker(latlng, {icon: point_marker});},
            onEachFeature: function (feature, layer) {
                layer.bindPopup(`<div class="popup"><img src="${flag}" alt="Flag of Country"><a href="/countries/${id}">${name}</a><p>${description}</p></div>`);
            }
        });
    });
}