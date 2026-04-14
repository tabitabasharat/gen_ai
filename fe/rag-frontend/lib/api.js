const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function sendMessage(message) {
  const res = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      query: message,
    }),
  });

  if (!res.ok) throw new Error("Failed to fetch");

  const data = await res.json();
  console.log("responseeeeee", data);
  return data;

}
