async function sendData() {
  const input = document.getElementById("jsonInput").value;
  const output = document.getElementById("responseOutput");

  try {
    const jsonData = JSON.parse(input);
    const response = await fetch("/data", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(jsonData),
    });
    const result = await response.json();
    output.textContent = JSON.stringify(result, null, 2);
  } catch (err) {
    output.textContent = "Invalid JSON input!";
  }
}
