function myMap() {
  var orlando = new google.maps.LatLng(28.453375, -81.472395);
  var image = '../images/broom.png';

  var mapCanvas = document.getElementById("map");
  var mapOptions = {center: orlando, zoom: 10};
  var map = new google.maps.Map(mapCanvas,mapOptions);

  var marker = new google.maps.Marker({
    position:orlando,
    animation: google.maps.Animation.DROP,
    // icon: '/Users/aboubacardaman/Documents/dev/mydjango/myprojects/src/static/magicassets/images/broom.png'
  });
  marker.setMap(map);
  var infowindow = new google.maps.InfoWindow({
    content: "<h4>Magic Broom Cleaning Service</h4>\
                <p> Servicing Orlando Area, FL</p>"
  });

  // infowindow.open(map, marker);

  var myCity = new google.maps.Circle({
    center: orlando,
    radius: 32000,
    strokeColor: "#0000FF",
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: "#0000FF",
    fillOpacity: 0.4
  });
  myCity.setMap(map);
  google.maps.event.addListener(marker,'click',function() {
      var pos = map.getZoom();
      map.setZoom(13);
      map.setCenter(marker.getPosition());
      window.setTimeout(function() {map.setZoom(pos);},3000);
      infowindow.open(map, marker);
    });



}
