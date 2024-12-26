// Fetch and render the watchlist from the API
async function fetchWatchlist() {
  const apiUrl = "http://127.0.0.1:8000/api/watchlist";
  try {
      const response = await fetch(apiUrl);
      if (!response.ok) {
          throw new Error(`Failed to fetch watchlist: ${response.statusText}`);
      }
      const data = await response.json();
      renderWatchlist(data);
  } catch (error) {
      console.error("Error fetching watchlist:", error);
      alert("Unable to load the watchlist. Please try again later.");
  }
}

// Render the watchlist table
function renderWatchlist(watchlist) {
  const tableBody = document.querySelector("#watchlist-table tbody");
  tableBody.innerHTML = ""; // Clear existing rows

  watchlist.forEach(stock => {
      const row = document.createElement("tr");

      // Ticker column
      const tickerCell = document.createElement("td");
      tickerCell.textContent = stock.ticker;
      row.appendChild(tickerCell);

      // Current Price column
      const priceCell = document.createElement("td");
      priceCell.textContent = `$${stock.current_price.toFixed(2)}`;
      row.appendChild(priceCell);

      // Actions column
      const actionsCell = document.createElement("td");
      const deleteButton = document.createElement("button");
      deleteButton.textContent = "Remove";
      deleteButton.onclick = () => removeStock(stock.ticker);
      actionsCell.appendChild(deleteButton);
      row.appendChild(actionsCell);

      tableBody.appendChild(row);
  });
}

// Add a stock to the watchlist
async function addStock(event) {
  event.preventDefault();
  const apiUrl = "http://127.0.0.1:8000/api/watchlist";
  const tickerInput = document.getElementById("ticker-input");
  const ticker = tickerInput.value.trim().toUpperCase();

  if (!ticker) {
      alert("Please enter a valid ticker.");
      return;
  }

  try {
      const response = await fetch(apiUrl, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ ticker })
      });

      if (!response.ok) {
          throw new Error(`Failed to add stock: ${response.statusText}`);
      }

      tickerInput.value = ""; // Clear the input field
      fetchWatchlist(); // Refresh the watchlist
  } catch (error) {
      console.error("Error adding stock:", error);
      alert("Unable to add the stock. Please try again later.");
  }
}

// Remove a stock from the watchlist
async function removeStock(ticker) {
  const apiUrl = `http://127.0.0.1:8000/api/watchlist/${ticker}`;
  try {
      const response = await fetch(apiUrl, { method: "DELETE" });

      if (!response.ok) {
          throw new Error(`Failed to remove stock: ${response.statusText}`);
      }

      fetchWatchlist(); // Refresh the watchlist
  } catch (error) {
      console.error("Error removing stock:", error);
      alert("Unable to remove the stock. Please try again later.");
  }
}

// Initialize the watchlist and form event listener
document.addEventListener("DOMContentLoaded", () => {
  fetchWatchlist();

  const addStockForm = document.getElementById("add-stock-form");
  addStockForm.addEventListener("submit", addStock);
});
