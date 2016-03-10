function validateForm() {
    var x = document.forms["searchForm"]["user_hashtag_input"].value;
    if (!(!/[~`!#$%\^&*+=\-\[\]\\';,/{ }|\\":<>\.?]/g.test(x))) {
        alert("Name must be filled out");
        return false;
    }
}