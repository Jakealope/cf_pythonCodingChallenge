//the variables that point to the html page items
var inItemText = document.getElementById("inItemText");
var btnNew = document.getElementById("btnAdd");
//this will start up the program by focusing on the text box
inItemText.focus();


function addNewItem(list, itemText) {
	//creates new items in a 'li' format
	var listItem = document.createElement("li");
	listItem.innerText = itemText;
	list.appendChild(listItem);
	//inserts the item at the top of the list
	list.insertBefore(listItem, list.childNodes[0]);
	//removes item on click
	listItem.onclick = function () {
		this.parentNode.removeChild(this);
	}
}
//adds item by clicking on the 'add' button
btnNew.onclick = function () {
	var itemText = inItemText.value;
	//prevents the adding of empty items including a single space
	if (!itemText || itemText === "" || itemText === " ") {
		return false;
	}

	addNewItem(document.getElementById("todoList"), itemText);
	//refocus' on the text box after addition 
	inItemText.focus();
	//and clears the contents
	inItemText.value = ""
}