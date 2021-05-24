$("document").ready(() => {
  $("#tabela_aut thead").hide();

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

    console.log("dodawanie_otworz");
    otworzOkno(okno);
  }

  function otworzOkno(okno) {
    console.log(okno);
    console.log("okworzOkno");
    if (okno == null) return;
    overlay = document.getElementById("overlay");
    okno.classList.add("active");
    overlay.classList.add("active");
  }
  function zamknijOkno(okno) {
    console.log(okno);
    console.log("zamknijOkno");
    if (okno == null) return;
    overlay = document.getElementById("overlay");
    okno.classList.remove("active");
    overlay.classList.remove("active");
  }

  var wiecej_otwierajace = $(".wiecej");
  var wiecej_zamykajace = $(".okno_close_button");
  var overlay = $("#overlay");
  // console.log(wiecej_otwierajace);
  wiecej_otwierajace.on("click", (e) => {
    console.log("wiecej_otwierane");
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
