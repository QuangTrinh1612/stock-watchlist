// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
    // Elements
    const watchlistContainer = document.getElementById("watchlist");
    const stockDetailsContainer = document.getElementById("stock-details");
    const addStockForm = document.getElementById("add-stock-form");
    const removeStockForm = document.getElementById("remove-stock-form");
  
    // Base API URL
    const BASE_API_URL = "http://127.0.0.1:8000/api";
  
    /**
     * Fetch and display the watchlist
     */
    async function fetchWatchlist() {
      try {
        const response = await fetch(`${BASE_API_URL}/watchlist`);
        const data = await response.json();
        if (response.ok) {
          displayWatchlist(data.watchlist);
        } else {
          console.error("Error fetching watchlist:", data.detail);
        }
      } catch (error) {
        console.error("Error fetching watchlist:", error);
      }
    }
  
    /**
     * Display the watchlist in the DOM
     */
    function displayWatchlist(watchlist) {
      watchlistContainer.innerHTML = "";
      if (watchlist.length === 0) {
        watchlistContainer.innerHTML = "<p>Your watchlist is empty.</p>";
        return;
      }
      const list = document.createElement("ul");
      watchlist.forEach((ticker) => {
        const listItem = document.createElement("li");
        listItem.textContent = ticker;
        list.appendChild(listItem);
      });
      watchlistContainer.appendChild(list);
    }
  
    /**
     * Fetch stock price details
     */
    async function fetchStockDetails(ticker) {
      try {
        const response = await fetch(`${BASE_API_URL}/stock/${ticker}/price`);
        const data = await response.json();
        if (response.ok) {
          displayStockDetails(data);
        } else {
          console.error("Error fetching stock details:", data.detail);
        }
      } catch (error) {
        console.error("Error fetching stock details:", error);
      }
    }
  
    /**
     * Display stock details in the DOM
     */
    function displayStockDetails(stock) {
      stockDetailsContainer.innerHTML = `
        <h2>Stock Details</h2>
        <p><strong>Ticker:</strong> ${stock.ticker}</p>
        <p><strong>Price:</strong> $${stock.price.toFixed(2)}</p>
      `;
    }
  
    /**
     * Add a stock to the watchlist
     */
    async function addStockToWatchlist(ticker) {
      try {
        const response = await fetch(`${BASE_API_URL}/watchlist`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ ticker }),
        });
        const data = await response.json();
        if (response.ok) {
          alert(data.message);
          fetchWatchlist(); // Refresh the watchlist
        } else {
          console.error("Error adding stock:", data.detail);
        }
      } catch (error) {
        console.error("Error adding stock:", error);
      }
    }
  
    /**
     * Remove a stock from the watchlist
     */
    async function removeStockFromWatchlist(ticker) {
      try {
        const response = await fetch(`${BASE_API_URL}/watchlist`, {
          method: "DELETE",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ ticker }),
        });
        const data = await response.json();
        if (response.ok) {
          alert(data.message);
          fetchWatchlist(); // Refresh the watchlist
        } else {
          console.error("Error removing stock:", data.detail);
        }
      } catch (error) {
        console.error("Error removing stock:", error);
      }
    }
  
    // Event Listeners
    addStockForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const tickerInput = addStockForm.querySelector("input[name='ticker']");
      const ticker = tickerInput.value.trim();
      if (ticker) {
        addStockToWatchlist(ticker);
        tickerInput.value = ""; // Clear the input field
      }
    });
  
    removeStockForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const tickerInput = removeStockForm.querySelector("input[name='ticker']");
      const ticker = tickerInput.value.trim();
      if (ticker) {
        removeStockFromWatchlist(ticker);
        tickerInput.value = ""; // Clear the input field
      }
    });
  
    // Initial Fetch
    fetchWatchlist();
  });  