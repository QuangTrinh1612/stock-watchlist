document.addEventListener("DOMContentLoaded", () => {
    const watchlistTable = document.getElementById("watchlist-table").querySelector("tbody");
    const addStockForm = document.getElementById("add-stock-form");
    const tickerInput = document.getElementById("ticker-input");

    // Fetch watchlist from the server
    const fetchWatchlist = async () => {
        const response = await fetch("/api/watchlist");
        const data = await response.json();
        watchlistTable.innerHTML = "";
        data.watchlist.forEach(ticker => addRow(ticker));
    };

    // Add a new stock to the table
    const addRow = (ticker) => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${ticker}</td>
            <td id="price-${ticker}">Loading...</td>
            <td><button onclick="removeStock('${ticker}')">Remove</button></td>
        `;
        watchlistTable.appendChild(row);
        fetchPrice(ticker);
    };

    // Fetch stock price
    const fetchPrice = async (ticker) => {
        const response = await fetch(`/api/stock/${ticker}/price`);
        const data = await response.json();
        const priceCell = document.getElementById(`price-${ticker}`);
        priceCell.textContent = data.price ? `$${data.price.toFixed(2)}` : "Error";
    };

    // Add stock to watchlist
    addStockForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const ticker = tickerInput.value.trim();
        if (!ticker) return;
        const response = await fetch("/api/watchlist", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ticker }),
        });
        if (response.ok) {
            addRow(ticker);
            tickerInput.value = "";
        }
    });

    // Remove stock from watchlist
    window.removeStock = async (ticker) => {
        const response = await fetch("/api/watchlist", {
            method: "DELETE",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ ticker }),
        });
        if (response.ok) {
            fetchWatchlist();
        }
    };

    // Initialize
    fetchWatchlist();
});
