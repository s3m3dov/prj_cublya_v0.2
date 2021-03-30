// Password Validation
// /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{10,}$/
// /^(?=.*?[0-9])(?=.*?[A-Z])(?=.*?[#?!@$%^&*\-_]).{10,}$/

var regex = new RegExp(/^(?=.*?[0-9])(?=.*?[A-Z])(?=.*?[#?!@$%^&*\-_]).{10,}$/)

$("#acc-form-inp-pass").on("keyup", function() {
	if(regex.test($(this).val())) {
		$(this).parent().parent().addClass("inp-v");
		$(this).parent().parent().removeClass("inp-i");
	} else {
		$(this).parent().parent().addClass("inp-i");
		$(this).parent().parent().removeClass("inp-v");
	}
});

// You also do password validation on back-end