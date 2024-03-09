// static/js/inventory.js

document.addEventListener('DOMContentLoaded', function () {
    const categorySelect = document.getElementById('category-select');
    const inventoryList = document.getElementById('inventory-list');

    categorySelect.addEventListener('change', function () {
        const selectedCategoryId = categorySelect.value;
        const categories = inventoryList.querySelectorAll('.category');

        categories.forEach(category => {
            if (selectedCategoryId === '' || category.dataset.category === selectedCategoryId) {
                category.style.display = 'block';
            } else {
                category.style.display = 'none';
            }
        });
    });
});
