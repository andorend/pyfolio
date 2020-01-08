var selected = "";


function remove_css_attribute(item, attribute) {
  if (item.getAttribute("style").search(attribute)) {
          item.style.removeProperty(attribute);
  }
}


function hashtag_clicked(active_hashtag) {
  var hashtags = document.getElementsByClassName("hashtag");
  var boxes = document.getElementsByClassName("box");
  active_hashtag_text = active_hashtag.textContent.trim();

  if (active_hashtag_text != selected) {

    selected = active_hashtag_text;
    // Find the boxes hashtags
    [...boxes].forEach( function(box){
      var box_hashtags = box.getElementsByClassName("hashtag");

      // Create list of box hashtag texts
      var box_hashtag_texts = [];

      [...box_hashtags].forEach( function(box_hashtag){
        box_hashtag_texts.push(box_hashtag.textContent.trim());
      });

      // Show only the relevant projects
      if (!(box_hashtag_texts.includes(active_hashtag_text))) {
        box.style.width = "0px";
        box.style.display = "none";
      } else {
        box.style.removeProperty("width");
        box.style.display = "flex";
      }

      // Highlight the selected hashtags
      [...box_hashtags].forEach( function(box_hashtag){
        box_hashtag_text = box_hashtag.textContent.trim();
        if (box_hashtag_text == selected) {
          box_hashtag.style.backgroundColor = "black";
        } else {
        // Remove highlight from not selected hashtags
          remove_css_attribute(box_hashtag, "background-color");
        }
      });
    });
  } else {

    // Find the boxes hashtags
    [...boxes].forEach( function(box){
      var box_hashtags = box.getElementsByClassName("hashtag");

      // Show every project
      remove_css_attribute(box, "width");
      box.style.display = "flex";

      // Remove text highlights
      [...box_hashtags].forEach( function(box_hashtag) {
        remove_css_attribute(box_hashtag, "background-color");
      });

      selected = "";

    });
  }
};


function hashtag_mouseover(active_hashtag) {

  var hashtags = document.getElementsByClassName("hashtag");
  var active_hashtag_text = active_hashtag.textContent;

  for (let hashtag of hashtags) {
    if (hashtag.textContent == active_hashtag_text) {
      hashtag.style.color = "#ffff00";
    }
  }
};


function hashtag_mouseout(active_hashtag) {

  var hashtags = document.getElementsByClassName("hashtag");
  var active_hashtag_text = active_hashtag.textContent;

  for (let hashtag of hashtags) {
    if (hashtag.textContent == active_hashtag_text) {
     hashtag.style.color = "white";
    }
  }
};

function adjust_box_size() {
  var highlighted = document.getElementsByClassName("highlighted")[0];
  var placeholder_width = document.getElementsByClassName("placeholder")[0].offsetWidth;
  var window_width = window.innerWidth;
  var nr_of_project_per_line = parseInt(Math.round(window_width / placeholder_width));
  var highlighted_flex = Math.max(nr_of_project_per_line - 1, 1);

  highlighted.style.setProperty("flex", highlighted_flex);
}
