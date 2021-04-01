// * Search & Categories *
//?? Search
$("#nav-search-inp").on("click",function() {
    $(".search").addClass("visible");
    $("#nav-reset-btn").css("display", "unset");
    $(".back-to-prev").css("display", "inherit");
    $(".search-tools").css("display", "none");
});

//?? Close Search
$("#nav-reset-btn").on("click",function() {
    if ($("#nav-search-inp").val() == "") {
        $(".cats").addClass("visible");
        $(".search").removeClass("visible");
        $("#nav-reset-btn").css("display", "none");
        $(".back-to-prev").css("display", "none");
        $(".search-tools").css("display", "inherit");
    }
});

//?? Back To Categories
$(".back-to-prev").on("click", function() {
    $(".search").removeClass("visible");
    $(this).css("display", "none");
    $("#nav-reset-btn").css("display", "none");
    $(".search-tools").css("display", "inherit");
});

// nav-search-form (prevent empy search)
$(".nav-search-form").on("submit", function(event) {
    if ($(this).find('input').val() == "") {
        event.preventDefault();
        // On back-end also you shold prevent from empty search and search with whitespace
    }
});