$("document").ready(() => {
    var x = 52;
    var y = 19;
    var zoom = 6;
    var id_miasta = -1;
    var rodzaj = "";
    $("#miasto li a") .on("click", function() {
        const nazwa = $(this).attr("data-nazwa-miasta");
        x = data_position[nazwa]["x"];
        y = data_position[nazwa]["y"];
        id_miasta = data_position[nazwa]["id"];
        zoom = 12;
        mymap.setView([x, y], zoom);
    });
    $("#rodzaj li a") .on("click", function() {
        rodzaj = $(this).attr("data-rodzaj");
    });

    
    var mymap = L.map('mapid', {drawControl: false}).setView([x, y], zoom);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiYWRhbTIwMTAiLCJhIjoiY2tvZGs5M2FnMDM1NjJ3cWduYWhndWc3ZCJ9.MPKzCTkQLdAuAK46hWE-Xg'
    }).addTo(mymap);

    // do rysowania

    var drawnItems = new L.FeatureGroup();
     mymap.addLayer(drawnItems);
     var drawControl = new L.Control.Draw({
        draw: {
             circle: false,
             rectangle: false,
             circlemarker: false,
             marker: false,
             polyline: false
         },
         edit: {
            featureGroup: drawnItems,
            // featureGroup: editableLayers,
            edit: false,
            remove: false
         }
     });
     mymap.addControl(drawControl);


    mymap.on(L.Draw.Event.CREATED, function (e) {
    var type = e.layerType,
        layer = e.layer;
    if (type === 'marker') {
        // Do marker specific actions
    };
    // Do whatever else you need to. (save to db; add to map etc)

    var lista_punktow = {};

    for(let i = 0; i<Object.keys(layer["_latlngs"]["0"]).length; i++){
        console.log(layer["_latlngs"]["0"][i]);
        var pomoc = {};
        pomoc["x"] = layer["_latlngs"]["0"][i]["lat"];
        pomoc["y"] = layer["_latlngs"]["0"][i]["lng"];
        lista_punktow[i] = pomoc;
    }
    
    // wysyłanie do bazy
    if(id_miasta == -1 || rodzaj == ""){
        alert("miasto oraz rodzaj są wymagane");
    }else{
        mymap.addLayer(layer);
        
        const serializedData = {};
        serializedData["miasto_id"] = id_miasta;
        serializedData["rodzaj_strefy"] = rodzaj;
        serializedData["punkty"] = lista_punktow;

        console.log(serializedData);

        $.ajax({
            type: 'POST',
            url: "/dodaj_strefe/ajax/post_punkty",
            data: serializedData,
            success: function (response) {
                if(!$.isEmptyObject(response)){
                    console.log(response);
                    alert("pomyślnie dodano strefę.");
                    location.reload();
                    
                }else{
                    console.log(response);
                    alert("Nie udało się dodać strefy.");
                    location.reload();
                }
                console.log(response);
                alert("pomyślnie dodano strefę.");
                location.reload();
            },
            error: function (response) {
                console.log(response);
                alert("error");
                location.reload();
            }
        })
    }

    });
    

    // koniec do rysowania

});


