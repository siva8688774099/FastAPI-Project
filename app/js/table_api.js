fetch('http://127.0.0.1:8000/table')
	.then(response => response.json())
	.then(data=>{
	const table = document.getElementById('main-table');
	data.forEach(user => {
		console.log(user);

		const row = document.createElement('tr');

		const username = document.createElement('td');
		username.textContent = user.username;
		row.appendChild(username);

		const email = document.createElement('td');
		email.textContent = user.email;
		row.appendChild(email);

		const mobile = document.createElement('td');
		mobile.textContent = user.mobile;
		row.appendChild(mobile);
		
		const imagecell = document.createElement('td');
		const image = document.createElement('img');
		image.src = "data:image/jpeg;base64,"+user.image;
		image.width = 80;
		image.height = 80;
		imagecell.style.padding = "0%"
		imagecell.appendChild(image);

		row.appendChild(imagecell);

		table.appendChild(row);
	});
});
