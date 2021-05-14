$("document").ready(() => {
  //to dlugoterminowego pierdolniemy cenę under the hood ajaxem i będzie git a typ auta możemy w urlu
  // chyba że to jebać
  // var wybrany_typ = "tir";
  // var zaznaczona_cena = 5;
  // $.ajax({
  //     type: 'POST',
  //     // wszystko ajaxem
  //     // url: "/dlugoterminowy/",
  //     // data: JSON.stringify({"cena": zaznaczona_cena, "typ_pojazdu": wybrany_typ}),
  //     url: "/dlugoterminowy/"+wybrany_typ,
  //     data: JSON.stringify({"cena": zaznaczona_cena}),
  //     success: function (response) {
  //         if(!$.isEmptyObject(response)){
  //             // console.log(response);
  //             alert(response["message"]);
  //             location.reload();
  //         }else{
  //             // console.log(response);
  //             alert("Nie udało się dodać strefy.");
  //             location.reload();
  //         }
  //     },
  //     error: function (response) {
  //         console.log(response);
  //         alert("error");
  //         location.reload();
  //     }
  // })
  // wpisywanie ceny do forma
  // var cena = 5;
  // $("#submit").on("click", ()=>{
  //     $("#cena").attr("value", cena);
  // });
});
