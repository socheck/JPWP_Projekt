$("document").ready(() => {
  var x = 52;
  var y = 19;
  var zoom = 6;
  $("#tabela_aut thead").hide();
  $(".content").hide();

  function dodawanie_otworz(e) {
    var okno = document.querySelector(e.target.dataset.oknoTarget);

    var car_id = e.target.dataset.carId;
    var car_miasto = e.target.dataset.carMiasto;
    console.log(car_id);
    console.log(car_miasto);

    var wypelnianie_okno = $("#okno");
    var car_dane = data_car[car_miasto][car_id];
    console.log(car_dane);
    document.querySelector("#okno .okno_title").innerHTML = car_dane.nazwa;

    $("#okno img").attr("src", car_dane.img);
    $("#okno tbody").empty();

    $("<tr></tr>")
      .append("<td>Miasto</td>" + "<td>" + car_dane.miasto + "</td>")
      .appendTo("#okno tbody");
    $("<tr></tr>")
      .append("<td>Paliwo</td>" + "<td>" + "energia elektryczna" + "</td>")
      .appendTo("#okno tbody");
    $("<tr></tr>")
      .append("<td>Cena</td>" + "<td>" + car_dane.cena + " zł/min</td>")
      .appendTo("#okno tbody");
    $("<tr></tr>")
      .append("<td>zasieg</td>" + "<td>" + car_dane.zasieg + " km</td>")
      .appendTo("#okno tbody");

    otworzOkno(okno);
  }

  function otworzOkno(okno) {
    if (okno == null) return;
    okno.classList.add("active");
    overlay.classList.add("active");
  }
  function zamknijOkno(okno) {
    if (okno == null) return;
    okno.classList.remove("active");
    overlay.classList.remove("active");
  }

  $("li a").on("click", function () {
    const nazwa_miasta = $(this).attr("data-nazwa-miasta");
    x = data_position[nazwa_miasta]["x"];
    y = data_position[nazwa_miasta]["y"];
    var id_miasta = data_position[nazwa_miasta]["id"];
    zoom = 12;
    mymap.setView([x, y], zoom);
    $("#tabela_aut tbody").empty();

    $("#tabela_aut thead").hide();
    $(".content").hide();

    var list_punktow = [];

    for (let punkt in data_strefy[id_miasta]) {
      list_punktow.push([
        data_strefy[id_miasta][punkt].x,
        data_strefy[id_miasta][punkt].y,
      ]);
    }

    L.polygon(list_punktow).addTo(mymap);

    try {
      Object.values(data_car[nazwa_miasta]).forEach((item) => {
        var inner = document.createElement("div");
        inner.id = item["id"];
        inner.classList.add("pop-up");
        var inner_title = document.createElement("div");
        inner_title.classList.add("pop-up_nazwa");
        inner_title.textContent = item["nazwa"];
        var inner_buttons = document.createElement("div");
        inner_buttons.classList.add("pop-up_buttons");
        var button_wiecej = document.createElement("div");
        button_wiecej.classList.add("wiecej");
        button_wiecej.classList.add("btn");
        button_wiecej.classList.add("btn-primary");
        button_wiecej.dataset.carMiasto = nazwa_miasta;
        button_wiecej.dataset.carId = item["id"];
        button_wiecej.dataset.oknoTarget = "#okno";
        button_wiecej.addEventListener("click", dodawanie_otworz);
        button_wiecej.innerHTML = "Więcej";
        var button_wynajmij = document.createElement("a");
        if (authentication) {
          button_wynajmij.href =
            "/krotkoterminowy/hulajnoga" + "/" + item["id"];
        } else {
          button_wynajmij.href = "/logowanie/";
        }

        var button_wynajmij_div = document.createElement("div");
        button_wynajmij_div.classList.add("btn");
        button_wynajmij_div.classList.add("btn-primary");
        button_wynajmij_div.innerHTML = "Wynajmij";
        button_wynajmij.appendChild(button_wynajmij_div);
        inner_buttons.appendChild(button_wiecej);
        inner_buttons.appendChild(button_wynajmij);
        inner.appendChild(inner_title);
        inner.appendChild(inner_buttons);

        $("#tabela_aut thead").show();
        $(".content").show();
        L.marker([item["pozycja"]["x"], item["pozycja"]["y"]], {
          icon: carIcon,
        })
          .addTo(mymap)
          .bindPopup(inner);

        if (authentication) {
          $("<tr></tr>")
            .append(
              '<th scope = "row">' +
                '<img src="' +
                item["img"] +
                '">' +
                "</th>" +
                "<td>" +
                item["nazwa"] +
                "</td>" +
                "<td>" +
                item["zasieg"] +
                " km</td>" +
                '<td><div data-car-miasto = "' +
                nazwa_miasta +
                '" data-car-id = "' +
                item["id"] +
                '" data-okno-target="#okno" class="btn btn-primary wiecej">Więcej</div></td>' +
                '<td><a class="btn btn-primary" href="/krotkoterminowy/hulajnoga' +
                "/" +
                item["id"] +
                '">Wynajmij</a></td>'
            )
            .appendTo("#tabela_aut tbody");
        } else {
          $("<tr></tr>")
            .append(
              '<th scope = "row">' +
                '<img src="' +
                item["img"] +
                '">' +
                "</th>" +
                "<td>" +
                item["nazwa"] +
                "</td>" +
                "<td>" +
                item["zasieg"] +
                " km</td>" +
                '<td><div data-car-miasto = "' +
                nazwa_miasta +
                '" data-car-id = "' +
                item["id"] +
                '" data-okno-target="#okno" class="btn btn-primary wiecej">Więcej</div></td>' +
                '<td><a class="btn btn-primary" href="/logowanie/">Wynajmij</a></td>'
            )
            .appendTo("#tabela_aut tbody");
        }

        var wiecej_otwierajace = $(".wiecej");
        var wiecej_zamykajace = $(".okno_close_button");
        var overlay = $("#overlay");

        wiecej_otwierajace.on("click", (e) => {
          dodawanie_otworz(e);
        });

        wiecej_zamykajace.on("click", (e) => {
          var okno = e.target.closest(".okno");
          zamknijOkno(okno);
        });

        overlay.on("click", () => {
          const okna = document.querySelectorAll(".okno.active");
          okna.forEach((okno) => {
            zamknijOkno(okno);
          });
        });
      });
    } catch {
      $("#tabela_aut thead").hide();
      $(".content").hide();
    }
  });

  var mymap = L.map("mapid").setView([x, y], zoom);
  L.tileLayer(
    "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
    {
      attribution:
        'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      maxZoom: 18,
      id: "mapbox/streets-v11",
      tileSize: 512,
      zoomOffset: -1,
      accessToken:
        "pk.eyJ1IjoiYWRhbTIwMTAiLCJhIjoiY2tvZGs5M2FnMDM1NjJ3cWduYWhndWc3ZCJ9.MPKzCTkQLdAuAK46hWE-Xg",
    }
  ).addTo(mymap);

  var carIcon = L.icon({
    iconUrl: "/static/images/hulajnoga_marker.png",
    // shadowUrl: "leaf-shadow.png",

    iconSize: [34, 34], // size of the icon
    // shadowSize: [50, 64], // size of the shadow
    // iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
    // shadowAnchor: [4, 62], // the same for the shadow
    popupAnchor: [0, -10], // point from which the popup should open relative to the iconAnchor
  });
});
