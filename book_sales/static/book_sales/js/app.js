/* Configuration */

const API = {
	books: '/api/books',
	sales: '/api/booksales/',
	search: '/api/booksales/search/',
	trends: '/api/booksales/sales-trends/',
};

let currentPage = 1;
let chart = null;

/* DOM */

const salesTab = document.getElementById('sales-tab-button');
const analyticsTab = document.getElementById('analytics-tab-button');

const salesSection = document.getElementById('sales-section');
const analyticsSection = document.getElementById('analytics-section');

const bookSearchInput = document.getElementById('book-search-input');

const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');

const tableBody = document.getElementById('sales-table-body');

const pageIndicator = document.getElementById('page-indicator');

const previousButton = document.getElementById(
	'previous-page-button',
);
const nextButton = document.getElementById('next-page-button');

/* Tabs */

salesTab.addEventListener('click', () => {
	salesTab.classList.add('active');
	analyticsTab.classList.remove('active');

	salesSection.classList.remove('hidden');
	analyticsSection.classList.add('hidden');
});

analyticsTab.addEventListener('click', () => {
	analyticsTab.classList.add('active');
	salesTab.classList.remove('active');

	salesSection.classList.add('hidden');
	analyticsSection.classList.remove('hidden');
});

/* Fetch Helpers */

async function fetchJSON(url) {
	const response = await fetch(url);

	if (!response.ok) {
		throw new Error('Request failed');
	}

	return response.json();
}

/* Table */

function renderTable(results) {
	tableBody.innerHTML = '';

	results.forEach((sale) => {
		tableBody.insertAdjacentHTML(
			'beforeend',

			`
            <tr>

                <td>${sale.id}</td>

                <td>${sale.book.title}</td>

                <td>${sale.book.author}</td>

                <td>${sale.sale_date}</td>

                <td>${sale.quantity}</td>

            </tr>
            `,
		);
	});
}

/* Sales */

async function loadSales(page = 1) {
	const data = await fetchJSON(`${API.sales}?page=${page}`);
	console.log('Data:', data);

	renderTable(data.results);

	pageIndicator.textContent = `Page ${page}`;

	previousButton.disabled = !data.previous;
	nextButton.disabled = !data.next;
}

/* Search */
async function searchBookSales(query) {
	if (!query) {
		loadSales();
		return;
	}

	const data = await fetchJSON(
		`${API.search}?q=${encodeURIComponent(query)}`,
	);

	renderTable(data);
}

function debounce(callback, delay = 300) {
	let timeoutId;

	return (...args) => {
		clearTimeout(timeoutId);

		timeoutId = setTimeout(() => {
			callback(...args);
		}, delay);
	};
}

const debouncedSearch = debounce(async () => {
	const query = searchInput.value.trim();

	await searchBookSales(query);
}, 300);

searchInput.addEventListener('input', debouncedSearch);

/* Pagination */

previousButton.addEventListener('click', () => {
	if (currentPage > 1) {
		currentPage--;

		loadSales(currentPage);
	}
});

nextButton.addEventListener('click', () => {
	currentPage++;

	loadSales(currentPage);
});

/* Chart */

async function handleBookSearchForAnalytics() {
	const data = await fetchJSON(API.books);
	console.log('Books: ', data);
}

bookSearchInput.addEventListener(
	'click',
	handleBookSearchForAnalytics,
);

async function loadAnalytics() {
	const data = await fetchJSON(`${API.trends}?book_id=2`);

	const labels = data.map((item) => item.month);
	const quantities = data.map((item) => item.quantity);

	const ctx = document
		.getElementById('sales-trend-chart')
		.getContext('2d');

	if (chart) {
		chart.destroy();
	}

	chart = new Chart(ctx, {
		type: 'bar',

		data: {
			labels,

			datasets: [
				{
					label: 'Books Sold',
					data: quantities,
				},
			],
		},
	});
}

/**************************************************************************
 * Initial Load
 **************************************************************************/

window.addEventListener('DOMContentLoaded', () => {
	loadSales();

	loadAnalytics();
});
