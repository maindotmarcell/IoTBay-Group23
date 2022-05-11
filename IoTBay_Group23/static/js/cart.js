// console.log('Hello world!');
const updateBtns = document.getElementsByClassName('update-cart');

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function () {
		const productID = this.dataset.product;
		const action = this.dataset.action;
		console.log(`Product ID: ${productID}, action: ${action}`);
		console.log(`USER: ${user}`);
		if (user === 'AnonymousUser') console.log('Not logged in');
		else updateUserOrder(productID, action);
	});
}

const updateUserOrder = (productID, action) => {
	console.log(`User is logged in, sending data...`);

	const url = '/update_item/';
	fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,
		},
		body: JSON.stringify({ productID: productID, action: action }),
	})
		.then((response) => {
			return response.json();
		})

		.then((data) => {
			location.reload();
		});
};
