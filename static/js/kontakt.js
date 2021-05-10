$("document").ready(() => {
    var x = 52;
    var y = 19;
    var zoom = 6;
    var id_miasta = -1;
    console.log(data_position);
    console.log(data_oddzialy);

    $("#tabela_oddzialow").hide();

    $("#miasto li a") .on("click", function() {
        const nazwa_miasta = $(this).attr("data-nazwa-miasta");
        x = data_position[nazwa_miasta]["x"];
        y = data_position[nazwa_miasta]["y"];
        id_miasta = data_position[nazwa_miasta]["id"];
        zoom = 12;
        mymap.setView([x, y], zoom);
        $("#miasto").parent().children("button").text(nazwa_miasta);
        $("#tabela_oddzialow tbody").empty();
        $("#tabela_oddzialow").hide();
     

        for(var i = 1; i <= Object.keys(data_oddzialy).length; i++){
            if(data_oddzialy[i]["nazwa_miasta"] == nazwa_miasta){
                L.marker([data_oddzialy[i]["position"]["x"], data_oddzialy[i]["position"]["y"]]).addTo(mymap).bindPopup("<b class = 'test'>Adres</b><br>" + data_oddzialy[i]["adres"]);

                $("#tabela_oddzialow").show();
                $('<tr></tr>').append('<th scope = "row">'+ i +'</th>' + '<td>'+ data_oddzialy[i]["adres"] +'</td>').appendTo("#tabela_oddzialow tbody");
                
            }
            
        }

    });
    $("#rodzaj li a") .on("click", function() {
        rodzaj = $(this).attr("data-rodzaj");
        $("#rodzaj").parent().children("button").text(rodzaj);
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
    

});