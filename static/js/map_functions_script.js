$("document").ready(() => {
    var x = 52;
    var y = 19;
    var zoom = 6;
    console.log(data_position);
    console.log(data_car);
    $("li a") .on("click", function() {
        const nazwa = $(this).attr("data-nazwa-miasta");
        x = data_position[nazwa]["x"];
        y = data_position[nazwa]["y"];
        var id_miasta = data_position[nazwa]["id"];
        zoom = 12;
        mymap.setView([x, y], zoom);
        
        $.ajax({
            type: 'GET',
            url: "/dodajmiasto/ajax/get_samochody",
            data: {"id_miasta": id_miasta, "nazwa": nazwa},
            success: function (response) {

                if(!$.isEmptyObject(response)){
                    // alert("są takie auta");
                    console.log(response);

                    licznik_id = 0;
                    for (car in response){
                        // var w = jQuery('<tr/>', {
                        //     id: 'some-id',
                        //     "class": 'some-class',
                        //     title: 'now this div has a title!'
                        // }).appendTo('#tabela_aut tbody');
                        var wiersz = document.createElement("tr");
                        var car_id = document.createElement("th");
                        // car_id.attr("scope", "row").text(licznik_id+1);
                        car_id.text(licznik_id+1);
                        var car_nazwa = document.createElement("td");
                        car_nazwa.text(car["nazwa"]);
                        var car_x = document.createElement("td");
                        var car_y = document.createElement("td");
                        car_y.text(car["pozycja"]["y"]);
                        wiersz.append(car_id, car_nazwa, car_x, car_y);
                        $("#tabela_aut tbody").append(wiersz);
                    }
                    

                }else{
                    alert("ni ma");
                }
            },
            error: function (response) {
                console.log(response);
            }
        })
    });

    
    var mymap = L.map('mapid').setView([x, y], zoom);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiYWRhbTIwMTAiLCJhIjoiY2tvZGs5M2FnMDM1NjJ3cWduYWhndWc3ZCJ9.MPKzCTkQLdAuAK46hWE-Xg'
    }).addTo(mymap);

    var marker = L.marker([50.065073, 19.921989]).addTo(mymap);
    var polygon = L.polygon([
    [51.509, -0.08],
    [51.503, -0.06],
    [51.51, -0.047]
    ]).addTo(mymap);
    function onMapClick(e) {
    alert("You clicked the map at " + e.latlng);
    } 

    mymap.on('click', onMapClick);



  

});


