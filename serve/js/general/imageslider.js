function injectImages(slider){
  const total_image_set = 4;

  // inject images async
  function renderTemplate(state){
    return `<div
              class='image-element image-element-${state}'
              style='background-image:url(https://s3-us-west-1.amazonaws.com/hackmerced/look_back_2017/${state}.png)'
              ></div>`
  }

  for(let i = 1; i <= total_image_set; i++){
    slider.innerHTML += renderTemplate(i);
  }
}

function imageSlider() {
  let slider = document.getElementById("image_slider");

  injectImages(slider);

  //
  //     console.log(state);
  // setInterval(function(){
  //   state++;
  //   console.log(state);
  //   slider.style['background-image'] = 'url(https://s3-us-west-1.amazonaws.com/hackmerced/look_back_2017/' + state + '.png)';
  // }, 2500);
}
