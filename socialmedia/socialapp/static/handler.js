$(function() {
$("#btn_search").on("click",function(){
var keyword =$("#search").val();
window.location= "/socialapp/"+keyword+"/filter"
  });

  $("#search").autocomplete({
    source: "get_search/",
    select: function (event, ui) {
    window.location = "/socialapp/"+ui.item.id+"/post_page"
    },
    minLength: 2,
      });

    $(".test").on("click",function(){
        var id=$(this).attr(id);
        $("#id").html("ayaa");
	
alert("hhh");  
  });
});
