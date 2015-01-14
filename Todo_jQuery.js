function addListItem() {
	//This variable gives a location for the new item
	var text = $("#inItemText").val();
    //adding the new item. prepend adds to the top, append adds
    // at the bottom
    $("#todoList").prepend('<li>' + text + '</li>');
    //sets the value of the input box to empy then focus' back
    $("#inItemText").val('').focus();
}
//function to remove the item once clicked
function deleteItem() {
	$(this).remove();
};
//action fuction
$(function () {
	//starts the program with a focus on the text box
	$("#inItemText").focus();
	//action for the add button
	$("#btnAdd").on('click', addListItem);
    //action for clicking on item to remove it
    $('ul').on('click', 'li', deleteItem);
});