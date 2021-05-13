$("document").ready(() => {
    var x = 52;
    var y = 19;
    var zoom = 6;
    // $("#tabela_aut tbody").hide();
    // $("#tabela_aut tbody").remove();
    // $("#tabela_aut thead").hide();
    $("#tabela_aut thead").hide();

    $("li a") .on("click", function() {
        const nazwa_miasta = $(this).attr("data-nazwa-miasta");
        x = data_position[nazwa_miasta]["x"];
        y = data_position[nazwa_miasta]["y"];
        var id_miasta = data_position[nazwa_miasta]["id"];
        zoom = 12;
        mymap.setView([x, y], zoom);
        $("#tabela_aut tbody").empty();
        // $("#tabela_aut tbody").remove();
        
        // $.ajax({
        //     type: 'GET',
        //     url: "/car_type_selection/ajax/get_samochody",
        //     data: {"id_miasta": id_miasta, "nazwa": nazwa},
        //     success: function (response) {

        //         if(!$.isEmptyObject(response)){
        //             // alert("są takie auta");
        //             console.log(response);

        //             licznik_id = 0;
        //             var car = response;
        //             for( var i =0; i<Object.keys(car).length; i++ ){
        //             // for (car in response){
        //                 console.log(car[i]);
        //                 L.marker([car[i]["pozycja"]["x"], car[i]["pozycja"]["y"]]).addTo(mymap);
        //                 licznik_id += 1;
        //                 $('<tr></tr>').append('<th scope = "row">'+ licznik_id +'</th>' + '<td>'+ car[i]["nazwa"] +'</td>'+ '<td>'+ car[i]["pozycja"]["x"] +'</td>'+ '<td>'+ car[i]["pozycja"]["y"] +'</td>').appendTo("#tabela_aut tbody");

        //                 $("#tabela_aut thead").show();
                        
        //             }
                    

        //         }else{
        //             alert("ni ma");
        //         }
        //     },
        //     error: function (response) {
        //         console.log(response);
        //     }
        // })

        // $("#tabela_aut thead").show();
        licznik_id = 0;
        console.log(nazwa_miasta);
        
        try {
            console.log(Object.values(data_car[nazwa_miasta]));
            Object.values(data_car[nazwa_miasta]).forEach((item) => {
                console.log(item);
                $("#tabela_aut thead").show();
                L.marker([item["pozycja"]["x"], item["pozycja"]["y"]]).addTo(mymap);
                licznik_id += 1;
                $('<tr></tr>').append('<th scope = "row">'+ '<img src="'+ item["img"] + '">'+'</th>' + '<td>'+ item["nazwa"] +'</td>'+ '<td>'+ item["kolor"] +'</td>'+ '<td>'+ item["nr_rejestracyjny"] +'</td>' +'<td>'+ item["zasieg"] +'</td>'+ '<td><div class="btn btn-primary">Więcej</div></td>'+ '<td><a class="btn btn-primary" href="/krotkoterminowy/'+item["typ_auta"]+'/'+item["id"]+'">Wynajmij</a></td>').appendTo("#tabela_aut tbody");
            });
        } catch {
            $("#tabela_aut thead").hide();
        }
        
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


