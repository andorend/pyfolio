var selected = "";

function hashtag_func(clicked) {
  var hastags = document.getElementsByClassName("hashtag");
  var clicked_element = clicked.textContent;
  if (clicked_element == selected) {
    for (let item of hastags) {
      item.style.color = "white";
    }
    selected = "";
  } else {
    for (let item of hastags) {
      if (item.textContent == clicked_element) {
        item.style.color = "#ffff00";
      } else {
        item.style.color = "white";
      }
    }
    selected = clicked_element;
  }
}