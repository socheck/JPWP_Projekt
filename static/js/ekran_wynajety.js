$("document").ready(() => {
  //   let [seconds, minutes, hours] = [0, 0, 0];
  let seconds = data_wynajem.startowy_czas.s;
  let minutes = data_wynajem.startowy_czas.m;
  let hours = data_wynajem.startowy_czas.h;
  let timerRef = document.querySelector(".timerDisplay");
  let int = null;
  let cena = document.getElementById("cena");
  cena.innerHTML =
    "Cena: " +
    (data_wynajem.cena_wartosc * (minutes + 60 * hours + 1)).toFixed(2) +
    " zł";
  let nazwa_pojazdu = document.getElementById("nazwa_pojazdu");
  nazwa_pojazdu.innerHTML = "Wynajęty pojazd: " + data_wynajem.nazwa_pojazdu;
  let data_rozpoczecia = document.getElementById("data_rozpoczecia");
  data_rozpoczecia.innerHTML =
    "Rozpoczęcie wynajmu: " + data_wynajem.data_start;
  let nr_karty = document.getElementById("nr_karty");
  nr_karty.innerHTML =
    "Nr karty: &bull;&bull;&bull;" + data_wynajem.nr_karty.slice(-4);

  if (int !== null) {
    clearInterval(int);
  }
  int = setInterval(displayTimer, 1000);

  document.getElementById("pauseTimer").addEventListener("click", () => {
    clearInterval(int);
    alert("Zwracamy, zwracamy... i wysyłam POST na backend");
    // $.ajax({
    //   type: "POST",
    //   url: "/cos/tam/url",
    //   data: JSON.stringify({
    //     id_pojazdu: data_wynajem.id_pojazdu,
    //     user_id: data_wynajem.user_id,
    //   }),
    //   success: function (response) {
    //     if (!$.isEmptyObject(response)) {
    //       console.log(response);
    //       alert("udało się więc nie powinno tego być");
    //     }
    //   },
    //   error: function (response) {
    //     console.log(response);
    //     alert("error");
    //   },
    // });
  });

  function displayTimer() {
    seconds += 1;
    // cena.innerHTML =
    //   "Cena: " +
    //   (
    //     data_wynajem.cena_wartosc *
    //     (seconds + 60 * minutes + 3600 * hours)
    //   ).toFixed(2) +
    //   " zł";
    if (seconds == 60) {
      seconds = 0;
      minutes++;
      cena.innerHTML =
        "Cena: " +
        (data_wynajem.cena_wartosc * (minutes + 60 * hours + 1)).toFixed(2) +
        " zł";
      if (minutes == 60) {
        minutes = 0;
        hours++;
      }
    }

    let h = hours < 10 ? "0" + hours : hours;
    let m = minutes < 10 ? "0" + minutes : minutes;
    let s = seconds < 10 ? "0" + seconds : seconds;

    timerRef.innerHTML = ` ${h} : ${m} : ${s}`;
  }
});
