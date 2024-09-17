document.getElementById('productForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(this);

    fetch('/add_product', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                loadProducts();
                document.getElementById('name').value = '';
            } else {
                alert(data.message);
            }
        });
});


function loadProducts() {
    fetch('/get_products')
        .then(response => response.json())
        .then(products => {
            const productList = document.getElementById('productList');
            productList.innerHTML = '';
            products.forEach(product => {
                const li = document.createElement('li');
                li.textContent = `${product.name}`;
                productList.appendChild(li);
            });
        });
}

document.getElementById('viewList').addEventListener('click', function(){
    document.getElementById('productListGroup').style.display = 'flex';
    document.getElementById('productForm').style.display = 'none';
})

document.getElementById('addProduct').addEventListener('click', function(){
    document.getElementById('productListGroup').style.display = 'none';
    document.getElementById('productForm').style.display = 'flex';
})

document.getElementById('copyButton').addEventListener('click', function() {
    const productList = document.getElementById('productList');
    let textToCopy = '';
    productList.querySelectorAll('li').forEach(li => {
        textToCopy += li.textContent + '\n';
    });

    navigator.clipboard.writeText(textToCopy)
        .then(() => {
            alert('Product list copied to clipboard!');
        })
        .catch(err => {
            console.error('Failed to copy: ', err);
        });
});

loadProducts();