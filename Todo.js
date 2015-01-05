var inItemText = document.getElementById("inItemText");
inItemText.focus();
var btnNew = document.getElementById("btnAdd");

function addNewItem(list, itemText) {
	var listItem = document.createElement("li");
	listItem.innerText = itemText;
	list.appendChild(listItem);
	list.insertBefore(listItem, list.childNodes[0]);
	listItem.onclick = function () {
		this.parentNode.removeChild(this);
	}
}

btnNew.onclick = function () {
	var itemText = inItemText.value;
	if (!itemText || itemText === "" || itemText === " ") {
		return false;
	}

	addNewItem(document.getElementById("todoList"), itemText);

	inItemText.focus();
	inItemText.value = ""
}