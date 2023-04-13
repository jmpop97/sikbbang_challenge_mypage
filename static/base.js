// $(".qna_edit").hide()
$(".slide_nav").hide()

var isNavVisible = false;

$(".xi-bars").click(function () {
  if (isNavVisible) {
    $(".slide_nav").fadeOut(500)
  } else {
    $(".slide_nav").fadeIn(500)
  }
  isNavVisible = !isNavVisible;
});

document.getElementById(".xi-bars")