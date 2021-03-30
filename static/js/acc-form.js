// Input Focus
$(".acc-form-inp").each(function () {
	$(this).on("focus", function() {
		$(this).parent().parent().addClass("inp-f");
	});
	$(this).on("blur", function() {
		if($(this).val() == ""){
			$(this).parent().parent().removeClass("inp-f");
		}
	});
	$(this).on("input", function () {
		$(this).val($(this).val().replace(/ /g, ""));
	});
});

// See Password as text
$(".pass-icon-area").on("click", function() {
	if ($("#open-eye-icon").css('display')  == 'none') {
		$("#open-eye-icon").css('display', 'unset');
		$("#close-eye-icon").css('display', 'none');
		$("#acc-form-inp-pass").attr("type","password");
	} else {
		$("#open-eye-icon").css('display', 'none');
		$("#close-eye-icon").css('display', 'unset');
		$("#acc-form-inp-pass").attr("type","text");
	}
});