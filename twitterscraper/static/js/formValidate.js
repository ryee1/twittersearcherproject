function validateForm() {
    var x = document.forms["searchForm"]["user_hashtag_input"].value;
    if (x substr(0,1))
    if (!(!/[~`!$%\^&*+=\-\[\]\\';,/{ }|\\":<>\.?]/g.test(x))) {
        alert("Name must be filled out");
        return false;
    }
}