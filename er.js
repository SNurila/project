async function summarizeText() {
    const text = document.getElementById("inputText").value;
    if (!text.trim()) {
      alert("Please enter some text to summarize!");
      return;
    }
  
    try {
      const res = await fetch("/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
      });
  
      if (!res.ok) throw new Error("Server error while summarizing!");
  
      const data = await res.json();
      document.getElementById("summaryBox").innerText = data.summary;
    } catch (err) {
      console.error(err);
      alert("Something went wrong. Check your input or try again.");
    }
  }