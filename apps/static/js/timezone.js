function updateTimezoneIfNeeded() {
  const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
  if (localStorage.getItem("timezone") !== tz) {
    fetch(setTimezoneUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify({ timezone: tz }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.status === "success") {
          localStorage.setItem("timezone", tz);
        }
      });
  }
}

document.addEventListener("DOMContentLoaded", updateTimezoneIfNeeded);
