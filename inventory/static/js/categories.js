// Define inventory data
const inventoryData = [
    { name: "Lettuce", category: "Vegetables", quantity: 10, unitPrice: 1.50 },
    // Other inventory items...
];

// Function to add item to cart
function addItemToCart(name, category, quantity, unitPrice, totalPrice) {
    const cartTable = document.getElementById("cartTable");
    const tbody = cartTable.querySelector("tbody");

    // Create a new row
    const newRow = document.createElement("tr");

    // Fill the row with data
    newRow.innerHTML = `
        <td>${name}</td>
        <td>${category}</td>
        <td>${quantity}</td>
        <td>$${unitPrice.toFixed(2)}</td>
        <td>$${totalPrice.toFixed(2)}</td>
        <td><button onclick="removeItem(this)">Remove</button></td>
    `;

    // Append the row to the table
    tbody.appendChild(newRow);

    // Calculate and display total price
    const totalPriceElement = document.getElementById("totalPrice");
    const currentTotalPrice = parseFloat(totalPriceElement.textContent.split(":")[1].trim().replace('$', ''));
    const newTotalPrice = currentTotalPrice + totalPrice;
    totalPriceElement.textContent = `Total Price: $${newTotalPrice.toFixed(2)}`;
}

// Function to remove item
function removeItem(button) {
    const row = button.parentNode.parentNode;
    const totalPrice = parseFloat(row.cells[4].textContent.replace('$', ''));

    // Remove the row from the table
    row.parentNode.removeChild(row);

    // Update total price
    const totalPriceElement = document.getElementById("totalPrice");
    const currentTotalPrice = parseFloat(totalPriceElement.textContent.split(":")[1].trim().replace('$', ''));
    const newTotalPrice = currentTotalPrice - totalPrice;
    totalPriceElement.textContent = `Total Price: $${newTotalPrice.toFixed(2)}`;
}

// Event listener for add button click
document.getElementById("addBtn").addEventListener("click", function() {
    const selectedCategory = document.getElementById("category").value;
    let selectedProduce;
    let selectedWeight;

    switch (selectedCategory) {
        case 'vegetables':
            selectedProduce = document.getElementById("vegetableProduce").value;
            selectedWeight = calculateWeightInPounds(document.getElementById("quantity").value);
            document.getElementById("vegetableWeight").textContent = selectedWeight + " lbs";
            break;
        case 'meat':
            selectedProduce = document.getElementById("meatProduce").value;
            selectedWeight = calculateWeightInPounds(document.getElementById("quantity").value);
            document.getElementById("meatWeight").textContent = selectedWeight + " lbs";
            break;
        case 'frozen':
            selectedProduce = document.getElementById("frozenProduce").value;
            break;
        case 'beverages':
            selectedProduce = document.getElementById("beverageProduce").value;
            break;
        default:
            break;
    }

    const selectedQuantity = document.getElementById("quantity").value;
    const selectedItem = inventoryData.find(item => item.name === selectedProduce);

    if (selectedItem) {
        const totalPrice = selectedItem.unitPrice * selectedQuantity;
        addItemToCart(selectedItem.name, selectedItem.category, selectedQuantity, selectedItem.unitPrice, totalPrice);
    } else {
        alert("Item not found in inventory!");
    }
});
