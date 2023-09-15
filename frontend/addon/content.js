// Content script (content.js)
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "checkPhishing") {
    const url = window.location.href;
      fetch("127.0.0.1:5000/checkurl", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url }),
    })
      .then((response) => response.json())
      .then((data) => {
          if (data.confidence>= 0.7) {
              // High probability of phishing, block the page
	      alert("HELLO")
          chrome.runtime.sendMessage({ action: "blockPage" });
        }
      })
      .catch((error) => {
        console.error("Error checking phishing:", error);
      });
  }
});
