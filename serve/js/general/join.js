$(document).on("click", ".role--learn-more", function(){
    const $this = $(this);

    $this.parent().parent().find(".role-details").toggle();
});

let roles = {};
function generateRole(role){
  role = $.trim(role);

  if(!roles[role]){
    $("#filter-roles").append(`<button data-type='${role.replace(" ", "-")}' class='role-filter slim'>${role}</button>`);

    roles[role] = true;
  }
}

// load Roles
function findRoles(){
  $(".role-type").each(function(){
    generateRole($(this).text());
  })
}


let filter = {};
$(document).on("click", ".role-filter", function(){
  let type = $(this).data("type");
  filter[type] = (filter[type]) ? false : true;
  $(this).toggleClass("selected");
  updateFilter();
});

function updateFilter(){
  let vis = 0;
  $(".role-container").css("display", "none");

  for(let i in filter){
    if(filter[i]){
      $(".role--type-" + i).css("display", "block");
      vis++;
    }

  }

  if(vis === 0){
    $(".role-container").css("display", "block");
  }


}
