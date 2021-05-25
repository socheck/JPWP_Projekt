$("document").ready(() => {
    var x = 52;
    var y = 19;
    var zoom = 6;
    var id_miasta = -1;
    console.log(data_position);
    $("#miasto li a") .on("click", function() {
        const nazwa_miasta = $(this).attr("data-nazwa-miasta");
        x = data_position[nazwa_miasta]["x"];
        y = data_position[nazwa_miasta]["y"];
        id_miasta = data_position[nazwa_miasta]["id"];
        zoom = 12;
        mymap.setView([x, y], zoom);
        $("#miasto").parent().children("button").text(nazwa_miasta);
        L.marker([data_position[nazwa_miasta]["x"], data_position[nazwa_miasta]["y"]]).addTo(mymap).bindPopup('<a href="/kontakt"> <div class="popup"> <h4>'+ nazwa_miasta +'</h4> <span>'+ "Kliknij i jedź z nami!" +"</span> </div> </a>").openPopup().on("click", ()=>{
            window.location.href = "/kontakt";
        });

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