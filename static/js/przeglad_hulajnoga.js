$("document").ready(() => {
  var x = 52;
  var y = 19;
  var zoom = 6;
  $("#tabela_aut thead").hide();
  $(".content").hide();

  function dodawanie_otworz(e) {
    var okno = document.querySelector(e.target.dataset.oknoTarget);
    // console.log(okno);
    // console.log(okno.children("okno_title").text());
    var car_id = e.target.dataset.carId;
    var car_miasto = e.target.dataset.carMiasto;
    console.log(car_id);
    console.log(car_miasto);
    // wypełnianie tabeli
    var wypelnianie_okno = $("#okno");
    var car_dane = data_car[car_miasto][car_id];
    console.log(car_dane);
    document.querySelector("#okno .okno_title").innerHTML = car_dane.nazwa;

    $("#okno img").attr("src", car_dane.img);
    $("#okno tbody").empty();

    $("<tr></tr>")
      .append("<td>Marka</td>" + "<td>" + car_dane.marka + "</td>")
      .appendTo("#okno tbody");
    $("<tr></tr>")
      .append("<td>Model</td>" + "<td>" + car_dane.model + "</td>")
      .appendTo("#okno tbody");
    $("<tr></tr>")
      .append(
        "<td>Numer rejestracyjny</td>" +
          "<td>" +
          car_dane.nr_rejestracyjny +
          "</td>"
      )
      .appendTo("#okno tbody");
    $("<tr></tr>")
      .append("<td>Kolor</td>" + "<td>" + car_dane.kolor + "</td>")
      .appendTo("#okno tbody");
    $("<tr></tr>")
      .append("<td>Moc</td>" + "<td>" + car_dane.moc + "</td>")
      .appendTo("#okno tbody");
    $("<tr></tr>")
      .append("<td>Paliwo</td>" + "<td>" + car_dane.paliwo + "</td>")
      .appendTo("#okno tbody");
    $("<tr></tr>")
      .append("<td>Wyposazenie</td>" + "<td>" + car_dane.wyposazenie + "</td>")
      .appendTo("#okno tbody");
    $("<tr></tr>")
      .append("<td>Skrzynia</td>" + "<td>" + car_dane.skrzynia + "</td>")
      .appendTo("#okno tbody");
    $("<tr></tr>")
      .append("<td>Opis</td>" + "<td>" + car_dane.opis + "</td>")
      .appendTo("#okno tbody");
    $("<tr></tr>")
      .append("<td>zasieg</td>" + "<td>" + car_dane.zasieg + "</td>")
      .appendTo("#okno tbody");
    $("<tr></tr>")
      .append("<td>Typ auta</td>" + "<td>" + car_dane.typ_auta + "</td>")
      .appendTo("#okno tbody");

    //
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
    // $("#tabela_aut tbody").remove();
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
        // console.log(item);
        // var inner = document.createElement("div");
        // inner.id = item["id"];
        // inner.classList.add("pop-up");
        // var inner_title = document.createElement("div");
        // inner_title.classList.add("pop-up_nazwa");
        // inner_title.textContent = item["nazwa"];
        // var inner_buttons = document.createElement("div");
        // inner_buttons.classList.add("pop-up_buttons");
        // var button_wynajmij = document.createElement("a");
        // button_wynajmij.href = "/krotkoterminowy/hulajnoga" + "/" + item["id"];
        // var button_wynajmij_div = document.createElement("div");
        // button_wynajmij_div.classList.add("btn");
        // button_wynajmij_div.classList.add("btn-primary");
        // button_wynajmij_div.innerHTML = "Wynajmij";
        // button_wynajmij.appendChild(button_wynajmij_div);

        // inner_buttons.appendChild(button_wynajmij);
        // inner.appendChild(inner_title);
        // inner.appendChild(inner_buttons);

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
                "</td>" +
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
                "</td>" +
                '<td><a class="btn btn-primary" href="/logowanie/">Wynajmij</a></td>'
            )
            .appendTo("#tabela_aut tbody");
        }
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

  // var carIcon = L.icon({
  //   iconUrl: "/static/images/autko_marker.png",
  //   // shadowUrl: "leaf-shadow.png",

  //   iconSize: [38, 38], // size of the icon
  //   // shadowSize: [50, 64], // size of the shadow
  //   // iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
  //   // shadowAnchor: [4, 62], // the same for the shadow
  //   popupAnchor: [0, -10], // point from which the popup should open relative to the iconAnchor
  // });
});
