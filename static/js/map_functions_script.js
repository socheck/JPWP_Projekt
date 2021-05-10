$("document").ready(() => {
    var x = 52;
    var y = 19;
    var zoom = 6;
    $("li a") .on("click", function() {
        const nazwa = $(this).attr("data-nazwa-miasta");
        x = data_position[nazwa]["x"];
        y = data_position[nazwa]["y"];
        var id_miasta = data_position[nazwa]["id"];
        zoom = 12;
        mymap.setView([x, y], zoom);
        $("#tabela_aut tbody").empty();
        
        $.ajax({
            type: 'GET',
            url: "/dodajmiasto/ajax/get_samochody",
            data: {"id_miasta": id_miasta, "nazwa": nazwa},
            success: function (response) {

                if(!$.isEmptyObject(response)){
                    // alert("są takie auta");
                    console.log(response);

                    licznik_id = 0;
                    var car = response;
                    for( var i =0; i<Object.keys(car).length; i++ ){
                    // for (car in response){
                        console.log(car[i]);
                        L.marker([car[i]["pozycja"]["x"], car[i]["pozycja"]["y"]]).addTo(mymap);
                        licznik_id += 1;
                        $('<tr></tr>').append('<th scope = "row">'+ licznik_id +'</th>' + '<td>'+ car[i]["nazwa"] +'</td>'+ '<td>'+ car[i]["pozycja"]["x"] +'</td>'+ '<td>'+ car[i]["pozycja"]["y"] +'</td>').appendTo("#tabela_aut tbody");
                        
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


