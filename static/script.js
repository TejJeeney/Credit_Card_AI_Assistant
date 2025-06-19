// document.addEventListener("DOMContentLoaded", function () {
//   const form = document.getElementById("advisor-form");

//   form.addEventListener("submit", async (e) => {
//     e.preventDefault(); // 🚫 Prevent page refresh

//     const income = parseInt(form.income.value);
//     const spend = parseInt(form.spend.value);
//     const benefits = form.benefits.value.split(",").map(b => b.trim().toLowerCase());

//     try {
//       const response = await fetch("http://127.0.0.1:5000/recommend", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json"
//         },
//         body: JSON.stringify({
//           income: income,
//           spend: spend,
//           benefits: benefits
//         })
//       });

//       const data = await response.json();

//       const results = document.getElementById("results");
//       results.innerHTML = ""; // Clear previous results

//       if (data.length === 0) {
//         results.innerHTML = "<p>No matching cards found.</p>";
//         return;
//       }

//       data.forEach(card => {
//         const cardDiv = document.createElement("div");
//         cardDiv.className = "card";
//         cardDiv.innerHTML = `
//           <h3>${card.name}</h3>
//           <p><strong>Estimated Rewards:</strong> ${card.estimated_rewards}</p>
//           <p><strong>Reasons:</strong></p>
//           <ul>${card.reasons.map(reason => `<li>${reason}</li>`).join("")}</ul>
//         `;
//         results.appendChild(cardDiv);
//       });

//     } catch (err) {
//       alert("Error contacting the server. Make sure the backend is running.");
//       console.error(err);
//     }
//   });
// });


document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("advisor-form");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const income = parseInt(form.income.value);
    const spend = parseInt(form.spend.value);
    const benefits = form.benefits.value.split(",").map(b => b.trim());

    try {
      const response = await fetch("/recommend", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ income, spend, benefits })
      });

      const data = await response.json();

      const results = document.getElementById("results");
      results.innerHTML = ""; // Clear old results

      if (data.error) {
        results.innerHTML = `<p style="color:red;">Error: ${data.error}</p>`;
        return;
      }

      // Show the AI's response as formatted text
      results.innerHTML = `
        <h3 style="color:#58a6ff;">Top Recommendations (AI-Powered):</h3>
        <pre style="background:#0d1117; color:#c9d1d9; padding:15px; border-radius:10px;">${data.ai_response}</pre>
      `;
    } catch (err) {
      console.error("Request failed:", err);
      alert("Something went wrong while fetching recommendations.");
    }
  });
});
