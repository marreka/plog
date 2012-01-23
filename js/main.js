function initialize() {
  var myOptions = {
    center: MAP_CENTER,
    zoom: ZOOM,
    panControl: false,
    mapTypeControl: false,
    streetViewControl: false,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

  var routeTableLayer = new google.maps.FusionTablesLayer({
    query: {
      select: 'geometry',
      from: TABLE_ID,
      where: WHERE_CONDITION,
    },
    styles: [{
      polylineOptions: {
        strokeColor: "#FF0000",
        strokeWeight: "4",
      }
    }, {
      where: "date = '" + TODAY + "'",
      markerOptions: {
        iconName: "grn_diamond",
      },
      polylineOptions: {
        strokeColor: "#00FF00",
        strokeWeight: "6",
      },
    }, {
      where: "date < '" + TODAY + "'",
      polylineOptions: {
        strokeColor: "#0000FF",
        strokeWeight: "2",
      },
    },]
  });
  routeTableLayer.setMap(map);
}